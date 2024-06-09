import os
import sys
import time
import requests
import subprocess
import tkinter as tk
from tkinter import messagebox

def check_for_updates(current_version):
    while True:  # Replace with your current version
        owner = 'ACCFIT'
        repo = 'Stream-Deck-Alerts'
        api_url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            latest_release = response.json()
            latest_version = latest_release['tag_name']

            if latest_version != current_version:
                root = tk.Tk()
                root.withdraw()
                install_update = messagebox.askyesno(
                    'Update Available',
                    f'An update (v{latest_version}) is available. Install now?'
                )
                root.destroy()

                if install_update:
                    download_url = latest_release['assets'][0]['browser_download_url']
                    download_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'new_version.exe')
                    download_file(download_url, download_path)
                    restart_with_new_version(download_path)
            time.sleep(5)
        except requests.RequestException as e:
            print('Error checking for updates:', e)

def download_file(url, path):
    print(f'Downloading {url}')
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

def restart_with_new_version(new_version_path):
    print('Restarting with the new version...')
    time.sleep(2)  # Give time for user to read any messages
    subprocess.Popen([sys.executable, new_version_path])
    sys.exit()