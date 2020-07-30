#!/usr/bin python
# -*- coding: utf-8 -*-

import json, requests, time

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from luma.core.legacy.font import proportional, LCD_FONT
from luma.core.legacy import text, show_message

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=32, height=8, block_orientation=+90)

startmsg = "Current BTC Price: "

while True :
    headers = {"User-Agent":"Mozilla/5.0"}
    resp = requests.get("https://api.cryptonator.com/api/ticker/btc-usd", headers=headers)
    data = json.loads(resp.text)
    msg = data['ticker']['price']
    show_message(device, startmsg , fill="white", font=proportional(LCD_FONT),scroll_delay=0.06)
    show_message(device, msg , fill="white", font=proportional(LCD_FONT),scroll_delay=0.06)
    time.sleep(0.1)
