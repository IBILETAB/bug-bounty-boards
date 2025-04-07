# The Ram - Open Terminal (macOS)
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
kbd.press(Keycode.GUI, Keycode.SPACE)  # Spotlight
kbd.release_all()
time.sleep(0.5)
layout.write("terminal")
kbd.press(Keycode.ENTER)
kbd.release_all()

# The Ram - End of File
