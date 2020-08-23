#!/usr/bin python
# -*- coding: utf-8 -*-

import json, requests, time

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from luma.core.legacy.font import proportional, LCD_FONT
from luma.core.legacy import text, show_message

# creating the device 
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, width=32, height=8, block_orientation=-90, rotate=2)

startmsg = " _"

while True :
    headers = {"User-Agent":"Mozilla/5.0"}
    resp = requests.get("https://script.googleusercontent.com/macros/echo?user_content_key=SrpenCHi0GpW2QZIOcnXuQlQ46wnDyaNdvBOM7RpGz29seWIILAMIyuVikX88PDFtu2PXaQgEHVCQSxnjkQbilGLcjiTk5T9m5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnJ9GRkcRevgjTvo8Dc32iw_BLJPcPfRdVKhJT5HNzQuXEeN3QFwl2n0M6ZmO-h7C6eIqWsDnSrEd&lib=MwxUjRcLr2qLlnVOLh12wSNkqcO1Ikdrk", headers=headers)
    data = json.loads(resp.text)
    msg = data['fulldate']
    show_message(device, startmsg , fill="white", font=proportional(LCD_FONT),scroll_delay=0.05)
    show_message(device, msg , fill="white", font=proportional(LCD_FONT),scroll_delay=0.06)
    time.sleep(1800.0)
