import subprocess
import time

def connect_to_wifi(ssid, password):
    # Disconnect from any existing Wi-Fi network
    subprocess.run(["netsh", "interface", "set", "interface", "name='Wi-Fi'", "admin=disable"], shell=True)
    subprocess.run(["netsh", "interface", "set", "interface", "name='Wi-Fi'", "admin=enable"], shell=True)

    # Connect to the specified Wi-Fi network
    subprocess.run(["netsh", "wlan", "add", "profileparameter", "user=current", "name=" + ssid, "keyMaterial=" + password])

    subprocess.run(["netsh", "wlan", "connect", "name="+ssid], shell=True)

    # Wait for a moment for the connection to be established
    time.sleep(5)

if __name__ == "__main__":
    # Replace 'your-wifi-ssid' and 'your-wifi-password' with the actual values
    wifi_ssid = "THETAXS00312899.OSC" #cameras wifi ssid
    wifi_password = "00312899"  #wifi password

    # Call the connect_to_wifi function
    connect_to_wifi(wifi_ssid, wifi_password)
