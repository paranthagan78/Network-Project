'''
monitoring changes in available WiFi networks on a Windows
system using the netsh command and Twisted framework. Let's break
down the purpose of each part of the code
'''


import subprocess
import time
from twisted.internet import task, reactor

class WiFiMonitor:
    def __init__(self):
        self.network_name = "SSN"
        self.password = "Ssn1!Som2@Sase3#"
        self.previous_networks = []

    def get_available_networks(self):
        # Run netsh command to list available WiFi networks
        result = subprocess.run(['netsh', 'wlan', 'show', 'network'], capture_output=True, text=True)
        output_lines = result.stdout.splitlines()

        # Extract SSID names from the output
        available_networks = []
        for line in output_lines:
            if 'SSID' in line:
                ssid = line.split(':')[1].strip()
                available_networks.append(ssid)
        return available_networks

    def start_monitoring(self):
        print("Starting WiFi monitoring...")
        # Store initial list of available networks
        self.previous_networks = self.get_available_networks()

    def check_network_changes(self):
        # Get the current list of available networks
        current_networks = self.get_available_networks()

        # Check for new networks
        new_networks = [network for network in current_networks if network not in self.previous_networks]
        if new_networks:
            print("Detected new WiFi networks:")
            for network in new_networks:
                print(network)

        # Check for disappeared networks
        disappeared_networks = [network for network in self.previous_networks if network not in current_networks]
        if disappeared_networks:
            print("Detected disappeared WiFi networks:")
            for network in disappeared_networks:
                print(network)

        # Update previous_networks for the next iteration
        self.previous_networks = current_networks

if __name__ == '__main__':
    # Create an instance of WiFiMonitor
    wifi_monitor = WiFiMonitor()

    # Start monitoring WiFi networks
    wifi_monitor.start_monitoring()

    # Check for network changes periodically
    lc = task.LoopingCall(wifi_monitor.check_network_changes)
    lc.start(1)  # Check every 5 seconds

    # Run the Twisted reactor
    reactor.run()
