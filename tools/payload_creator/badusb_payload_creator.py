# The Ram - BadUSB Payload Generator
# Created for educational and ethical hacking use.
# --------------------------------------------

import time
import os

def create_payload(payload_name, payload_command):
    code = f'''
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

time.sleep(3)
kbd.press(Keycode.WINDOWS, Keycode.R)
kbd.release_all()
time.sleep(1)
layout.write("{payload_command}")
kbd.press(Keycode.ENTER)
kbd.release_all()
'''

    folder = "generated_payloads"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{payload_name}.py")
    with open(path, "w") as f:
        f.write(code.strip())
    print(f"[+] Payload saved to {path}")

if __name__ == "__main__":
    print("=== BadUSB Payload Generator ===")
    name = input("Payload name: ")
    command = input("Command to execute: ")
    create_payload(name, command)

# The Ram - End of File
