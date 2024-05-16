from scapy.all import sniff, IP, TCP
from collections import defaultdict

# Function to capture network packets
def capture_packets(count=1000):
    packets = sniff(count=count)
    return packets

# Function to analyze captured packets
def analyze_packets(packets):
    connections = defaultdict(int)
    for pkt in packets:
        if IP in pkt and TCP in pkt:
            src = pkt[IP].src
            dst = pkt[IP].dst
            connections[(src, dst)] += len(pkt)
    return connections

# Function to get data for network activity
def get_network_activity_data():
    packets = capture_packets()
    connections = analyze_packets(packets)
    labels = [f"{conn[0]} -> {conn[1]}" for conn in connections]
    sizes = list(connections.values())
    return labels, sizes

if __name__ == "__main__":
    labels, sizes = get_network_activity_data()
