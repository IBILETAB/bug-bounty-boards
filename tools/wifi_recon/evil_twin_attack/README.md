# 🧠 Evil Twin Attack

This script sets up your ESP32 as an Evil Twin (spoofed access point) to capture network traffic or attempt to trick users into connecting to a fake AP.

## 🔧 Requirements
- **ESP32 with CircuitPython** installed
- `network` module for managing Wi-Fi connections
- **Password** for setting up the fake access point (WPA2-PSK)

## 🎯 How to Use:
1. Run the script on your ESP32.
2. Input the **SSID** of the network you want to spoof and a **password** for your fake AP.
3. The ESP32 will create a fake AP with the same SSID.
4. The script will keep the fake AP running indefinitely.

## 🛡 Legal Disclaimer
Use for authorized penetration testing only. Do not engage in unauthorized activities.
