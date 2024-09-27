# -- Automatic Update Code (In Progress) -- #

#import os
#import sys
#import time
#import requests
#import subprocess
#import tkinter as tk
#from tkinter import messagebox
#
#REPO_OWNER = 'accfit'
#REPO_NAME = 'athey-deck'
#CHECK_INTERVAL = 3600  # Check every hour (3600 seconds)
#
#def check_for_updates():
#    global latest_release
#    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases/latest'
#    response = requests.get(url)
#    if response.status_code == 200:
#        release_data = response.json()
#        latest_tag = release_data['tag_name']
#        if latest_release is None or latest_release != latest_tag:
#            latest_release = latest_tag
#            show_update_notification(release_data)
#    else:
#        print('Failed to fetch release information from GitHub')
#        
#def show_update_notification(release_data):
#    def on_click(icon, item):
#        root = Tk()
#        root.withdraw()  # Hide the root window
#        user_response = messagebox.askyesno(
#            'Update Available', f'A new version ({latest_release}) is available. Do you want to update now?')
#        if user_response:
#            download_and_install_update(release_data)
#        root.destroy()
#
#    image = Image.new('RGB', (64, 64), color1)
#    icon = pystray.Icon('UpdateNotifier', image, 'Update Notifier', menu=pystray.Menu(item('Check for updates', on_click)))
#    icon.run()
#    
#def download_and_install_update(release_data):
#    # Find the .exe asset
#    for asset in release_data['assets']:
#        if asset['name'].endswith('.exe'):
#            exe_url = asset['browser_download_url']
#            break
#    else:
#        messagebox.showerror('Error', 'No executable update found.')
#        return
#
#    # Download the .exe file
#    exe_name = os.path.basename(urlparse(exe_url).path)
#    response = requests.get(exe_url, stream=True)
#    with open(exe_name, 'wb') as f:
#        for chunk in response.iter_content(chunk_size=8192):
#            if chunk:
#                f.write(chunk)
#    
#    # Run the .exe installer
#    os.startfile(exe_name)
#
#def download_file(url, path):
#    print(f'Downloading {url}')
#    with requests.get(url, stream=True) as r:
#        r.raise_for_status()
#        with open(path, 'wb') as f:
#            for chunk in r.iter_content(chunk_size=8192):
#                if chunk:
#                    f.write(chunk)
#
#def restart_with_new_version(new_version_path):
#    print('Restarting with the new version...')
#    time.sleep(2)  # Give time for user to read any messages
#    subprocess.Popen([sys.executable, new_version_path])
#    sys.exit()