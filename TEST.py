## -- THIS IS A TEST FILE DO NOT USE -- ##

import sys
from gui import LicensePlateManager
from PyQt5.QtWidgets import QApplication
import re

data_str = '281PQF'

if __name__ == '__main__':
    with open("license_plates.txt", "r") as file:
        for line in file:
            plate_id, plate_pattern, severity = line.strip().split(",", 2)
            if bool(re.search(plate_pattern, data_str)):
                if 'GREEN' in severity:
                    print("GREEN")
                    #logging.info("BRETT ARRIVAL/DEPARTURE")
                    #brett.set()
                elif 'YELLOW' in severity:
                    print("YELLOW")
                    #logging.info("LPR YELLOW ALERT")
                    #lpr_yellow.set()
                elif 'ORANGE' in severity:
                    print("ORANGE")
                    #logging.info("LPR ORANGE ALERT")
                    #lpr_orange.set()
                elif 'RED' in severity:
                    print("RED")
                    #logging.info("LPR RED ALERT")
                    #lpr_red.set()