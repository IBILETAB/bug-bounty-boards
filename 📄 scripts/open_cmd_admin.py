# The Ram - Open CMD as Administrator (Windows)
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
kbd.press(Keycode.WINDOWS)
kbd.release_all()
time.sleep(0.5)
layout.write("cmd")
time.sleep(0.5)
kbd.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.ENTER)
kbd.release_all()

# The Ram - End of File

