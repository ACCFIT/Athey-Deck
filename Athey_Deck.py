# Name: Athey Deck
# Author: Ben Anderson
# Description: Athey Deck system that integrates with milestone and briefcam to give real-time alerts and user operation.
# TO CREATE AN .exe run this in terminal: pyinstaller Athey_Deck.spec

# -- Imports -- #
from flask import Flask, request
from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper
from PIL import Image, ImageOps
from waitress import serve
import threading
import pyautogui
from pynput.keyboard import Key, Controller
import json
import time
import os
import win32gui
import win32api
import win32con
import logging
import pystray
from pystray import MenuItem as item
import ctypes
import sys
import signal
import psutil
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from gui import LicensePlateManager
from init import *
from PyQt5.QtWidgets import QApplication

#Create initial object for streamdeck control
myicon = Icon()

#Initialize keyboard control
keyboard = Controller()

#Get documents folder path
documents_folder = os.path.join(os.path.expanduser('~'), 'Documents')

#Set path for logging
log_file_path = os.path.join(documents_folder, 'AtheyDeck.log')

#Define logging configuration
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

#LOCK FILES for only keeping one instance of program running, not multiple.
LOCK_FILE = os.path.join(documents_folder, "AtheyDeck.lock")

app = Flask(__name__) #Start Flask (Flask is used for webhooks)

#Threading events for alarms
test2 = threading.Event() 
poi_yellow = threading.Event()
poi_orange = threading.Event()
poi_red = threading.Event()
lpr_yellow = threading.Event()
lpr_orange = threading.Event()
lpr_red = threading.Event()
brett = threading.Event()

verify_time = time.time() #Time verification flag for to make sure alerts are working (This is logged in the log file for reference)
verify_interval = 1900 
button_pressed_flag = False #Button pressed flag for when button is pressed the callback function is referenced (key_change_callback())
key_press_amount = [0] * 15 #Amount of times the keys are pressed
processing_key_press = False #Button pressed flag for delaying multiple key presses
last_key_press_time = 0
debounce_interval = 0.2

bean_counter = 0 #Easter egg
bean_flag = threading.Event()
bean_time = time.time()

briefcam = threading.Event() #Future update with separate briefcam thread processing
briefcam_set = False

fullscreen_flag = False #Check if Briefcam is fullscreen

#Web browser configuration
options = webdriver.FirefoxOptions()
options.add_argument("--kiosk")
options.add_argument("--incognito")
driver = webdriver.Firefox(options=options)

# -- Endpoint thread to handle incoming webhooks and check to see if there is an alert -- #
@app.route('/webhooks', methods=['POST']) #Set webhook address and method
def webhook_listener():
    global verify_time
    data = request.get_json() #Get data in json format
    data_str = json.dumps(data) #Convert json to a string

    logging.info("-- Received data from server --")

    if 'TEST2' in data_str: #TEST2 Alarm (Testing purposes)
        test2.set()
        logging.info("TEST2 ALERT")
        
    #Go through license plate file to check for license plate matching
    # !!IMPORTANT!! Briefcam does not send license plate severity level, so this needs to be configured within Athey Deck (Setting license plates in Athey Deck AND Briefcam)
    with open("license_plates.txt", "r") as file: 
        for line in file:
            plate_id, plate_pattern, severity = line.strip().split(",", 2)
            if bool(re.search(plate_pattern, data_str)):
                if 'GREEN' in severity:
                    logging.info("BRETT ARRIVAL/DEPARTURE")
                    brett.set()
                elif 'YELLOW' in severity:
                    logging.info("LPR YELLOW ALERT")
                    if not lpr_yellow.is_set():
                        lpr_yellow.set()
                elif 'ORANGE' in severity:
                    logging.info("LPR ORANGE ALERT")
                    if not lpr_orange.is_set():
                        lpr_orange.set()
                elif 'RED' in severity:
                    logging.info("LPR RED ALERT")
                    if not lpr_red.is_set():
                        lpr_red.set()
                logging.info(data_str)
    
    #Check for Facial recognition alerts
    if 'YELLOW' in data_str and ('South Entrance Facial D1' in data_str or 'South Entrance Facial D2' in data_str or 'East Entrance Facial' in data_str or 'West Entrance Facial' in data_str or 'PTZ Rear Facial' in data_str): #POI Alarm
        if not poi_yellow.is_set():
            poi_yellow.set()
        logging.info("POI YELLOW ALERT")
        logging.info(data_str)
    elif 'ORANGE' in data_str and ('South Entrance Facial D1' in data_str or 'South Entrance Facial D2' in data_str or 'East Entrance Facial' in data_str or 'West Entrance Facial' in data_str or 'PTZ Rear Facial' in data_str): #POI Alarm
        if not poi_orange.is_set():
            poi_orange.set()
        logging.info("POI ORANGE ALERT")
        logging.info(data_str)
    elif 'RED' in data_str and ('South Entrance Facial D1' in data_str or 'South Entrance Facial D2' in data_str or 'East Entrance Facial' in data_str or 'West Entrance Facial' in data_str or 'PTZ Rear Facial' in data_str): #POI Alarm
        if not poi_red.is_set():
            poi_red.set()
        logging.info("POI RED ALERT")
        logging.info(data_str)
    elif 'accf-ms-db1.accf.local' in data_str: #Verification packet
        verify_time = time.time()
        logging.info("Verification webhook received.")
    else: #Clear flags
        test2.clear() 
        poi_yellow.clear()
        poi_orange.clear()
        poi_red.clear()
        lpr_yellow.clear()
        lpr_orange.clear()
        lpr_red.clear()
        brett.clear()
        logging.warning("** No alerts received from server **")
        logging.info(data_str)
    data_str = None
    return 'OK'

# -- Code to start running the stream deck -- #
def stream_deck_run():
    global button_pressed_flag
    global fullscreen_flag
    global briefcam_set
    streamdeck = DeviceManager().enumerate() 
    
    for index, deck in enumerate(streamdeck): #Enumerate through all streamdecks (Only 1 right now)
        deck.open()
        deck.reset()

        #Scale images
        myicon.image_init(deck)

        #Set initial images
        myicon.set_keys_normal(deck)

        #Run key callback function for when a button is pressed
        deck.set_key_callback(key_change_callback) 
        time.sleep(1)
        briefcam_wrapper()
        driver.get("https://10.100.24.11/app/login") #Initial log in page for web browser
        while 1: #While loop while thread is running
            #Wait for the alarm/event to be set from webhook
            #Check alarm flags
            if test2.is_set(): #Testing flag with future update testing
                deck.set_key_image(7, PILHelper.to_native_key_format(deck, myicon.poi_image_red))
                while not button_pressed_flag:
                    myicon.set_red_alarm(deck)
                    if briefcam_set is False:
                        briefcam_wrapper()
                        briefcam_set = True
                myicon.set_keys_normal(deck)
                test2.clear()
                briefcam_set = False
            elif lpr_yellow.is_set():
                set_briefcam()
                briefcam_login() 
                deck.set_key_image(7, PILHelper.to_native_key_format(deck, myicon.lpr_image_yellow))
                while not button_pressed_flag:
                    myicon.set_yellow_alarm(deck)
                myicon.set_keys_normal(deck)
                lpr_yellow.clear()
            elif lpr_orange.is_set():
                set_briefcam()
                briefcam_login() 
                deck.set_key_image(7, PILHelper.to_native_key_format(deck, myicon.lpr_image_orange))
                while not button_pressed_flag:
                    myicon.set_orange_alarm(deck)
                myicon.set_keys_normal(deck)
                lpr_orange.clear()
            elif lpr_red.is_set():
                set_briefcam()
                briefcam_login() 
                deck.set_key_image(7, PILHelper.to_native_key_format(deck, myicon.lpr_image_red))
                while not button_pressed_flag:
                    myicon.set_red_alarm(deck)
                myicon.set_keys_normal(deck)
                lpr_red.clear()
            elif poi_yellow.is_set(): 
                set_briefcam()
                briefcam_login()                                                                                      
                deck.set_key_image(7, PILHelper.to_native_key_format(deck, myicon.poi_image_yellow))
                while not button_pressed_flag:
                    myicon.set_yellow_alarm(deck)
                myicon.set_keys_normal(deck)
                poi_yellow.clear()
            elif poi_orange.is_set(): 
                set_briefcam()
                briefcam_login()                                                                                      
                deck.set_key_image(7, PILHelper.to_native_key_format(deck, myicon.poi_image_orange))
                while not button_pressed_flag:
                    myicon.set_orange_alarm(deck)
                myicon.set_keys_normal(deck)
                poi_orange.clear()
            elif poi_red.is_set(): 
                set_briefcam()
                briefcam_login()                                                                                     
                deck.set_key_image(7, PILHelper.to_native_key_format(deck, myicon.poi_image_red))
                while not button_pressed_flag:
                    myicon.set_red_alarm(deck)
                myicon.set_keys_normal(deck)
                poi_red.clear()
            elif brett.is_set():
                deck.set_key_image(7, PILHelper.to_native_key_format(deck, myicon.brett_image))
                myicon.set_brett_keys(deck)
                while not button_pressed_flag:
                    pass
                myicon.set_keys_normal(deck)
                brett.clear()
            elif bean_flag.is_set():
                myicon.set_bean_keys(deck)
                myicon.set_keys_normal(deck)
                bean_flag.clear()
            elif briefcam.is_set():
                briefcam_login()
                briefcam.clear()
            button_pressed_flag = False
            time.sleep(0.05) #Sleep for a bit to reduce processing load
    driver.quit()

def timeout(): #Check verification packet. Log an error if there is too much time between packets.
    if time.time() - verify_time > verify_interval:
        return True
    else:
        return False

# -- Callback function to see if a button has been pressed on streamdeck -- #
def key_change_callback(deck, key, state):
    global button_pressed_flag
    global processing_key_press
    global last_key_press_time
    global bean_counter
    global bean_flag
    global bean_time
    global key_press_amount
    
    #Logic for button press feedback
    if state == True: 
        for i in range(15):
            if key_press_amount[i] == 1:
                return
        key_press_amount[key] = 1
        myicon.key_press_get(deck, key)
        time.sleep(0.2)
        return
    elif state == False:
        key_press_amount[key] = 0
        for i in range(15):
            if key_press_amount[i] == 1:
                logging.warn("Multiple Keys Pressed, Not registering key press")
                return
        myicon.key_press_normal(deck, key)
    
    #Set current time
    current_time = time.time()

    #Debounce interval for pressing keys to quickly in succession
    if current_time - last_key_press_time < debounce_interval:
        return False
    last_key_press_time = current_time
    
    #Easter egg counter
    if bean_counter == 1:
        bean_time = time.time()
    elif bean_counter >= 1:
        if bean_time - time.time() > 60:
            bean_counter = 0

    button_pressed_flag = True
    try:
        if key == 0 or key == 1 or key == 2 or key == 3 or key == 4 or key == 5 or key == 6 or key == 8 or key == 9:
            set_monitor() #Check which application is in focus before handling button press
            logging.info("Set Monitor")
        if key == 0:
            logging.info("Before key 1 is pressed")
            keyboard.press(Key.ctrl)
            keyboard.press(Key.shift)
            keyboard.press('1')
            keyboard.release('1')
            keyboard.release(Key.shift)
            keyboard.release(Key.ctrl)
            #pyautogui.hotkey('ctrl', 'shift', '1') #OLD CODE DEPRECATED (Leaving it here for future possibility of use again)
            logging.info("After key 1 Pressed")
        elif key == 1:
            logging.info("Before key 2 is pressed")
            keyboard.press(Key.ctrl)
            keyboard.press(Key.shift)
            keyboard.press('2')
            keyboard.release('2')
            keyboard.release(Key.shift)
            keyboard.release(Key.ctrl)
            #pyautogui.hotkey('ctrl', 'shift', '2')
            logging.info("After key 2 Pressed")
        elif key == 2:
            logging.info("Before key 3 is pressed")
            keyboard.press(Key.ctrl)
            keyboard.press(Key.shift)
            keyboard.press('3')
            keyboard.release('3')
            keyboard.release(Key.shift)
            keyboard.release(Key.ctrl)
            #pyautogui.hotkey('ctrl', 'shift', '3')
            logging.info("After key 3 Pressed")
        elif key == 3:
            logging.info("Before key 4 is pressed")
            keyboard.press(Key.ctrl)
            keyboard.press(Key.shift)
            keyboard.press('4')
            keyboard.release('4')
            keyboard.release(Key.shift)
            keyboard.release(Key.ctrl)
            #pyautogui.hotkey('ctrl', 'shift', '4')
            logging.info("After key 4 Pressed")
        elif key == 4:
            logging.info("Before key 5 is pressed")
            keyboard.press(Key.ctrl)
            keyboard.press(Key.shift)
            keyboard.press('5')
            keyboard.release('5')
            keyboard.release(Key.shift)
            keyboard.release(Key.ctrl)
            #pyautogui.hotkey('ctrl', 'shift', '5')
            logging.info("After key 5 Pressed")
        elif key == 5:
            logging.info("Before key 6 is pressed")
            keyboard.press(Key.ctrl)
            keyboard.press(Key.shift)
            keyboard.press('6')
            keyboard.release('6')
            keyboard.release(Key.shift)
            keyboard.release(Key.ctrl)
            logging.info("After key 6 Pressed")
        elif key == 6:
            logging.info("Before key 7 is pressed")
            keyboard.press(Key.ctrl)
            keyboard.press(Key.shift)
            keyboard.press('7')
            keyboard.release('7')
            keyboard.release(Key.shift)
            keyboard.release(Key.ctrl)
            logging.info("After key 7 Pressed")
        elif key == 7:
            logging.info("Before Briefcam is pressed")
            set_briefcam() 
            briefcam.set()
            logging.info("After Briefcam is pressed")
            bean_counter += 1
        elif key == 8:
            logging.info("Before key AD1 is pressed")
            keyboard.press(Key.ctrl)
            keyboard.press(Key.shift)
            keyboard.press('8')
            keyboard.release('8')
            keyboard.release(Key.shift)
            keyboard.release(Key.ctrl)
            logging.info("After key AD1 Pressed")
        elif key == 9:
            logging.info("Before key AD2 is pressed")
            keyboard.press(Key.ctrl)
            keyboard.press(Key.shift)
            keyboard.press('9')
            keyboard.release('9')
            keyboard.release(Key.shift)
            keyboard.release(Key.ctrl)
            logging.info("After key AD2 Pressed")
        if timeout() == True:
            logging.error("ERROR - CHECK WEBHOOK ALERTS")
        if bean_counter >= 10:
            bean_flag.set()
            bean_counter = 0
    except Exception as button_error:
        logging.error("Failed to recieve button press function: ", button_error)
    logging.info("Returning True. Got key press # ")
    logging.info(key)
    return True

## -- For creation of .exe (Leave this commented out for future testing) -- #
#def resource_path(relative_path):
#    try:
#        base_path = sys._MEIPASS
#    except Exception:
#        base_path = os.path.abspath("img/")
#
#    return os.path.join(base_path, relative_path)

# -- Setting monitor focus for what application is in focus -- #
def set_monitor():
    window_handle = None
    try:
        window_handle = win32gui.FindWindowEx(0, window_handle, None, "Milestone XProtect Smart Client")
        if window_handle == 0 or window_handle == None:
            logging.error("Failed to get Window handle")
            return False
        win32gui.ShowWindow(window_handle, win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(window_handle)
        logging.info("Got milestone window handle and returning True")
        return True
    except:
        logging.error("ERROR receiving milestone window handle: ")
        return False

# -- Setting monitor focus for what application is in focus -- #
def set_briefcam():
    window_handle = None
    global fullscreen_flag
    logging.info("Inside briefcam window function")
    try:
        window_handle = win32gui.FindWindowEx(0, window_handle, None, "BriefCam — Mozilla Firefox")
        if window_handle == 0 or window_handle == None:
            window_handle = win32gui.FindWindowEx(0, window_handle, None, "Mozilla Firefox")
            if window_handle == 0 or window_handle == None:
                logging.error("ERROR receiving briefcam window handle. Is Briefcam open?")
                return False

        if window_handle != 0:
            win32gui.ShowWindow(window_handle, win32con.SW_MAXIMIZE)
            win32gui.SetForegroundWindow(window_handle)
            if fullscreen_flag is False:
                pyautogui.press('f11')
                fullscreen_flag = True
            logging.info("Got briefcam window handle and returning True")
            return True
    except:
        logging.error("ERROR receiving briefcam window handle. Is Briefcam open? ")
        return False

# -- Handling exiting of program -- #
def on_exit():
    driver.quit()
    logging.info("-- Stopping Athey Deck - User Exit --")
    remove_lock_file()
    os._exit(1)

# -- Handling restarting of program -- #
def on_restart():
    logging.info("-- Restarting Athey Deck - User Restart --")
    driver.quit()
    os.execl(sys.executable, sys.executable, *sys.argv)

# -- About page of program -- #
def on_about():
    ctypes.windll.user32.MessageBoxW(0, 'ATHEY DECK - v1.1', "Info", 0)

# -- Handling license plate manager -- #
def on_license_add():
    app = QApplication(sys.argv)
    window = LicensePlateManager()
    window.show()
    sys.exit(app.exec_())

# -- Lock file for to only keep on instance of program running (not multiple) -- #
def check_lock_file():
    if os.path.exists(LOCK_FILE): 
        with open(LOCK_FILE, "r") as f:
            old_pid = int(f.read())
            if psutil.pid_exists(old_pid):
                os.kill(old_pid, signal.SIGTERM)
            time.sleep(1)
            f.close()
            remove_lock_file()
            return True

# -- Create Lock file -- #
def create_lock_file():
    with open(LOCK_FILE, "w") as f:
        f.write(str(os.getpid()))
        f.close()

# -- Handle exit signals -- #
def handle_signal(signum, frame):
    os._exit(1)

# -- Remove (delete) lock file -- #
def remove_lock_file():
    os.remove(LOCK_FILE)

# -- Check to see if browser is running -- #
def is_browser_running():
    try:
        driver.current_url  # Attempt to access current_url
        return True  # Browser is running
    except:
        return False  # Browser is not running

# -- Wrapper function for briefcam to run multiple functions -- #
def briefcam_wrapper():
    set_briefcam()
    briefcam_login()

# -- Briefcam login logic -- #
def briefcam_login():
    #Check to see if user is on initial page
    if "10.100.24.11/app/respond/alerts" in driver.current_url:
        return False

    logging.info("Got driver")
    
    # Open the webpage
    driver.get("https://10.100.24.11/app/login")
    logging.info("Opened webpage")
    time.sleep(0.5)
    
    # Read content
    if "10.100.24.11/app/login" in driver.current_url:
        
        #Input information for login
        driver.find_element(By.ID, "userNameField").send_keys(r"accf\SOC")
        driver.find_element(By.ID, 'passwordField').send_keys("GodWithUs!")
        logging.info("Input fields complete")

        #Check checkbox for LDAP
        driver.find_element(By.CLASS_NAME, "PrivateSwitchBase-input").click()
        logging.info('Checked checkbox')
        
        #Find the element to click "Sign In"
        driver.find_element(By.CLASS_NAME, "jss3").click()
        
        logging.info("Logged in")
        time.sleep(0.8)
        
        #Go to Respond page
        driver.get("https://10.100.24.11/app/respond/alerts")
        return True
    else:
        driver.get("https://10.100.24.11/app/respond/alerts")
    
## -- Main Function -- ##
if __name__ == '__main__':
    
    #Check if program is already running
    if check_lock_file():
        logging.info(" ***INSTANCE OF PROGRAM ALREADY RUNNING, RESTARTING PROGRAM***")
    logging.info("Starting Athey Deck")
    logging.info("Checking for alarms...")
    
    #Create lock file for program instance checking
    create_lock_file()

    #Handle program signals
    signal.signal(signal.SIGTERM, handle_signal)
    
    # Create the taskbar icon
    menu = (item('Check for Updates...', None), item('Add License Plates...', on_license_add), item('About', on_about), item('Restart', on_restart), item('Exit', on_exit))
    icon = pystray.Icon("AtheyDeck", Image.open(resource_path('Logo.png')), "ATHEY DECK", menu)

    # Start the webhook app and Stream Deck controller in separate threads
    flask_thread = threading.Thread(target=lambda: serve(app, host='0.0.0.0', port=8096))
    stream_deck_thread = threading.Thread(target=stream_deck_run)
    
    #!UPDATE THREAD NOT CURRENTLY IMPLEMENTED!
    #update_thread = threading.Thread(target=update.check_for_updates(current_version)) 

    # Start the threads
    flask_thread.start()
    stream_deck_thread.start()
    
    #update_thread.start()
    
    icon.run()

    # Wait for the threads to finish and join them back into one process
    flask_thread.join()
    stream_deck_thread.join()
    
    #update_thread.join()