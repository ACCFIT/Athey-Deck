# Name: ACCF Stream Deck Alert System
# Author: Ben Anderson
# Description: Panel interface and functionality and alerts are displayed on the StreamDeck whenever an alert happens through Milestone.
# TO CREATE AN .exe run in terminal: pyinstaller --onefile -w --icon=img\Logo.ico --add-data hidapi.dll:. --add-data "img\Logo.png:." --add-data "img\streamdeck_key1.png:." --add-data "img\streamdeck_key2.png:." --add-data "img\streamdeck_key3.png:." --add-data "img\streamdeck_key1-alert.png:." --add-data "img\streamdeck_key2-alert.png:." --add-data "img\streamdeck_key3-alert.png:." --add-data "img\streamdeck_key4.png:." --add-data "img\streamdeck_key4-alert.png:." --add-data "img\streamdeck_key5.png:." --add-data "img\streamdeck_key5-alert.png:." --add-data "img\TEST2_Alert.png:." --add-data "img\LPR_Alert.png:." --add-data "img\POI_Alert.png:." --add-data "img\Alerts-Disabled.png:." --clean ACCF-StreamDeck_Alert.py

# -- Imports -- #
from flask import Flask, request
from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper
from PIL import Image, ImageOps
from waitress import serve
import threading
import pyautogui
import json
import time
import os
import win32api
import signal
import win32con
import logging
import pystray
from pystray import MenuItem as item
import ctypes
import sys
import signal
import psutil
import re
import queue
from selenium import webdriver
from selenium.webdriver.common.by import By

#Get documents folder path
documents_folder = os.path.join(os.path.expanduser('~'), 'Documents')

#Set path for logging
log_file_path = os.path.join(documents_folder, 'ACCF_StreamDeck.log')

#Define logging config
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

#LOCK FILES for only keeping one instance of program running, not multiple.
LOCK_FILE = os.path.join(documents_folder, "ACCF_StreamDeck.lock")

app = Flask(__name__) #Start Flask (Flask is used for webhooks)

test2 = threading.Event() #Threading events for alarms
poi_yellow = threading.Event()
poi_orange = threading.Event()
poi_red = threading.Event()
lpr_yellow = threading.Event()
lpr_orange = threading.Event()
lpr_red = threading.Event()
brett = threading.Event()

onexit = threading.Event()
onrestart = threading.Event()

verify_time = time.time() #Time verification flag for to make sure alerts are working
verify_interval = 1900 
button_pressed_flag = False #Button pressed flag for when button is pressed the callback function is referenced (key_change_callback())
processing_key_press = False #Button pressed flag for delaying multiple key presses
last_key_press_time = 0
debounce_interval = 0.8

#Easter Eggs for Jacob
bean_counter = 0 
bean_flag = threading.Event() 
bean_time = time.time()

#Briefcam events
briefcam = threading.Event()

brett_search = r'\b281P.F\b'

#Set firefox options
options = webdriver.FirefoxOptions()
options.add_argument("--kiosk") #Set to kiosk mode
driver = webdriver.Firefox(options=options)

# -- Endpoint thread to handle incoming webhooks and check to see if there is an alert -- #
@app.route('/webhooks', methods=['POST']) #Set webhook address and method
def webhook_listener():
    global verify_time #Verify time for webhook verifications
    global onrestart
    global onexit
    data = request.get_json() #Get data in json format
    data_str = json.dumps(data) #Convert json to a string

    logging.info("-- Received data from server --")
    

    if 'TEST2' in data_str: #TEST2 Alarm for admin testing
        test2.set()
        logging.info("TEST2 ALERT") 
    elif '281PQF' in data_str or bool(re.search(brett_search, data_str)): #Pastor Brett Arrival/Departure
        brett.set()
        logging.info("Brett Arrival/Departure")
        logging.info(data_str)
    elif 'YELLOW' in data_str and ('West Exiting LPR' in data_str or 'West Entering LPR' in data_str or 'East Exiting LPR' in data_str or 'East Entering LPR' in data_str): #LPR Alarm
        lpr_yellow.set()
        logging.info("LPR YELLOW ALERT")
        logging.info(data_str)
    elif 'ORANGE' in data_str and ('West Exiting LPR' in data_str or 'West Entering LPR' in data_str or 'East Exiting LPR' in data_str or 'East Entering LPR' in data_str): #LPR Alarm
        lpr_orange.set()
        logging.info("LPR ORANGE ALERT")
        logging.info(data_str)
    elif 'RED' in data_str and ('West Exiting LPR' in data_str or 'West Entering LPR' in data_str or 'East Exiting LPR' in data_str or 'East Entering LPR' in data_str): #LPR Alarm
        lpr_red.set()
        logging.info("LPR RED ALERT")
        logging.info(data_str)
    elif 'YELLOW' in data_str and ('South Entrance Facial D1' in data_str or 'South Entrance Facial D2' in data_str or 'East Entrance Facial' in data_str or 'West Entrance Facial' in data_str): #POI Alarm
        poi_yellow.set()
        logging.info("POI YELLOW ALERT")
        logging.info(data_str)
    elif 'ORANGE' in data_str and ('South Entrance Facial D1' in data_str or 'South Entrance Facial D2' in data_str or 'East Entrance Facial' in data_str or 'West Entrance Facial' in data_str): #POI Alarm
        poi_orange.set()
        logging.info("POI ORANGE ALERT")
        logging.info(data_str)
    elif 'RED' in data_str and ('South Entrance Facial D1' in data_str or 'South Entrance Facial D2' in data_str or 'East Entrance Facial' in data_str or 'West Entrance Facial' in data_str): #POI Alarm
        poi_red.set()
        logging.info("POI RED ALERT")
        logging.info(data_str)
    elif 'accf-ms-db1.accf.local' in data_str: #Verification packet
        verify_time = time.time()
        logging.info("Verification webhook received.")
    else:
        test2.clear() #Clear flags
        poi_yellow.clear()
        poi_orange.clear()
        poi_red.clear()
        lpr_yellow.clear()
        lpr_orange.clear()
        lpr_red.clear()
        brett.clear()
        logging.info("** No alerts received from server **")
        logging.info(data_str)
    data_str = None
    return 'OK'

# -- Code to start running the stream deck -- #
def stream_deck_run():
    global button_pressed_flag #Flag for button pressed
    streamdeck = DeviceManager().enumerate() 
    
    for index, deck in enumerate(streamdeck): #Enumerate through all streamdecks (Only 1 right now)
        deck.open()
        deck.reset()

        #Set image paths
        icon1 = Image.open(resource_path('streamdeck_key1.png')) 
        icon2 = Image.open(resource_path('streamdeck_key2.png'))
        icon3 = Image.open(resource_path('streamdeck_key3.png'))
        icon4 = Image.open(resource_path('streamdeck_key4.png'))
        icon5 = Image.open(resource_path('streamdeck_key5.png'))
        icon1_alert = Image.open(resource_path('streamdeck_key1-alert.png'))
        icon2_alert = Image.open(resource_path('streamdeck_key2-alert.png'))
        icon3_alert = Image.open(resource_path('streamdeck_key3-alert.png'))
        icon4_alert = Image.open(resource_path('streamdeck_key4-alert.png'))
        icon5_alert = Image.open(resource_path('streamdeck_key5-alert.png'))
        test2_alert = Image.open(resource_path('TEST2_Alert.png'))
        lpr_alert = Image.open(resource_path('LPR_Alert.png'))
        poi_alert = Image.open(resource_path('POI_Alert.png'))
        alert_down = Image.open(resource_path('Alerts-Disabled.png'))
        icon1_brett = Image.open(resource_path('streamdeck_key1-brett.png'))
        icon2_brett = Image.open(resource_path('streamdeck_key2-brett.png'))
        icon3_brett = Image.open(resource_path('streamdeck_key3-brett.png'))
        icon4_brett = Image.open(resource_path('streamdeck_key4-brett.png'))
        icon5_brett = Image.open(resource_path('streamdeck_key5-brett.png'))
        brett_alert = Image.open(resource_path('Brett-Alert.png'))
        bean_alert = Image.open(resource_path('tom_hanks_2.png'))
        alert_button = Image.open(resource_path('alert-button.png'))
        icon1_orange = Image.open(resource_path('streamdeck_key1-orange.png'))
        icon2_orange = Image.open(resource_path('streamdeck_key2-orange.png'))
        icon3_orange = Image.open(resource_path('streamdeck_key3-orange.png'))
        icon4_orange = Image.open(resource_path('streamdeck_key4-orange.png'))
        icon5_orange = Image.open(resource_path('streamdeck_key5-orange.png'))
        icon1_yellow = Image.open(resource_path('streamdeck_key1-yellow.png'))
        icon2_yellow = Image.open(resource_path('streamdeck_key2-yellow.png'))
        icon3_yellow = Image.open(resource_path('streamdeck_key3-yellow.png'))
        icon4_yellow = Image.open(resource_path('streamdeck_key4-yellow.png'))
        icon5_yellow = Image.open(resource_path('streamdeck_key5-yellow.png'))
        

        #Scale images
        image1 = PILHelper.create_scaled_key_image(deck, icon1, margins=[0, 0, 0, 0])
        image2 = PILHelper.create_scaled_key_image(deck, icon2, margins=[0, 0, 0, 0])
        image3 = PILHelper.create_scaled_key_image(deck, icon3, margins=[0, 0, 0, 0])
        image4 = PILHelper.create_scaled_key_image(deck, icon4, margins=[0, 0, 0, 0])
        image5 = PILHelper.create_scaled_key_image(deck, icon5, margins=[0, 0, 0, 0])
        image1_alert = PILHelper.create_scaled_key_image(deck, icon1_alert, margins=[0, 0, 0, 0])
        image2_alert = PILHelper.create_scaled_key_image(deck, icon2_alert, margins=[0, 0, 0, 0])
        image3_alert = PILHelper.create_scaled_key_image(deck, icon3_alert, margins=[0, 0, 0, 0])
        image4_alert = PILHelper.create_scaled_key_image(deck, icon4_alert, margins=[0, 0, 0, 0])
        image5_alert = PILHelper.create_scaled_key_image(deck, icon5_alert, margins=[0, 0, 0, 0])
        test2_image = PILHelper.create_scaled_key_image(deck, test2_alert, margins=[0, 0, 0, 0])
        lpr_image = PILHelper.create_scaled_key_image(deck, lpr_alert, margins=[0, 0, 0, 0])
        poi_image = PILHelper.create_scaled_key_image(deck, poi_alert, margins=[0, 0, 0, 0])
        alert_disabled = PILHelper.create_scaled_key_image(deck, alert_down, margins=[0, 0, 0, 0])
        image1_brett = PILHelper.create_scaled_key_image(deck, icon1_brett, margins=[0, 0, 0, 0])
        image2_brett = PILHelper.create_scaled_key_image(deck, icon2_brett, margins=[0, 0, 0, 0])
        image3_brett = PILHelper.create_scaled_key_image(deck, icon3_brett, margins=[0, 0, 0, 0])
        image4_brett = PILHelper.create_scaled_key_image(deck, icon4_brett, margins=[0, 0, 0, 0])
        image5_brett = PILHelper.create_scaled_key_image(deck, icon5_brett, margins=[0, 0, 0, 0])
        brett_image = PILHelper.create_scaled_key_image(deck, brett_alert, margins=[0, 0, 0, 0])
        bean_image = PILHelper.create_scaled_key_image(deck, bean_alert, margins=[0, 0, 0, 0])
        alert_image = PILHelper.create_scaled_key_image(deck, alert_button, margins=[0, 0, 0, 0])
        image1_orange = PILHelper.create_scaled_key_image(deck, icon1_orange, margins=[0, 0, 0, 0])
        image2_orange = PILHelper.create_scaled_key_image(deck, icon2_orange, margins=[0, 0, 0, 0])
        image3_orange = PILHelper.create_scaled_key_image(deck, icon3_orange, margins=[0, 0, 0, 0])
        image4_orange = PILHelper.create_scaled_key_image(deck, icon4_orange, margins=[0, 0, 0, 0])
        image5_orange = PILHelper.create_scaled_key_image(deck, icon5_orange, margins=[0, 0, 0, 0])
        image1_yellow = PILHelper.create_scaled_key_image(deck, icon1_yellow, margins=[0, 0, 0, 0])
        image2_yellow = PILHelper.create_scaled_key_image(deck, icon2_yellow, margins=[0, 0, 0, 0])
        image3_yellow = PILHelper.create_scaled_key_image(deck, icon3_yellow, margins=[0, 0, 0, 0])
        image4_yellow = PILHelper.create_scaled_key_image(deck, icon4_yellow, margins=[0, 0, 0, 0])
        image5_yellow = PILHelper.create_scaled_key_image(deck, icon5_yellow, margins=[0, 0, 0, 0])

        #Set initial images
        set_keys_normal(deck, image1, image2, image3, image4, image5, alert_image)

        #Set key callback function for button presses
        deck.set_key_callback(key_change_callback) 

        while 1: #While loop while thread is running
            # Wait for the event to be set from webhook
            
            #Check alarm flags
            if test2.is_set():
                set_briefcam()
                briefcam_login(driver) 
                deck.set_key_image(4, PILHelper.to_native_key_format(deck, test2_image))
                while not button_pressed_flag:
                    set_red_keys(deck, image1, image2, image3, image4, image5, image1_alert, image2_alert, image3_alert, image4_alert, image5_alert)
                set_keys_normal(deck, image1, image2, image3, image4, image5, alert_image)
                test2.clear()
            elif lpr_yellow.is_set():
                set_briefcam()
                briefcam_login(driver) 
                deck.set_key_image(4, PILHelper.to_native_key_format(deck, lpr_image))
                while not button_pressed_flag:
                    set_yellow_keys(deck, image1, image2, image3, image4, image5, image1_yellow, image2_yellow, image3_yellow, image4_yellow, image5_yellow)
                set_keys_normal(deck, image1, image2, image3, image4, image5, alert_image)
                lpr_yellow.clear()
            elif lpr_orange.is_set():
                set_briefcam()
                briefcam_login(driver) 
                deck.set_key_image(4, PILHelper.to_native_key_format(deck, lpr_image))
                while not button_pressed_flag:
                    set_orange_keys(deck, image1, image2, image3, image4, image5, image1_orange, image2_orange, image3_orange, image4_orange, image5_orange)
                set_keys_normal(deck, image1, image2, image3, image4, image5, alert_image)
                lpr_orange.clear()
            elif lpr_red.is_set():
                set_briefcam()
                briefcam_login(driver) 
                deck.set_key_image(4, PILHelper.to_native_key_format(deck, lpr_image))
                while not button_pressed_flag:
                    set_red_keys(deck, image1, image2, image3, image4, image5, image1_alert, image2_alert, image3_alert, image4_alert, image5_alert)
                set_keys_normal(deck, image1, image2, image3, image4, image5, alert_image)
                lpr_red.clear()
            elif poi_yellow.is_set(): 
                set_briefcam()
                briefcam_login(driver)                                                                                      
                deck.set_key_image(4, PILHelper.to_native_key_format(deck, poi_image))
                while not button_pressed_flag:
                    set_yellow_keys(deck, image1, image2, image3, image4, image5, image1_yellow, image2_yellow, image3_yellow, image4_yellow, image5_yellow)
                set_keys_normal(deck, image1, image2, image3, image4, image5, alert_image)
                poi_yellow.clear()
            elif poi_orange.is_set(): 
                set_briefcam()
                briefcam_login(driver)                                                                                      
                deck.set_key_image(4, PILHelper.to_native_key_format(deck, poi_image))
                while not button_pressed_flag:
                    set_orange_keys(deck, image1, image2, image3, image4, image5, image1_orange, image2_orange, image3_orange, image4_orange, image5_orange)
                set_keys_normal(deck, image1, image2, image3, image4, image5, alert_image)
                poi_orange.clear()
            elif poi_red.is_set(): 
                set_briefcam()
                briefcam_login(driver)                                                                                     
                deck.set_key_image(4, PILHelper.to_native_key_format(deck, poi_image))
                while not button_pressed_flag:
                    set_red_keys(deck, image1, image2, image3, image4, image5, image1_alert, image2_alert, image3_alert, image4_alert, image5_alert)
                set_keys_normal(deck, image1, image2, image3, image4, image5, alert_image)
                poi_red.clear()
            elif brett.is_set():
                deck.set_key_image(4, PILHelper.to_native_key_format(deck, brett_image))
                set_brett_keys(deck, image1_brett, image2_brett, image3_brett, image4_brett, image5_brett)
                while not button_pressed_flag:
                    pass
                set_keys_normal(deck, image1, image2, image3, image4, image5, alert_image)
                brett.clear()
                set_keys_normal(deck, image1, image2, image3, image4, image5, alert_image)
            elif bean_flag.is_set():
                set_bean_keys(deck, bean_image)
                set_keys_normal(deck, image1, image2, image3, image4, image5, alert_image)
                bean_flag.clear()
            elif briefcam.is_set():
                briefcam_login(driver)
                briefcam.clear()
            button_pressed_flag = False
            if not is_browser_running(driver):
                logging.warn("Restarting browser, someone closed it")
                driver.quit()
                driver = webdriver.Firefox(options=options)
                time.sleep(1.5)
                set_briefcam()
            time.sleep(0.05) #Sleep for a bit to reduce processing load
    driver.quit()

# -- Set keys to respective alarm -- #
def set_yellow_keys(deck, image1, image2, image3, image4, image5, image1_yellow, image2_yellow, image3_yellow, image4_yellow, image5_yellow):
    deck.set_key_image(0, PILHelper.to_native_key_format(deck, image1_yellow)) #SET IMAGE TO YELLOW
    deck.set_key_image(1, PILHelper.to_native_key_format(deck, image2_yellow))
    deck.set_key_image(2, PILHelper.to_native_key_format(deck, image3_yellow))
    deck.set_key_image(3, PILHelper.to_native_key_format(deck, image4_yellow))
    deck.set_key_image(5, PILHelper.to_native_key_format(deck, image5_yellow))
    time.sleep(0.5)
    deck.set_key_image(0, PILHelper.to_native_key_format(deck, image1)) #SET TO NORMAL
    deck.set_key_image(1, PILHelper.to_native_key_format(deck, image2))
    deck.set_key_image(2, PILHelper.to_native_key_format(deck, image3))
    deck.set_key_image(3, PILHelper.to_native_key_format(deck, image4))
    deck.set_key_image(5, PILHelper.to_native_key_format(deck, image5))
    time.sleep(0.5)

def set_orange_keys(deck, image1, image2, image3, image4, image5, image1_orange, image2_orange, image3_orange, image4_orange, image5_orange):
    deck.set_key_image(0, PILHelper.to_native_key_format(deck, image1_orange)) #SET IMAGE TO ORANGE
    deck.set_key_image(1, PILHelper.to_native_key_format(deck, image2_orange))
    deck.set_key_image(2, PILHelper.to_native_key_format(deck, image3_orange))
    deck.set_key_image(3, PILHelper.to_native_key_format(deck, image4_orange))
    deck.set_key_image(5, PILHelper.to_native_key_format(deck, image5_orange))
    time.sleep(0.5)
    deck.set_key_image(0, PILHelper.to_native_key_format(deck, image1)) #SET TO NORMAL
    deck.set_key_image(1, PILHelper.to_native_key_format(deck, image2))
    deck.set_key_image(2, PILHelper.to_native_key_format(deck, image3))
    deck.set_key_image(3, PILHelper.to_native_key_format(deck, image4))
    deck.set_key_image(5, PILHelper.to_native_key_format(deck, image5))
    time.sleep(0.5)

def set_red_keys(deck, image1, image2, image3, image4, image5, image1_red, image2_red, image3_red, image4_red, image5_red):
    deck.set_key_image(0, PILHelper.to_native_key_format(deck, image1_red)) #SET IMAGE TO RED
    deck.set_key_image(1, PILHelper.to_native_key_format(deck, image2_red))
    deck.set_key_image(2, PILHelper.to_native_key_format(deck, image3_red))
    deck.set_key_image(3, PILHelper.to_native_key_format(deck, image4_red))
    deck.set_key_image(5, PILHelper.to_native_key_format(deck, image5_red))
    time.sleep(0.5)
    deck.set_key_image(0, PILHelper.to_native_key_format(deck, image1)) #SET TO NORMAL
    deck.set_key_image(1, PILHelper.to_native_key_format(deck, image2))
    deck.set_key_image(2, PILHelper.to_native_key_format(deck, image3))
    deck.set_key_image(3, PILHelper.to_native_key_format(deck, image4))
    deck.set_key_image(5, PILHelper.to_native_key_format(deck, image5))
    time.sleep(0.5)

def set_brett_keys(deck, image1_brett, image2_brett, image3_brett, image4_brett, image5_brett):
    time.sleep(0.05)
    deck.set_key_image(0, PILHelper.to_native_key_format(deck, image1_brett)) #SET IMAGE TO GREEN BRETT
    deck.set_key_image(1, PILHelper.to_native_key_format(deck, image2_brett))
    deck.set_key_image(2, PILHelper.to_native_key_format(deck, image3_brett))
    deck.set_key_image(3, PILHelper.to_native_key_format(deck, image4_brett))
    deck.set_key_image(5, PILHelper.to_native_key_format(deck, image5_brett))
    time.sleep(1)

def set_keys_normal(deck, image1, image2, image3, image4, image5, alert_image):
    time.sleep(0.05)
    deck.set_key_image(0, PILHelper.to_native_key_format(deck, image1)) #SET TO NORMAL
    deck.set_key_image(1, PILHelper.to_native_key_format(deck, image2))
    deck.set_key_image(2, PILHelper.to_native_key_format(deck, image3))
    deck.set_key_image(3, PILHelper.to_native_key_format(deck, image4))
    deck.set_key_image(4, PILHelper.to_native_key_format(deck, alert_image))
    deck.set_key_image(5, PILHelper.to_native_key_format(deck, image5))

def set_bean_keys(deck, bean_image):
    time.sleep(0.05)
    deck.set_key_image(0, PILHelper.to_native_key_format(deck, bean_image))
    deck.set_key_image(1, PILHelper.to_native_key_format(deck, bean_image))
    deck.set_key_image(2, PILHelper.to_native_key_format(deck, bean_image))
    deck.set_key_image(3, PILHelper.to_native_key_format(deck, bean_image))
    deck.set_key_image(4, PILHelper.to_native_key_format(deck, bean_image))
    deck.set_key_image(5, PILHelper.to_native_key_format(deck, bean_image))
    time.sleep(0.5)

# -- Verification timeouts to check webhook verification -- #
def handle_verification_timeout(deck, image):
    if time.time() - verify_time > verify_interval: #Check to see if timeout and set image if so
        logging.error("ERROR - CHECK WEBHOOK ALERTS")

def timeout():
    if time.time() - verify_time > verify_interval:
        return True
    else:
        return False

# -- Callback function to see if a button has been pressed on streamdeck -- #
def key_change_callback(deck, key, state):
    global button_pressed_flag
    global processing_key_press #Flag to check if key has been pressed recently or quickly
    global last_key_press_time
    global bean_counter
    global bean_flag
    global bean_time
    
    if bean_counter == 1:
        bean_time = time.time()
    elif bean_counter >= 1:
        if bean_time - time.time() > 60:
            bean_counter = 0
    
    #Get current time to check key press time
    current_time = time.time()
    
    #If key press is less than last key press (0.8s) then return false
    if current_time - last_key_press_time < debounce_interval:
        return False
    
    #Set new time for key press to check for future key presses
    last_key_press_time = current_time

    button_pressed_flag = True
    try:
        #Check which key has been pressed (0 = key 1) (1 = key 2)...etc.
        if key == 0 or key == 1 or key == 2 or key == 3 or key == 5:
            set_monitor() #Check which application is in focus before handling button press
            time.sleep(0.01) #Sleep for a bit before handling key stroke and setting window focus
        if key == 0:
            pyautogui.hotkey('ctrl', 'shift', '1') #Do keystroke control + shift + 1 
            logging.info("Key 1 Pressed")
        elif key == 1:
            pyautogui.hotkey('ctrl', 'shift', '2') #Same thing above but with + 2
            logging.info("Key 2 Pressed")
        elif key == 2:
            pyautogui.hotkey('ctrl', 'shift', '3')
            logging.info("Key 3 Pressed")
        elif key == 3:
            pyautogui.hotkey('ctrl', 'shift', '4')
            logging.info("Key 4 Pressed")
        elif key == 4:
            set_briefcam() #Set briefcam window in focus
            briefcam.set() #Make sure user is logged in and on correct window
            logging.info("Alert Button Pressed")
            bean_counter += 1
        elif key == 5:
            pyautogui.hotkey('ctrl', 'shift', '5')
            logging.info("Key 5 Pressed")

        if timeout() == True:
            logging.error("ERROR - CHECK WEBHOOK ALERTS")
        if bean_counter >= 10: #Bean counter for Jacob
            bean_flag.set()
            bean_counter = 0
    except Exception as button_error:
        logging.error("Failed to recieve button press function: ", button_error) #Throw exception if something goes wrong
    return True

# -- For creation of .exe and getting correct file paths -- #
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# -- Setting monitor focus to milestone -- #
def set_monitor():
    try:
        window_handle = win32gui.FindWindowEx(0, window_handle, None, "Milestone XProtect Smart Client")
        if window_handle == 0:
            logging.error("Failed to get milestone Window handle")
            return False
        win32gui.ShowWindow(window_handle, win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(window_handle)
        logging.info("Got milestone window handle and returning True")
        return True
    except:
        logging.error("ERROR receiving milestone window handle: ")
        return False

# -- Setting monitor focus to briefcam -- #
def set_briefcam():
    logging.info("Inside briefcam window func")
    try:
        window_handle = win32gui.FindWindowEx(0, window_handle, None, "BriefCam — Mozilla Firefox")
        if window_handle == 0:
            window_handle = win32gui.FindWindowEx(0, window_handle, None, "Mozilla Firefox")
            if window_handle == 0:
                logging.error("ERROR receiving briefcam window handle")
                return False

        if window_handle != 0:
            win32gui.ShowWindow(window_handle, win32con.SW_MAXIMIZE)
            win32gui.SetForegroundWindow(window_handle)
            logging.info("Got briefcam window handle and returning True")
            return True
    except:
        logging.error("ERROR receiving briefcam window handle: ")
        return False

# -- Handling exiting of program -- #
def on_exit():
    driver.quit
    logging.info("Stopping Stream Deck Alarm System - User Exit")
    #icon.stop()
    remove_lock_file()
    os._exit(1)

def on_restart():
    driver.quit()
    os.execl(sys.executable, sys.executable, *sys.argv)
    

# -- Handling about of program -- #
def on_about():
    ctypes.windll.user32.MessageBoxW(0, 'v1.1.3', "Info", 0)

# -- Check lock file so that program can be started again -- #
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

# -- Creation of lock file when user starts program -- #
def create_lock_file():
    with open(LOCK_FILE, "w") as f:
        f.write(str(os.getpid()))
        f.close()

def handle_signal(signum, frame):
    os._exit(1)

def remove_lock_file():
    os.remove(LOCK_FILE)

# -- Check to see if browser is running -- #
def is_browser_running(driver):
    try:
        driver.current_url  # Attempt to access current_url
        return True  # Browser is running
    except:
        return False  # Browser is not running

# -- Login user to briefcam and automate tasks to get to alerts screen -- #
def briefcam_login(driver):
    if "10.100.24.11/app/respond/alerts" in driver.current_url:
        return False

    logging.info("Got driver")

    # Open the webpage
    driver.get("https://10.100.24.11/app/login")
    logging.info("Opened webpage")
    time.sleep(0.5)

    # Read content and login
    if "10.100.24.11/app/login" in driver.current_url:
        driver.find_element(By.ID, "userNameField").send_keys("accf\SOC")
        driver.find_element(By.ID, 'passwordField').send_keys("GodWithUs!")
        logging.info("Input fields complete")

        driver.find_element(By.CLASS_NAME, "PrivateSwitchBase-input").click()
        logging.info('Checked checkbox')

        driver.find_element(By.CLASS_NAME, "jss3").click()
        
        logging.info("Logged in")
        time.sleep(0.8)
        driver.get("https://10.100.24.11/app/respond/alerts")
        return True
    else:
        driver.get("https://10.100.24.11/app/respond/alerts")
    
## -- Main Function -- ##
if __name__ == '__main__':
    if check_lock_file(): #Check to see if program is already running before opening
        logging.info(" ***INSTANCE OF PROGRAM ALREADY RUNNING, RESTARTING PROGRAM***")
    logging.info("Starting Stream Deck Alarm System")
    logging.info("Checking for alarms...")
    
    create_lock_file()

    signal.signal(signal.SIGTERM, handle_signal)
    current_version = 'v1.1.3'

    # Create the icon
    menu = (item('Exit', on_exit), item('About', on_about), item('Restart', on_restart))
    icon = pystray.Icon("StreamDeck", Image.open(resource_path('Logo.png')), "ACCF-StreamDeck", menu)
    
 to see if program is already running before opening
        logging.info(" ***INSTANCE OF PROGRAM ALREADY RUNNING, RESTARTING PROGRAM***")
    logging.info("Starting Stream Deck Alarm System")
    logging.info("Checking for alarms...")
    
    create_lock_file()

    signal.signal(signal.SIGTERM, handle_signal)
    current_version = 'v1.1.3'

    # Create the icon
    menu = (item('Exit', on_exit), item('About', on_about), item('Restart', on_restart))
    icon = pystray.Icon("StreamDeck", Image.open(resource_path('Logo.png')), "ACCF-StreamDeck", menu)
    
    
    # Start the webhook app and Stream Deck controller in separate threads
    flask_thread = threading.Thread(target=lambda: serve(app, host='0.0.0.0', port=8096))
    stream_deck_thread = threading.Thread(target=stream_deck_run)
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