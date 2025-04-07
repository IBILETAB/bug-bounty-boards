# The Ram - Wi-Fi Sniffer (Network Scanner)
# Created for educational and ethical hacking use.
# --------------------------------------------

import network
import time

# Scanning for available networks
def scan_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print("[+] Scanning for Wi-Fi networks...")
    networks = wlan.scan()
    
    for ssid, bssid, channel, RSSI, authmode, hidden in networks:
        print(f"SSID: {ssid}, Channel: {channel}, Signal Strength: {RSSI} dBm")

# Main execution
if __name__ == "__main__":
    print("[+] Starting Wi-Fi Scanner...")
    scan_wifi()
