import psutil
from twisted.internet import task, reactor

class BandwidthMonitor:
    def __init__(self, interval=1):
        self.interval = interval

    def get_bandwidth_usage(self):
        # Get current network usage statistics
        net_stats = psutil.net_io_counters()

        # Calculate total bytes sent and received
        bytes_sent = net_stats.bytes_sent
        bytes_received = net_stats.bytes_recv

        # Convert bytes to megabytes
        mb_sent = bytes_sent / (1024 * 1024)
        mb_received = bytes_received / (1024 * 1024)

        mb_sent = round(mb_sent, 3)
        mb_received = round(mb_received, 3)

        return mb_sent, mb_received

    def print_bandwidth_usage(self):
        mb_sent, mb_received = self.get_bandwidth_usage()
        print(f"Bandwidth Usage - Sent: {mb_sent:.2f} MB, Received: {mb_received:.2f} MB")

    def start_monitoring(self):
        # Start monitoring bandwidth usage periodically
        lc = task.LoopingCall(self.print_bandwidth_usage)
        lc.start(self.interval)

if __name__ == '__main__':
    # Create an instance of BandwidthMonitor
    bandwidth_monitor = BandwidthMonitor(interval=60)  # Monitoring interval in seconds

    # Start monitoring
    bandwidth_monitor.start_monitoring()

    # Run the Twisted reactor
    reactor.run()
