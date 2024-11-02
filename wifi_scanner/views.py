import pywifi
import time
import numpy as np
from django.shortcuts import render

# Initialize the Wi-Fi interface
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

# Function to scan and get Wi-Fi RSSI
def scan_wifi():
    iface.scan()  # Trigger Wi-Fi scan
    time.sleep(3)  # Give some time for scan to complete
    results = iface.scan_results()
    
    # Store network name (SSID) and RSSI
    network_data = []
    for network in results:
        ssid = network.ssid
        rssi = network.signal  # RSSI value in dBm
        network_data.append({'ssid': ssid, 'rssi': rssi})
    
    return network_data

# Django view to display Wi-Fi RSSI data
def wifi_signal_strength_view(request):
    # Capture Wi-Fi signal strength
    network_data = scan_wifi()
    
    # Calculate the average RSSI for each network
    ssids = list(set([net['ssid'] for net in network_data]))
    avg_rssi_data = {ssid: np.mean([net['rssi'] for net in network_data if net['ssid'] == ssid]) for ssid in ssids}
    
    context = {
        'network_data': network_data,
        'avg_rssi_data': avg_rssi_data
    }
    
    return render(request, 'scanner.html', context)
