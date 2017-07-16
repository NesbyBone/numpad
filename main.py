#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import time

from kivy.app import App
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')

class SetNamePopup(Popup):
	pass

class GuiGridLayout(GridLayout):
    
    def setName(self, *args):
		SetNamePopup().open()
    
    def TapNumber(self, N):
        if len(self.display.text) < 8:
            self.display.text += N

    def SendSMS(self):

        celphone = self.ids.entry.text
        self.ids.entry.text = ""

        ser = serial.Serial('/dev/ttyS0', 115200, timeout=5)
        time.sleep(1)
        ser.write('ATZ\r')
        time.sleep(1)
        ser.write('AT+CMGF=1\r')
        time.sleep(1)
        ser.write('''AT+CMGS="''' + celphone + '''"\r''')
        time.sleep(1)
        ser.write('Soy el Servidor enviandote un sms de promocion' + "\r")
        time.sleep(1)
        ser.write(chr(26))
        time.sleep(1)
        print "Message Sent!\n"
        time.sleep(1)
        ser.close()
        App.get_running_app().stop()

class MyGui(App):
    def build(self):
        return GuiGridLayout()

if __name__ == '__main__':
    MyGui().run()
