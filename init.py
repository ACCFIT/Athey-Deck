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
        self.iconad1 = Image.open(resource_path('streamdeck_ad1.png'))
        self.iconad2 = Image.open(resource_path('streamdeck_ad2.png'))
        self.icon1_alert = Image.open(resource_path('streamdeck_key1-alert.png'))
        self.icon2_alert = Image.open(resource_path('streamdeck_key2-alert.png'))
        self.icon3_alert = Image.open(resource_path('streamdeck_key3-alert.png'))
        self.icon4_alert = Image.open(resource_path('streamdeck_key4-alert.png'))
        self.icon5_alert = Image.open(resource_path('streamdeck_key5-alert.png'))
        self.icon6_alert = Image.open(resource_path('streamdeck_key6-alert.png'))
        self.icon7_alert = Image.open(resource_path('streamdeck_key7-alert.png'))
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
        self.iconad1_brett = Image.open(resource_path('streamdeck_ad1-brett.png'))
        self.iconad2_brett = Image.open(resource_path('streamdeck_ad2-brett.png'))
        self.brett_alert = Image.open(resource_path('Brett-Alert.png'))
        self.bean_alert = Image.open(resource_path('tom_hanks_2.png'))
        self.alert_button = Image.open(resource_path('alert-button.png'))
        self.alert_button_press = Image.open(resource_path('alert-button-press.png'))
        self.icon1_orange = Image.open(resource_path('streamdeck_key1-orange.png'))
        self.icon2_orange = Image.open(resource_path('streamdeck_key2-orange.png'))
        self.icon3_orange = Image.open(resource_path('streamdeck_key3-orange.png'))
        self.icon4_orange = Image.open(resource_path('streamdeck_key4-orange.png'))
        self.icon5_orange = Image.open(resource_path('streamdeck_key5-orange.png'))
        self.icon6_orange = Image.open(resource_path('streamdeck_key6-orange.png'))
        self.icon7_orange = Image.open(resource_path('streamdeck_key7-orange.png'))
        self.iconad1_orange = Image.open(resource_path('streamdeck_ad1-orange.png'))
        self.iconad2_orange = Image.open(resource_path('streamdeck_ad2-orange.png'))
        self.icon1_yellow = Image.open(resource_path('streamdeck_key1-yellow.png'))
        self.icon2_yellow = Image.open(resource_path('streamdeck_key2-yellow.png'))
        self.icon3_yellow = Image.open(resource_path('streamdeck_key3-yellow.png'))
        self.icon4_yellow = Image.open(resource_path('streamdeck_key4-yellow.png'))
        self.icon5_yellow = Image.open(resource_path('streamdeck_key5-yellow.png'))
        self.icon6_yellow = Image.open(resource_path('streamdeck_key6-yellow.png'))
        self.icon7_yellow = Image.open(resource_path('streamdeck_key7-yellow.png'))
        self.iconad1_yellow = Image.open(resource_path('streamdeck_ad1-yellow.png'))
        self.iconad2_yellow = Image.open(resource_path('streamdeck_ad2-yellow.png'))
        self.icon1_blue = Image.open(resource_path('streamdeck_key1-blue.png'))
        self.icon2_blue = Image.open(resource_path('streamdeck_key2-blue.png'))
        self.icon3_blue = Image.open(resource_path('streamdeck_key3-blue.png'))
        self.icon4_blue = Image.open(resource_path('streamdeck_key4-blue.png'))
        self.icon5_blue = Image.open(resource_path('streamdeck_key5-blue.png'))
        self.icon6_blue = Image.open(resource_path('streamdeck_key6-blue.png'))
        self.icon7_blue = Image.open(resource_path('streamdeck_key7-blue.png'))
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
        self.imagead1 = None
        self.imagead2 = None
        self.image1_alert = None
        self.image2_alert = None
        self.image3_alert = None
        self.image4_alert = None
        self.image5_alert = None
        self.image6_alert = None
        self.image7_alert = None
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
        self.imagead1_brett = None
        self.imagead2_brett = None
        self.brett_image = None
        self.bean_image = None
        self.alert_image = None
        self.alert_image_press = None
        self.image1_orange = None
        self.image2_orange = None
        self.image3_orange = None
        self.image4_orange = None
        self.image5_orange = None
        self.image6_orange = None
        self.image7_orange = None
        self.imagead1_orange = None
        self.imagead2_orange = None
        self.image1_yellow = None
        self.image2_yellow = None
        self.image3_yellow = None
        self.image4_yellow = None
        self.image5_yellow = None
        self.image6_yellow = None
        self.image7_yellow = None
        self.imagead1_yellow = None
        self.imagead2_yellow = None
        self.image1_blue = None
        self.image2_blue = None
        self.image3_blue = None
        self.image4_blue = None
        self.image5_blue = None
        self.image6_blue = None
        self.image7_blue = None
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
        Icon.imagead1 = PILHelper.create_scaled_key_image(deck, Icon.iconad1, margins=[0, 0, 0, 0])
        Icon.imagead2 = PILHelper.create_scaled_key_image(deck, Icon.iconad2, margins=[0, 0, 0, 0])
        Icon.image1_alert = PILHelper.create_scaled_key_image(deck, Icon.icon1_alert, margins=[0, 0, 0, 0])
        Icon.image2_alert = PILHelper.create_scaled_key_image(deck, Icon.icon2_alert, margins=[0, 0, 0, 0])
        Icon.image3_alert = PILHelper.create_scaled_key_image(deck, Icon.icon3_alert, margins=[0, 0, 0, 0])
        Icon.image4_alert = PILHelper.create_scaled_key_image(deck, Icon.icon4_alert, margins=[0, 0, 0, 0])
        Icon.image5_alert = PILHelper.create_scaled_key_image(deck, Icon.icon5_alert, margins=[0, 0, 0, 0])
        Icon.image6_alert = PILHelper.create_scaled_key_image(deck, Icon.icon6_alert, margins=[0, 0, 0, 0])
        Icon.image7_alert = PILHelper.create_scaled_key_image(deck, Icon.icon7_alert, margins=[0, 0, 0, 0])
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
        Icon.imagead1_brett = PILHelper.create_scaled_key_image(deck, Icon.iconad1_brett, margins=[0, 0, 0, 0])
        Icon.imagead2_brett = PILHelper.create_scaled_key_image(deck, Icon.iconad2_brett, margins=[0, 0, 0, 0])
        Icon.brett_image = PILHelper.create_scaled_key_image(deck, Icon.brett_alert, margins=[0, 0, 0, 0])
        Icon.bean_image = PILHelper.create_scaled_key_image(deck, Icon.bean_alert, margins=[0, 0, 0, 0])
        Icon.alert_image = PILHelper.create_scaled_key_image(deck, Icon.alert_button, margins=[0, 0, 0, 0])
        Icon.alert_image_press = PILHelper.create_scaled_key_image(deck, Icon.alert_button_press, margins=[0, 0, 0, 0])
        Icon.image1_orange = PILHelper.create_scaled_key_image(deck, Icon.icon1_orange, margins=[0, 0, 0, 0])
        Icon.image2_orange = PILHelper.create_scaled_key_image(deck, Icon.icon2_orange, margins=[0, 0, 0, 0])
        Icon.image3_orange = PILHelper.create_scaled_key_image(deck, Icon.icon3_orange, margins=[0, 0, 0, 0])
        Icon.image4_orange = PILHelper.create_scaled_key_image(deck, Icon.icon4_orange, margins=[0, 0, 0, 0])
        Icon.image5_orange = PILHelper.create_scaled_key_image(deck, Icon.icon5_orange, margins=[0, 0, 0, 0])
        Icon.image6_orange = PILHelper.create_scaled_key_image(deck, Icon.icon6_orange, margins=[0, 0, 0, 0])
        Icon.image7_orange = PILHelper.create_scaled_key_image(deck, Icon.icon7_orange, margins=[0, 0, 0, 0])
        Icon.imagead1_orange = PILHelper.create_scaled_key_image(deck, Icon.iconad1_orange, margins=[0, 0, 0, 0])
        Icon.imagead2_orange = PILHelper.create_scaled_key_image(deck, Icon.iconad2_orange, margins=[0, 0, 0, 0])
        Icon.image1_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon1_yellow, margins=[0, 0, 0, 0])
        Icon.image2_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon2_yellow, margins=[0, 0, 0, 0])
        Icon.image3_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon3_yellow, margins=[0, 0, 0, 0])
        Icon.image4_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon4_yellow, margins=[0, 0, 0, 0])
        Icon.image5_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon5_yellow, margins=[0, 0, 0, 0])
        Icon.image6_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon6_yellow, margins=[0, 0, 0, 0])
        Icon.image7_yellow = PILHelper.create_scaled_key_image(deck, Icon.icon7_yellow, margins=[0, 0, 0, 0])
        Icon.imagead1_yellow = PILHelper.create_scaled_key_image(deck, Icon.iconad1_yellow, margins=[0, 0, 0, 0])
        Icon.imagead2_yellow = PILHelper.create_scaled_key_image(deck, Icon.iconad2_yellow, margins=[0, 0, 0, 0])
        Icon.image1_blue = PILHelper.create_scaled_key_image(deck, Icon.icon1_blue, margins=[0, 0, 0, 0])
        Icon.image2_blue = PILHelper.create_scaled_key_image(deck, Icon.icon2_blue, margins=[0, 0, 0, 0])
        Icon.image3_blue = PILHelper.create_scaled_key_image(deck, Icon.icon3_blue, margins=[0, 0, 0, 0])
        Icon.image4_blue = PILHelper.create_scaled_key_image(deck, Icon.icon4_blue, margins=[0, 0, 0, 0])
        Icon.image5_blue = PILHelper.create_scaled_key_image(deck, Icon.icon5_blue, margins=[0, 0, 0, 0])
        Icon.image6_blue = PILHelper.create_scaled_key_image(deck, Icon.icon6_blue, margins=[0, 0, 0, 0])
        Icon.image7_blue = PILHelper.create_scaled_key_image(deck, Icon.icon7_blue, margins=[0, 0, 0, 0])
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
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.imagead1))
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.imagead2))
        deck.set_key_image(10, None)
        deck.set_key_image(11, None)
        deck.set_key_image(12, None)
        deck.set_key_image(13, None)
        deck.set_key_image(14, None)
        
    def set_yellow_alarm(Icon, deck):
        deck.set_key_image(2, PILHelper.to_native_key_format(deck, Icon.image3_yellow))
        time.sleep(0.04)
        deck.set_key_image(3, PILHelper.to_native_key_format(deck, Icon.image4_yellow))
        time.sleep(0.04)
        deck.set_key_image(2, PILHelper.to_native_key_format(deck, Icon.image3))
        deck.set_key_image(4, PILHelper.to_native_key_format(deck, Icon.image5_yellow))
        time.sleep(0.04)
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.imagead1_yellow))
        time.sleep(0.04)
        deck.set_key_image(3, PILHelper.to_native_key_format(deck, Icon.image4))
        time.sleep(0.04)
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.imagead2_yellow))
        time.sleep(0.04)
        deck.set_key_image(4, PILHelper.to_native_key_format(deck, Icon.image5))
        time.sleep(0.04)
        deck.set_key_image(14, PILHelper.to_native_key_format(deck, Icon.image_yellow_blank))
        time.sleep(0.04)
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.imagead2))
        time.sleep(0.04)
        deck.set_key_image(13, PILHelper.to_native_key_format(deck, Icon.image_yellow_blank))
        time.sleep(0.04)
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.imagead1))
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
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.imagead1_orange))
        time.sleep(0.04)
        deck.set_key_image(3, PILHelper.to_native_key_format(deck, Icon.image4))
        time.sleep(0.04)
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.imagead2_orange))
        time.sleep(0.04)
        deck.set_key_image(4, PILHelper.to_native_key_format(deck, Icon.image5))
        time.sleep(0.04)
        deck.set_key_image(14, PILHelper.to_native_key_format(deck, Icon.image_orange_blank))
        time.sleep(0.04)
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.imagead2))
        time.sleep(0.04)
        deck.set_key_image(13, PILHelper.to_native_key_format(deck, Icon.image_orange_blank))
        time.sleep(0.04)
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.imagead1))
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
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.imagead1_alert))
        time.sleep(0.04)
        deck.set_key_image(3, PILHelper.to_native_key_format(deck, Icon.image4))
        time.sleep(0.04)
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.imagead2_alert))
        time.sleep(0.04)
        deck.set_key_image(4, PILHelper.to_native_key_format(deck, Icon.image5))
        time.sleep(0.04)
        deck.set_key_image(14, PILHelper.to_native_key_format(deck, Icon.image_red_blank))
        time.sleep(0.04)
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.imagead2))
        time.sleep(0.04)
        deck.set_key_image(13, PILHelper.to_native_key_format(deck, Icon.image_red_blank))
        time.sleep(0.04)
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.imagead1))
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
        deck.set_key_image(8, PILHelper.to_native_key_format(deck, Icon.imagead1_brett))
        deck.set_key_image(9, PILHelper.to_native_key_format(deck, Icon.imagead2_brett))
        deck.set_key_image(10, PILHelper.to_native_key_format(deck, Icon.image_brett_blank))
        deck.set_key_image(11, PILHelper.to_native_key_format(deck, Icon.image_brett_blank))
        deck.set_key_image(12, PILHelper.to_native_key_format(deck, Icon.image_brett_blank))
        deck.set_key_image(13, PILHelper.to_native_key_format(deck, Icon.image_brett_blank))
        deck.set_key_image(14, PILHelper.to_native_key_format(deck, Icon.image_brett_blank))
        time.sleep(1)

    def set_bean_keys(Icon, deck):
        time.sleep(0.05)
        deck.set_key_image(0, PILHelper.to_native_key_format(deck, Icon.bean_image))
        deck.set_key_image(1, PILHelper.to_native_key_format(deck, Icon.bean_image))
        deck.set_key_image(2, PILHelper.to_native_key_format(deck, Icon.bean_image))
        deck.set_key_image(3, PILHelper.to_native_key_format(deck, Icon.bean_image))
        deck.set_key_image(4, PILHelper.to_native_key_format(deck, Icon.bean_image))
        deck.set_key_image(5, PILHelper.to_native_key_format(deck, Icon.bean_image))
        time.sleep(0.5)
    
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
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.imagead1_blue))
        elif num == 9:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.imagead2_blue))
    
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
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.imagead1))
        elif num == 9:
            deck.set_key_image(num, PILHelper.to_native_key_format(deck, Icon.imagead2))

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".") #Use "img/" for terminal. Use "." for release.

    return os.path.join(base_path, relative_path)