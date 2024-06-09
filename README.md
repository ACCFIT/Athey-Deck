# Athey Deck
Athey Deck system that integrates with milestone and briefcam to give real-time alerts and user operation.

## Running Only The .EXE
1. Download the `ACCF-StreamDeck_Alert.exe` under the `dist` folder.
2. Enter the computer's IP address into a webhook on Milestone.
3. Run the .exe on the respective computer with Stream Deck connected.
4. OPTIONAL: Activate a rule (Acceptable rule names are below).

## Webhook Rule Names
The rule names that will work with the stream deck are as follows:
1. TEST2: Testing stream deck alarm
2. POI: Person of Interest Alarm
3. LPR: License Plate Recognition Alarm

## Troubleshooting
- Close the ACCF-StreamDeck_Alert.exe window and restart the .exe on the respective computer.
- A log file is saved under the Documents folder for debugging purposes (Named ACCF_StreamDeck.txt).

## Known Bugs
- When restarting the computer with the program open, it will give an error when starting it again when the computer is back on.
* Solution: is to delete the .Lock file under the Documents folder when the computer fully restarts before opening program.
- Seemingly randomly, the streamdeck will stop accepting button presses.
* Solution: Restart program.