from scapy.all import ARP, Ether, srp, arping
import sys

def scan_network(ip_range):
    print(f"Scanning network: {ip_range}")
    # Use arping for better reliability in some network configurations
    answered, unanswered = arping(ip_range, timeout=5, verbose=1)

    # Process the result
    devices = []
    for sent, received in answered:
        print(f"Received response from IP: {received.psrc}, MAC: {received.hwsrc}")
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

def print_devices(devices):
    print("Available devices in the network:")
    print("IP" + " "*18 + "MAC")
    for device in devices:
        print(f"{device['ip']:16}    {device['mac']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: sudo python network_scan.py <IP_RANGE>")
        sys.exit(1)

    ip_range = sys.argv[1]
    devices = scan_network(ip_range)
    print_devices(devices)
