# Athey Deck
A control panel system that integrates with milestone and briefcam to give real-time alerts and user operation.

## Features
* On-Demand visual alerts 
* On-Demand screen changes from milestone to briefcam and vice versa
* Kiosk browser interface via briefcam
* Auto-login for SOC operators

## Running The .EXE
1. Download the `Athey_Deck.exe` under the `dist` folder.
2. Enter the computer's IP address into a webhook on Milestone.
3. Run the .exe on the respective computer with the Stream Deck connected.
4. OPTIONAL: Activate a test rule for testing.

## Creating a New .EXE From Changing The Code
* Pre-requisites to updating the code
    1. Download the program from GitHub and open it in a code editor (Ex: VSCode)
    2. Python is installed (https://www.python.org/downloads/)
    3. Pyinstaller is installed  (Run in terminal: pip install pyinstaller)
    4. Add any other plugins after running pyinstaller
* TO CREATE AN .exe run this in terminal: pyinstaller Athey_Deck.spec
This will overwrite the existing .exe with the new one under /dist

## Webhook Rule Names
The rule names that will work with the stream deck are as follows:
1. TEST2: Testing stream deck alarm - This will send out a red TEST2 alert where it will act as if it got a new alert from Briefcam.

## Pre-Programmed Keyboard Shortcuts
The Athey Deck has pre-programmed shorcuts which interfaces with Milestone.
This is the list of shortcuts already pre-programmed:
1. ctrl-shift-1 = Key 1
2. ctrl-shift-2 = Key 2
3. ctrl-shift-3 = Key 3
4. ctrl-shift-4 = Key 4
5. ctrl-shift-5 = Key 5
6. ctrl-shift-6 = Key 6
7. ctrl-shift-7 = Key 7
9. ctrl-shift-9 = Key AD1
10. ctrl-shift-0 = Key AD2

## Troubleshooting
- Close the ACCF-StreamDeck_Alert.exe window and restart the .exe on the respective computer.
- A log file is saved under the Documents folder for debugging purposes (Named Athey_Deck.txt).

## Known Bugs
- License Plate Manager doesn't show any license plates.
* Solution: Exit the Athey Deck program and start the program from the desktop.
- The buttons stopped working for the camera presets.
* Solution: Restart Milestone, then (OPTIONAL) restart Athey Deck if that doesn't fix it. Milestone seems to crash before Athey Deck will ever crash.