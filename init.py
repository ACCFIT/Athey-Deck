# -- Initialization of resources to Stream Deck -- #
# You can find all resources under Athey-Deck/img

from PIL import Image, ImageOps
from StreamDeck.ImageHelpers import PILHelper
import os
import sys
import time

class Icon:
    def __init__(self): 

        self.icon1 = Image.open(resource_path('streamdeck_key1.png'))
        self.icon2 = Image.open(resource_path('streamdeck_key2.png'))
        self.icon3 = Image.open(resource_path('streamdeck_key3.png'))
        self.icon4 = Image.open(resource_path('streamdeck_key4.png'))
        self.icon5 = Image.open(resource_path('streamdeck_key5.png'))
        self.icon6 = Image.open(resource_path('streamdeck_key6.png'))
        self.icon7 = Image.open(resource_path('streamdeck_key7.png'))
        self.icon8 = Image.open(resource_path('streamdeck_key8.png'))
        self.icon9 = Image.open(resource_path('streamdeck_key9.png'))
        self.icon10 = Image.open(resource_path('streamdeck_key10.png'))
        self.icon11 = Image.open(resource_path('streamdeck_key11.png'))
        self.icon12 = Image.open(resource_path('streamdeck_key12.png'))
        self.icon13 = Image.open(resource_path('streamdeck_key13.png'))
        self.icon14 = Image.open(resource_path('streamdeck_key14.png'))
        self.icon15 = Image.open(resource_path('streamdeck_key15.png'))
        self.iconad1 = Image.open(resource_path('streamdeck_ad1.png'))
        self.iconad2 = Image.open(resource_path('streamdeck_ad2.png'))
        self.icon1_alert = Image.open(resource_path('streamdeck_key1-alert.png'))
        self.icon2_alert = Image.open(resource_path('streamdeck_key2-alert.png'))
        self.icon3_alert = Image.open(resource_path('streamdeck_key3-alert.png'))
        self.icon4_alert = Image.open(resource_path('streamdeck_key4-alert.png'))
        self.icon5_alert = Image.open(resource_path('streamdeck_key5-alert.png'))
        self.icon6_alert = Image.open(resource_path('streamdeck_key6-alert.png'))
        self.icon7_alert = Image.open(resource_path('streamdeck_key7-alert.png'))
        self.icon8_alert = Image.open(resource_path('streamdeck_key8-alert.png'))
        self.icon9_alert = Image.open(resource_path('streamdeck_key9-alert.png'))
        self.icon10_alert = Image.open(resource_path('streamdeck_key10-alert.png'))
        self.icon11_alert = Image.open(resource_path('streamdeck_key11-alert.png'))
        self.icon12_alert = Image.open(resource_path('streamdeck_key12-alert.png'))
        self.icon13_alert = Image.open(resource_path('streamdeck_key13-alert.png'))
        self.icon14_alert = Image.open(resource_path('streamdeck_key14-alert.png'))
        self.icon15_alert = Image.open(resource_path('streamdeck_key15-alert.png'))
        self.iconad1_alert = Image.open(resource_path('streamdeck_ad1-alert.png'))
        self.iconad2_alert = Image.open(resource_path('streamdeck_ad2-alert.png'))
        self.test2_alert = Image.open(resource_path('TEST2_Alert.png'))
        self.lpr_alert_yellow = Image.open(resource_path('LPR_Alert-Yellow.png'))
        self.lpr_alert_orange = Image.open(resource_path('LPR_Alert-Orange.png'))
        self.lpr_alert_red = Image.open(resource_path('LPR_Alert-Red.png'))
        self.poi_alert_yellow = Image.open(resource_path('POI_Alert-Yellow.png'))
        self.poi_alert_orange = Image.open(resource_path('POI_Alert-Orange.png'))
        self.poi_alert_red = Image.open(resource_path('POI_Alert-Red.png'))
        self.alert_down = Image.open(resource_path('Alerts-Disabled.png'))
        self.icon1_brett = Image.open(resource_path('streamdeck_key1-brett.png'))
        self.icon2_brett = Image.open(resource_path('streamdeck_key2-brett.png'))
        self.icon3_brett = Image.open(resource_path('streamdeck_key3-brett.png'))
        self.icon4_brett = Image.open(resource_path('streamdeck_key4-brett.png'))
        self.icon5_brett = Image.open(resource_path('streamdeck_key5-brett.png'))
        self.icon6_brett = Image.open(resource_path('streamdeck_key6-brett.png'))
        self.icon7_brett = Image.open(resource_path('streamdeck_key7-brett.png'))
        self.icon8_brett = Image.open(resource_path('streamdeck_key8-brett.png'))
        self.icon9_brett = Image.open(resource_path('streamdeck_key9-brett.png'))
        self.icon10_brett = Image.open(resource_path('streamdeck_key10-brett.png'))
        self.icon11_brett = Image.open(resource_path('streamdeck_key11-brett.png'))
        self.icon12_brett = Image.open(resource_path('streamdeck_key12-brett.png'))
        self.icon13_brett = Image.open(resource_path('streamdeck_key13-brett.png'))
        self.icon14_brett = Image.open(resource_path('streamdeck_key14-brett.png'))
        self.icon15_brett = Image.open(resource_path('streamdeck_key15-brett.png'))
        self.iconad1_brett = Image.open(resource_path('streamdeck_ad1-brett.png'))
        self.iconad2_brett = Image.open(resource_path('streamdeck_ad2-brett.png'))
        self.brett_alert = Image.open(resource_path('Brett-Alert.png'))
        self.alert_button = Image.open(resource_path('alert-button.png'))
        self.alert_button_press = Image.open(resource_path('alert-button-press.png'))
        self.icon1_orange = Image.open(resource_path('streamdeck_key1-orange.png'))
        self.icon2_orange = Image.open(resource_path('streamdeck_key2-orange.png'))
        self.icon3_orange = Image.open(resource_path('streamdeck_key3-orange.png'))
        self.icon4_orange = Image.open(resource_path('streamdeck_key4-orange.png'))
        self.icon5_orange = Image.open(resource_path('streamdeck_key5-orange.png'))
        self.icon6_orange = Image.open(resource_path('streamdeck_key6-orange.png'))
        self.icon7_orange = Image.open(resource_path('streamdeck_key7-orange.png'))
        self.icon8_orange = Image.open(resource_path('streamdeck_key8-orange.png'))
        self.icon9_orange = Image.open(resource_path('streamdeck_key9-orange.png'))
        self.icon10_orange = Image.open(resource_path('streamdeck_key10-orange.png'))
        self.icon11_orange = Image.open(resource_path('streamdeck_key11-orange.png'))
        self.icon12_orange = Image.open(resource_path('streamdeck_key12-orange.png'))
        self.icon13_orange = Image.open(resource_path('streamdeck_key13-orange.png'))
        self.icon14_orange = Image.open(resource_path('streamdeck_key14-orange.png'))
        self.icon15_orange = Image.open(resource_path('streamdeck_key15-orange.png'))
        self.iconad1_orange = Image.open(resource_path('streamdeck_ad1-orange.png'))
        self.iconad2_orange = Image.open(resource_path('streamdeck_ad2-orange.png'))
        self.icon1_yellow = Image.open(resource_path('streamdeck_key1-yellow.png'))
        self.icon2_yellow = Image.open(resource_path('streamdeck_key2-yellow.png'))
        self.icon3_yellow = Image.open(resource_path('streamdeck_key3-yellow.png'))
        self.icon4_yellow = Image.open(resource_path('streamdeck_key4-yellow.png'))
        self.icon5_yellow = Image.open(resource_path('streamdeck_key5-yellow.png'))
        self.icon6_yellow = Image.open(resource_path('streamdeck_key6-yellow.png'))
        self.icon7_yellow = Image.open(resource_path('streamdeck_key7-yellow.png'))
        self.icon8_yellow = Image.open(resource_path('streamdeck_key8-yellow.png'))
        self.icon9_yellow = Image.open(resource_path('streamdeck_key9-yellow.png'))
        self.icon10_yellow = Image.open(resource_path('streamdeck_key10-yellow.png'))
        self.icon11_yellow = Image.open(resource_path('streamdeck_key11-yellow.png'))
        self.icon12_yellow = Image.open(resource_path('streamdeck_key12-yellow.png'))
        self.icon13_yellow = Image.open(resource_path('streamdeck_key13-yellow.png'))
        self.icon14_yellow = Image.open(resource_path('streamdeck_key14-yellow.png'))
        self.icon15_yellow = Image.open(resource_path('streamdeck_key15-yellow.png'))
        self.iconad1_yellow = Image.open(resource_path('streamdeck_ad1-yellow.png'))
        self.iconad2_yellow = Image.open(resource_path('streamdeck_ad2-yellow.png'))
        self.icon1_blue = Image.open(resource_path('streamdeck_key1-blue.png'))
        self.icon2_blue = Image.open(resource_path('streamdeck_key2-blue.png'))
        self.icon3_blue = Image.open(resource_path('streamdeck_key3-blue.png'))
        self.icon4_blue = Image.open(resource_path('streamdeck_key4-blue.png'))
        self.icon5_blue = Image.open(resource_path('streamdeck_key5-blue.png'))
        self.icon6_blue = Image.open(resource_path('streamdeck_key6-blue.png'))
        self.icon7_blue = Image.open(resource_path('streamdeck_key7-blue.png'))
        self.icon8_blue = Image.open(resource_path('streamdeck_key8-blue.png'))
        self.icon9_blue = Image.open(resource_path('streamdeck_key9-blue.png'))
        self.icon10_blue = Image.open(resource_path('streamdeck_key10-blue.png'))
        self.icon11_blue = Image.open(resource_path('streamdeck_key11-blue.png'))
        self.icon12_blue = Image.open(resource_path('streamdeck_key12-blue.png'))
        self.icon13_blue = Image.open(resource_path('streamdeck_key13-blue.png'))
        self.icon14_blue = Image.open(resource_path('streamdeck_key14-blue.png'))
        self.icon15_blue = Image.open(resource_path('streamdeck_key15-blue.png'))
        self.iconad1_blue = Image.open(resource_path('streamdeck_ad1-blue.png'))
        self.iconad2_blue = Image.open(resource_path('streamdeck_ad2-blue.png'))
        self.icon_brett_blank = Image.open(resource_path('streamdeck_brett-blank.png'))
        self.icon_yellow_blank = Image.open(resource_path('streamdeck_yellow-blank.png'))
        self.icon_orange_blank = Image.open(resource_path('streamdeck_orange-blank.png'))
        self.icon_red_blank = Image.open(resource_path('streamdeck_red-blank.png'))
        self.image1 = None
        self.image2 = None
        self.image3 = None
        self.image4 = None
        self.image5 = None
        self.image6 = None
        self.image7 = None
        self.image8 = None
        self.image9 = None
        self.image10 = None
        self.image11 = None
        self.image12 = None
        self.image13 = None
        self.image14 = None
        self.image15 = None
        self.imagead1 = None
        self.imagead2 = None
        self.image1_alert = None
        self.image2_alert = None
        self.image3_alert = None
        self.image4_alert = None
        self.image5_alert = None
        self.image6_alert = None
        self.image7_alert = None
        self.image8_alert = None
        self.image9_alert = None
        self.image10_alert = None
        self.image11_alert = None
        self.image12_alert = None
        self.image13_alert = None
        self.image14_alert = None
        self.image15_alert = None
        self.imagead1_alert = None
        self.imagead2_alert = None
        self.test2_image = None
        self.lpr_image_yellow = None
        self.lpr_image_orange = None
        self.lpr_image_red = None
        self.poi_image_yellow = None
        self.poi_image_orange = None
        self.poi_image_red = None
        self.alert_disable = None
        self.image1_brett = None
        self.image2_brett = None
        self.image3_brett = None
        self.image4_brett = None
        self.image5_brett = None
        self.image6_brett = None
        self.image7_brett = None
        self.image8_brett = None
        self.image9_brett = None
        self.image10_brett = None
        self.image11_brett = None
        self.image12_brett = None
        self.image13_brett = None
        self.image14_brett = None
        self.image15_brett = None
        self.imagead1_brett = None
        self.imagead2_brett = None
        self.brett_image = None
        self.alert_image = None
        self.alert_image_press = None
        self.image1_orange = None
        self.image2_orange = None
        self.image3_orange = None
        self.image4_orange = None
        self.image5_orange = None
        self.image6_orange = None
        self.image7_orange = None
        self.image8_orange = None
        self.image9_orange = None
        self.image10_orange = None
        self.image11_orange = None
        self.image12_orange = None
        self.image13_orange = None
        self.image14_orange = None
        self.image15_orange = None
        self.imagead1_orange = None
        self.imagead2_orange = None
        self.image1_yellow = None
        self.image2_yellow = None
        self.image3_yellow = None
        self.image4_yellow = None
        self.image5_yellow = None
        self.image6_yellow = None
        self.image7_yellow = None
        self.image8_yellow = None
        self.image9_yellow = None
        self.image10_yellow = None
        self.image11_yellow = None
        self.image12_yellow = None
        self.image13_yellow = None
        self.image14_yellow = None
        self.image15_yellow = None
        self.imagead1_yellow = None
        self.imagead2_yellow = None
        self.image1_blue = None
        self.image2_blue = None
        self.image3_blue = None
        self.image4_blue = None
        self.image5_blue = None
        self.image6_blue = None
        self.image7_blue = None
        self.image8_blue = None
        self.image9_blue = None
        self.image10_blue = None
        self.image11_blue = None
        self.image12_blue = None
        self.image13_blue = None
        self.image14_blue = None
        self.image15_blue = None
        self.imagead1_blue = None
        self.imagead2_blue = None
        self.image_brett_blank = None
        self.image_yellow_blank = None
        self.image_orange_blank = None
        self.image_red_blank = None
        
    def image_init(Icon, deck):
        Icon.image1 = PILHelper.create_scaled_key_image(deck, Icon.icon1, margins=[0, 0, 0, 0])
        Icon.image2 = PILHelper.create_scaled_key_image(deck, Icon.icon2, margins=[0, 0, 0, 0])
        Icon.image3 = PILHelper.create_scaled_key_image(deck, Icon.icon3, margins=[0, 0, 0, 0])
        Icon.image4 = PILHelper.create_scaled_key_image(deck, Icon.icon4, margins=[0, 0, 0, 0])
        Icon.image5 = PILHelper.create_scaled_key_image(deck, Icon.icon5, margins=[0, 0, 0, 0])
        Icon.image6 = PILHelper.create_scaled_key_image(deck, Icon.icon6, margins=[0, 0, 0, 0])
        Icon.image7 = PILHelper.create_scaled_key_image(deck, Icon.icon7, margins=[0, 0, 0, 0])
        Icon.image8 = PILHelper.create_scaled_key_image(deck, Icon.icon8, margins=[0, 0, 0, 0])
        Icon.image9 = PILHelper.create_scaled_key_image(deck, Icon.icon9, margins=[0, 0, 0, 0])
        Icon.image10 = PILHelper.create_scaled_key_image(deck, Icon.icon10, margins=[0, 0, 0, 0])
        Icon.image11 = PILHelper.create_scaled_key_image(deck, Icon.icon11, margins=[0, 0, 0, 0])
        Icon.image12 = PILHelper.create_scaled_key_image(deck, Icon.icon12, margins=[0, 0, 0, 0])
        Icon.image13 = PILHelper.create_scaled_key_image(deck, Icon.icon13, margins=[0, 0, 0, 0])
        Icon.image14 = PILHelper.create_scaled_key_image(deck, Icon.icon14, margins=[0, 0, 0, 0])
        Icon.image15 = PILHelper.create_scaled_key_image(deck, Icon.icon15, margins=[0, 0, 0, 0])
        Icon.imagead1 = PILHelper.create_scaled_key_image(deck, Icon.iconad1, margins=[0, 0, 0, 0])
        Icon.imagead2 = PILHelper.create_scaled_key_image(deck, Icon.iconad2, margins=[0, 0, 0, 0])
        Icon.image1_alert = PILHelper.create_scaled_key_image(deck, Icon.icon1_alert, margins=[0, 0, 0, 0])
        Icon.image2_alert = PILHelper.create_scaled_key_image(deck, Icon.icon2_alert, margins=[0, 0, 0, 0])
        Icon.image3_alert = PILHelper.create_scaled_key_image(deck, Icon.icon3_alert, margins=[0, 0, 0, 0])
        Icon.image4_alert = PILHelper.create_scaled_key_image(deck, Icon.icon4_alert, margins=[0, 0, 0, 0])
        Icon.image5_alert = PILHelper.create_scaled_key_image(deck, Icon.icon5_alert, margins=[0, 0, 0, 0])
        Icon.image6_alert = PILHelper.create_scaled_key_image(deck, Icon.icon6_alert, margins=[0, 0, 0, 0])
        Icon.image7_alert = PILHelper.create_scaled_key_image(deck, Icon.icon7_alert, margins=[0, 0, 0, 0])
        Icon.image8_alert = PILHelper.create_scaled_key_image(deck, Icon.icon8_alert, margins=[0, 0, 0, 0])
        Icon.image9_alert = PILHelper.create_scaled_key_image(deck, Icon.icon9_alert, margins=[0, 0, 0, 0])
        Icon.image10_alert = PILHelper.create_scaled_key_image(deck, Icon.icon10_alert, margins=[0, 0, 0, 0])
        Icon.image11_alert = PILHelper.create_scaled_key_image(deck, Icon.icon11_alert, margins=[0, 0, 0, 0])
        Icon.image12_alert = PILHelper.create_scaled_key_image(deck, Icon.icon12_alert, margins=[0, 0, 0, 0])
        Icon.image13_alert = PILHelper.create_scaled_key_image(deck, Icon.icon13_alert, margins=[0, 0, 0, 0])
        Icon.image14_alert = PILHelper.create_scaled_key_image(deck, Icon.icon14_alert, margins=[0, 0, 0, 0])
        Icon.image15_alert = PILHelper.create_scaled_key_image(deck, Icon.icon15_alert, margins=[0, 0, 0, 0])
        Icon.imagead1_alert = PILHelper.create_scaled_key_image(deck, Icon.iconad1_alert, margins=[0, 0, 0, 0])
        Icon.imagead2_alert = PILHelper.create_scaled_key_image(deck, Icon.iconad2_alert, margins=[0, 0, 0, 0])
        Icon.test2_image = PILHelper.create_scaled_key_image(deck, Icon.test2_alert, margins=[0, 0, 0, 0])
        Icon.lpr_image_yellow = PILHelper.create_scaled_key_image(deck, Icon.lpr_alert_yellow, margins=[0, 0, 0, 0])
        Icon.lpr_image_orange = PILHelper.create_scaled_key_image(deck, Icon.lpr_alert_orange, margins=[0, 0, 0, 0])
        Icon.lpr_image_red = PILHelper.create_scaled_key_image(deck, Icon.lpr_alert_red, margins=[0, 0, 0, 0])
        Icon.poi_image_yellow = PILHelper.create_scaled_key_image(deck, Icon.poi_alert_yellow, margins=[0, 0, 0, 0])
        Icon.poi_image_orange = PILHelper.create_scaled_key_image(deck, Icon.poi_alert_orange, margins=[0, 0, 0, 0])
        Icon.poi_image_red = PILHelper.create_scaled_key_image(deck, Icon.poi_alert_red, margins=[0, 0, 0, 0])
        Icon.alert_disabled = PILHelper.create_scaled_key_image(deck, Icon.alert_down, margins=[0, 0, 0, 0])
        Icon.image1_brett = PILHelper.create_scaled_key_image(deck, Icon.icon1_brett, margins=[0, 0, 0, 0])
        Icon.image2_brett = PILHelper.create_scaled_key_image(deck, Icon.icon2_brett, margins=[0, 0, 0, 0])
        Icon.image3_brett = PILHelper.create_scaled_key_image(deck, Icon.icon3_brett, margins=[0, 0, 0, 0])
        Icon.image4_brett = PILHelper.create_scaled_key_image(deck, Icon.icon4_brett, margins=[0, 0, 0, 0])
        Icon.image5_brett = PILHelper.create_scaled_key_image(deck, Icon.icon5_brett, margins=[0, 0, 0, 0])
        Icon.image6_brett = PILHelper.create_scaled_key_image(deck, Icon.icon6_brett, margins=[0, 0, 0, 0])
        Icon.image7_brett = PILHelper.create_scaled_key_image(deck, Icon.icon7_brett, margins=[0, 0, 0, 0])
        Icon.image8_brett = PILHelper.create_scaled_key_image(deck, Icon.icon8_brett, margins=[0, 0, 0, 0])
        Icon.image9_brett = PILHelper.create_scaled_key_image(deck, Icon.icon9_brett, margins=[0, 0, 0, 0])
        Icon.image10_brett = PILHelper.create_scaled_key_image(deck, Icon.icon10_brett, margins=[0, 0, 0, 0])
        Icon.image11_brett = PILHelper.create_scaled_key_image(deck, Icon.icon11_brett, margins=[0, 0, 0, 0])
        Icon.image12_brett = PILHelper.create_scaled_key_image(deck, Icon.icon12_brett, margins=[0, 0, 0, 0])
        Icon.image13_brett = PILHelper.create_scaled_key_image(deck, Icon.icon13_brett, margins=[0, 0, 0, 0])
        Icon.image14_brett = PILHelper.create_scaled_key_image(deck, Icon.icon14_brett, margins=[0, 0, 0, 0])
        Icon.image15_brett = PILHelper.create_scaled_key_image(deck, Icon.icon15_brett, margins=[0, 0, 0, 0])
        Icon.imagead1_brett = PILHelper.create_scaled_key_image(deck, Icon.iconad1_brett, margins=[0, 0, 0, 0])
        Icon.imagead2_brett = PILHelper.create_scaled_key_image(deck, Icon.iconad2_brett, margins=[0, 0, 0, 0])
        Icon.brett_image = PILHelper.create_scaled_key_image(deck, Icon.brett_alert, margins=[0, 0, 0, 0])
        Icon.alert_image = PILHelper.create_scaled_key_image(deck, Icon.alert_button, margins=[0, 0, 0, 0])
        Icon.alert_image_press = PILHelper.create_scaled_key_image(deck, Icon.alert_button_press, margins=[0, 0, 0, 0])
        Icon.image1_orange = PILHelper.create_scaled_key_image(deck, Icon.icon1_orange, margins=[0, 0, 0, 0])
        Icon.image2_orange = PILHelper.create_scaled_key_image(deck, Icon.icon2_orange, margins=[0, 0, 0, 0])
        Icon.image3_orange = PILHelper.create_scaled_key_image(deck, Icon.icon3_orange, margins=[0, 0, 0, 0])
        Icon.image4_orange = PILHelper.create_scaled_key_image(deck, Icon.icon4_orange, margins=[0, 0, 0, 0])
        Icon.image5_orange = PILHelper.create_scaled_key_image(deck, Icon.icon5_orange, margins=[0, 0, 0, 0])
        Icon.image6_orange = PILHelper.create_scaled_key_image(deck, Icon.icon6_orange, margins=[0, 0, 0, 0])
        Icon.image7_orange = PILHelper.create_scaled_key_image(deck, Icon.icon7_orange, margins=[0, 0, 0, 0])
        Icon.image8_orange = PILHelper.create_scaled_key_image(deck, Icon.icon8_orange, margins=[0, 0, 0, 0])
        Icon.image9_orange = PILHelper.create_scaled_key_image(deck, Icon.icon9_orange, margins=[0, 0, 0, 0])
        Icon.image10_orange = PILHelper.create_scaled_key_image(deck, Icon.icon10_orange, margins=[0, 0, 0, 0])
        Icon.image11_orange = PILHelper.create_scaled_key_image(deck, Icon.icon11_orange, margins=[0, 0, 0, 0])
        Icon.image12_orange = PILHelper.create_scaled_key_image(deck, Icon.icon12_orange, margins=[0, 0, 0, 0])
        Icon.image13_orange = PILHelper.create_scaled_key_image(deck, Icon.icon13_orange, margins=[0, 0, 0, 0])
        Icon.image14_orange = PILHelper.create_scaled_key_image(deck, Icon.icon14_orange, margins=[0, 0, 0, 0])
        Icon.image15_orange = PILHelper.create_scaled_key_image(deck, Icon.icon15_orange, margins=[0, 0, 0, 0])
        Icon.imagead1_orange = PILHelper.create_scaled_key_image(deck, Icon.iconad1_orange, margins=[0, 0, 0, 0])
        Icon.imagead2_orange = PILHelper.create_scaled_key_image(deck, Icon.iconad2_orange, margins=[0, 0, 0, 0])
        Icon.image1_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon1_yellow, margins=[0, 0, 0, 0])
        Icon.image2_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon2_yellow, margins=[0, 0, 0, 0])
        Icon.image3_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon3_yellow, margins=[0, 0, 0, 0])
        Icon.image4_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon4_yellow, margins=[0, 0, 0, 0])
        Icon.image5_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon5_yellow, margins=[0, 0, 0, 0])
        Icon.image6_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon6_yellow, margins=[0, 0, 0, 0])
        Icon.image7_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon7_yellow, margins=[0, 0, 0, 0])
        Icon.image8_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon8_yellow, margins=[0, 0, 0, 0])
        Icon.image9_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon9_yellow, margins=[0, 0, 0, 0])
        Icon.image10_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon10_yellow, margins=[0, 0, 0, 0])
        Icon.image11_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon11_yellow, margins=[0, 0, 0, 0])
        Icon.image12_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon12_yellow, margins=[0, 0, 0, 0])
        Icon.image13_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon13_yellow, margins=[0, 0, 0, 0])
        Icon.image14_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon14_yellow, margins=[0, 0, 0, 0])
        Icon.image15_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon15_yellow, margins=[0, 0, 0, 0])
        Icon.imagead1_yellow = PILHelper.create_scaled_key_image(deck, Icon.iconad1_yellow, margins=[0, 0, 0, 0])
        Icon.imagead2_yellow = PILHelper.create_scaled_key_image(deck, Icon.iconad2_yellow, margins=[0, 0, 0, 0])
        Icon.image1_blue = PILHelper.create_scaled_key_image(deck, Icon.icon1_blue, margins=[0, 0, 0, 0])
        Icon.image2_blue = PILHelper.create_scaled_key_image(deck, Icon.icon2_blue, margins=[0, 0, 0, 0])
        Icon.image3_blue = PILHelper.create_scaled_key_image(deck, Icon.icon3_blue, margins=[0, 0, 0, 0])
        Icon.image4_blue = PILHelper.create_scaled_key_image(deck, Icon.icon4_blue, margins=[0, 0, 0, 0])
        Icon.image5_blue = PILHelper.create_scaled_key_image(deck, Icon.icon5_blue, margins=[0, 0, 0, 0])
        Icon.image6_blue = PILHelper.create_scaled_key_image(deck, Icon.icon6_blue, margins=[0, 0, 0, 0])
        Icon.image7_blue = PILHelper.create_scaled_key_image(deck, Icon.icon7_blue, margins=[0, 0, 0, 0])
        Icon.image8_blue = PILHelper.create_scaled_key_image(deck, Icon.icon8_blue, margins=[0, 0, 0, 0])
        Icon.image9_blue = PILHelper.create_scaled_key_image(deck, Icon.icon9_blue, margins=[0, 0, 0, 0])
        Icon.image10_blue = PILHelper.create_scaled_key_image(deck, Icon.icon10_blue, margins=[0, 0, 0, 0])
        Icon.image11_blue = PILHelper.create_scaled_key_image(deck, Icon.icon11_blue, margins=[0, 0, 0, 0])
        Icon.image12_blue = PILHelper.create_scaled_key_image(deck, Icon.icon12_blue, margins=[0, 0, 0, 0])
        Icon.image13_blue = PILHelper.create_scaled_key_image(deck, Icon.icon13_blue, margins=[0, 0, 0, 0])
        Icon.image14_blue = PILHelper.create_scaled_key_image(deck, Icon.icon14_blue, margins=[0, 0, 0, 0])
        Icon.image15_blue = PILHelper.create_scaled_key_image(deck, Icon.icon15_blue, margins=[0, 0, 0, 0])
        Icon.imagead1_blue = PILHelper.create_scaled_key_image(deck, Icon.iconad1_blue, margins=[0, 0, 0, 0])
        Icon.imagead2_blue = PILHelper.create_scaled_key_image(deck, Icon.iconad2_blue, margins=[0, 0, 0, 0])
        Icon.image_brett_blank = PILHelper.create_scaled_key_image(deck, Icon.icon_brett_blank, margins=[0, 0, 0, 0])
        Icon.image_yellow_blank = PILHelper.create_scaled_key_image(deck, Icon.icon_yellow_blank, margins=[0, 0, 0, 0])
        Icon.image_orange_blank = PILHelper.create_scaled_key_image(deck, Icon.icon_orange_blank, margins=[0, 0, 0, 0])
        Icon.image_red_blank = PILHelper.create_scaled_key_image(deck, Icon.icon_red_blank, margins=[0, 0, 0, 0])
        

def set_keys_normal(Icon, deck):
        time.sleep(0.05)
        deck.set_key_image(0, PILHelper.to_native_key_format(deck, Icon.image1)) #SET TO NORMAL
        deck.set_key_image(1, PILHelper.to_native_key_format(deck, Icon.image2))
        deck.set_key_image(2, PILHelper.to_native_key_format(deck, Icon.image3))
        deck.set_key_image(3, PILHelper.to_native_key_format(deck, Icon.image4))
        deck.set_key_image(4, PILHelper.to_native_key_format(deck, Icon.image5))
        deck.set_key_image(5, PILHelper.to_native_key_format(deck, Icon.image6))
        deck.set_key_image(6, PILHelper.to_native_key_format(deck, Icon.image7))
        deck.set_key_image(7, PILHelper.to_native_key_format(deck, Icon.alert_image))
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.image8))
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.image9))
        deck.set_key_image(10, PILHelper.to_native_key_format(deck, Icon.image10))
        deck.set_key_image(11, PILHelper.to_native_key_format(deck, Icon.image11))
        deck.set_key_image(12, PILHelper.to_native_key_format(deck, Icon.image12))
        deck.set_key_image(13, PILHelper.to_native_key_format(deck, Icon.image13))
        deck.set_key_image(14, PILHelper.to_native_key_format(deck, Icon.image14))
        
def set_yellow_alarm(Icon, deck):
        deck.set_key_image(2, PILHelper.to_native_key_format(deck, Icon.image3_yellow))
        time.sleep(0.04)
        deck.set_key_image(3, PILHelper.to_native_key_format(deck, Icon.image4_yellow))
        time.sleep(0.04)
        deck.set_key_image(2, PILHelper.to_native_key_format(deck, Icon.image3))
        deck.set_key_image(4, PILHelper.to_native_key_format(deck, Icon.image5_yellow))
        time.sleep(0.04)
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.image8_yellow))
        time.sleep(0.04)
        deck.set_key_image(3, PILHelper.to_native_key_format(deck, Icon.image4))
        time.sleep(0.04)
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.image9_yellow))
        time.sleep(0.04)
        deck.set_key_image(4, PILHelper.to_native_key_format(deck, Icon.image5))
        time.sleep(0.04)
        deck.set_key_image(14, PILHelper.to_native_key_format(deck, Icon.image_yellow_blank))
        time.sleep(0.04)
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.image9))
        time.sleep(0.04)
        deck.set_key_image(13, PILHelper.to_native_key_format(deck, Icon.image_yellow_blank))
        time.sleep(0.04)
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.image8))
        time.sleep(0.04)
        deck.set_key_image(14, None)
        deck.set_key_image(12, PILHelper.to_native_key_format(deck, Icon.image_yellow_blank))
        time.sleep(0.04)
        deck.set_key_image(13, None)
        time.sleep(0.04)
        deck.set_key_image(11, PILHelper.to_native_key_format(deck, Icon.image_yellow_blank))
        time.sleep(0.04)
        deck.set_key_image(12, None)
        deck.set_key_image(10, PILHelper.to_native_key_format(deck, Icon.image_yellow_blank))
        time.sleep(0.04)
        deck.set_key_image(6, PILHelper.to_native_key_format(deck, Icon.image7_yellow))
        time.sleep(0.04)
        deck.set_key_image(11, None)
        time.sleep(0.04)
        deck.set_key_image(5, PILHelper.to_native_key_format(deck, Icon.image6_yellow))
        time.sleep(0.04)
        deck.set_key_image(10, None)
        time.sleep(0.04)
        deck.set_key_image(0, PILHelper.to_native_key_format(deck, Icon.image1_yellow))
        time.sleep(0.04)
        deck.set_key_image(5, PILHelper.to_native_key_format(deck, Icon.image6))
        time.sleep(0.04)
        deck.set_key_image(1, PILHelper.to_native_key_format(deck, Icon.image2_yellow))
        time.sleep(0.04)
        deck.set_key_image(6, PILHelper.to_native_key_format(deck, Icon.image7))
        time.sleep(0.04)
        deck.set_key_image(0, PILHelper.to_native_key_format(deck, Icon.image1))
        deck.set_key_image(2, PILHelper.to_native_key_format(deck, Icon.image3_yellow))
        time.sleep(0.04)
        deck.set_key_image(1, PILHelper.to_native_key_format(deck, Icon.image2))

def set_orange_alarm(Icon, deck):
        deck.set_key_image(2, PILHelper.to_native_key_format(deck, Icon.image3_orange))
        time.sleep(0.04)
        deck.set_key_image(3, PILHelper.to_native_key_format(deck, Icon.image4_orange))
        time.sleep(0.04)
        deck.set_key_image(2, PILHelper.to_native_key_format(deck, Icon.image3))
        deck.set_key_image(4, PILHelper.to_native_key_format(deck, Icon.image5_orange))
        time.sleep(0.04)
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.image8_orange))
        time.sleep(0.04)
        deck.set_key_image(3, PILHelper.to_native_key_format(deck, Icon.image4))
        time.sleep(0.04)
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.image9_orange))
        time.sleep(0.04)
        deck.set_key_image(4, PILHelper.to_native_key_format(deck, Icon.image5))
        time.sleep(0.04)
        deck.set_key_image(14, PILHelper.to_native_key_format(deck, Icon.image_orange_blank))
        time.sleep(0.04)
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.image9))
        time.sleep(0.04)
        deck.set_key_image(13, PILHelper.to_native_key_format(deck, Icon.image_orange_blank))
        time.sleep(0.04)
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.image8))
        time.sleep(0.04)
        deck.set_key_image(14, None)
        deck.set_key_image(12, PILHelper.to_native_key_format(deck, Icon.image_orange_blank))
        time.sleep(0.04)
        deck.set_key_image(13, None)
        time.sleep(0.04)
        deck.set_key_image(11, PILHelper.to_native_key_format(deck, Icon.image_orange_blank))
        time.sleep(0.04)
        deck.set_key_image(12, None)
        deck.set_key_image(10, PILHelper.to_native_key_format(deck, Icon.image_orange_blank))
        time.sleep(0.04)
        deck.set_key_image(6, PILHelper.to_native_key_format(deck, Icon.image7_orange))
        time.sleep(0.04)
        deck.set_key_image(11, None)
        time.sleep(0.04)
        deck.set_key_image(5, PILHelper.to_native_key_format(deck, Icon.image6_orange))
        time.sleep(0.04)
        deck.set_key_image(10, None)
        time.sleep(0.04)
        deck.set_key_image(0, PILHelper.to_native_key_format(deck, Icon.image1_orange))
        time.sleep(0.04)
        deck.set_key_image(5, PILHelper.to_native_key_format(deck, Icon.image6))
        time.sleep(0.04)
        deck.set_key_image(1, PILHelper.to_native_key_format(deck, Icon.image2_orange))
        time.sleep(0.04)
        deck.set_key_image(6, PILHelper.to_native_key_format(deck, Icon.image7))
        time.sleep(0.04)
        deck.set_key_image(0, PILHelper.to_native_key_format(deck, Icon.image1))
        deck.set_key_image(2, PILHelper.to_native_key_format(deck, Icon.image3_orange))
        time.sleep(0.04)
        deck.set_key_image(1, PILHelper.to_native_key_format(deck, Icon.image2))

def set_red_alarm(Icon, deck):
        deck.set_key_image(2, PILHelper.to_native_key_format(deck, Icon.image3_alert))
        time.sleep(0.04)
        deck.set_key_image(3, PILHelper.to_native_key_format(deck, Icon.image4_alert))
        time.sleep(0.04)
        deck.set_key_image(2, PILHelper.to_native_key_format(deck, Icon.image3))
        deck.set_key_image(4, PILHelper.to_native_key_format(deck, Icon.image5_alert))
        time.sleep(0.04)
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.image8_alert))
        time.sleep(0.04)
        deck.set_key_image(3, PILHelper.to_native_key_format(deck, Icon.image4))
        time.sleep(0.04)
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.image9_alert))
        time.sleep(0.04)
        deck.set_key_image(4, PILHelper.to_native_key_format(deck, Icon.image5))
        time.sleep(0.04)
        deck.set_key_image(14, PILHelper.to_native_key_format(deck, Icon.image_red_blank))
        time.sleep(0.04)
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.image9))
        time.sleep(0.04)
        deck.set_key_image(13, PILHelper.to_native_key_format(deck, Icon.image_red_blank))
        time.sleep(0.04)
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.image8))
        time.sleep(0.04)
        deck.set_key_image(14, None)
        deck.set_key_image(12, PILHelper.to_native_key_format(deck, Icon.image_red_blank))
        time.sleep(0.04)
        deck.set_key_image(13, None)
        time.sleep(0.04)
        deck.set_key_image(11, PILHelper.to_native_key_format(deck, Icon.image_red_blank))
        time.sleep(0.04)
        deck.set_key_image(12, None)
        deck.set_key_image(10, PILHelper.to_native_key_format(deck, Icon.image_red_blank))
        time.sleep(0.04)
        deck.set_key_image(6, PILHelper.to_native_key_format(deck, Icon.image7_alert))
        time.sleep(0.04)
        deck.set_key_image(11, None)
        time.sleep(0.04)
        deck.set_key_image(5, PILHelper.to_native_key_format(deck, Icon.image6_alert))
        time.sleep(0.04)
        deck.set_key_image(10, None)
        time.sleep(0.04)
        deck.set_key_image(0, PILHelper.to_native_key_format(deck, Icon.image1_alert))
        time.sleep(0.04)
        deck.set_key_image(5, PILHelper.to_native_key_format(deck, Icon.image6))
        time.sleep(0.04)
        deck.set_key_image(1, PILHelper.to_native_key_format(deck, Icon.image2_alert))
        time.sleep(0.04)
        deck.set_key_image(6, PILHelper.to_native_key_format(deck, Icon.image7))
        time.sleep(0.04)
        deck.set_key_image(0, PILHelper.to_native_key_format(deck, Icon.image1))
        deck.set_key_image(2, PILHelper.to_native_key_format(deck, Icon.image3_alert))
        time.sleep(0.04)
        deck.set_key_image(1, PILHelper.to_native_key_format(deck, Icon.image2))

def set_brett_keys(Icon, deck):
        time.sleep(0.05)
        deck.set_key_image(0, PILHelper.to_native_key_format(deck, Icon.image1_brett)) #SET TO NORMAL
        deck.set_key_image(1, PILHelper.to_native_key_format(deck, Icon.image2_brett))
        deck.set_key_image(2, PILHelper.to_native_key_format(deck, Icon.image3_brett))
        deck.set_key_image(3, PILHelper.to_native_key_format(deck, Icon.image4_brett))
        deck.set_key_image(4, PILHelper.to_native_key_format(deck, Icon.image5_brett))
        deck.set_key_image(5, PILHelper.to_native_key_format(deck, Icon.image6_brett))
        deck.set_key_image(6, PILHelper.to_native_key_format(deck, Icon.image7_brett))
        deck.set_key_image(7, PILHelper.to_native_key_format(deck, Icon.brett_image))
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.image8_brett))
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.image9_brett))
        deck.set_key_image(10, PILHelper.to_native_key_format(deck, Icon.image10_brett))
        deck.set_key_image(11, PILHelper.to_native_key_format(deck, Icon.image11_brett))
        deck.set_key_image(12, PILHelper.to_native_key_format(deck, Icon.image12_brett))
        deck.set_key_image(13, PILHelper.to_native_key_format(deck, Icon.image13_brett))
        deck.set_key_image(14, PILHelper.to_native_key_format(deck, Icon.image14_brett))
        time.sleep(1)
    

def key_press_get(Icon, deck, num):
        if num == 0:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image1_blue))
        elif num == 1:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image2_blue))
        elif num == 2:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image3_blue))
        elif num == 3:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image4_blue))
        elif num == 4:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image5_blue))
        elif num == 5:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image6_blue))
        elif num == 6:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image7_blue))
        elif num == 7:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.alert_image_press))
        elif num == 8:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image8_blue))
        elif num == 9:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image9_blue))
        elif num == 10:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image10_blue))
        elif num == 11:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image11_blue))
        elif num == 12:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image12_blue))
        elif num == 13:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image13_blue))
        elif num == 14:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image14_blue))

def key_press_normal(Icon, deck, num):
        if num == 0:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image1))
        elif num == 1:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image2))
        elif num == 2:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image3))
        elif num == 3:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image4))
        elif num == 4:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image5))
        elif num == 5:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image6))
        elif num == 6:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image7))
        elif num == 7:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.alert_image))
        elif num == 8:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image8))
        elif num == 9:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image9))
        elif num == 10:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image10))
        elif num == 11:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image11))
        elif num == 12:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image12))
        elif num == 13:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image13))
        elif num == 14:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.image14))

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".") #Use "img/" for terminal testing. Use "." for release version.

    return os.path.join(base_path, relative_path)