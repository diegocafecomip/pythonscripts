from scapy.all import sniff, IP, ICMP, ARP, wrpcap, sr1
import threading
import time

# Target IP for ping
target_ip = "192.168.1.20"

# Output pcap file
pcap_file = "ping_and_arp_capture.pcap"

# Duration of packet capture in seconds
capture_duration = 5

# Packet filter (BPF syntax) to capture ARP and ICMP
packet_filter = f"(icmp or arp) and (host {target_ip} or ether dst ff:ff:ff:ff:ff:ff)"

# Container for captured packets
captured_packets = []

# Threaded capture function
def capture_packets():
    global captured_packets
    print("[*] Starting packet capture...")
    captured_packets = sniff(filter=packet_filter, timeout=capture_duration)
    print(f"[*] Capture complete: {len(captured_packets)} packet(s) captured.")

# Start packet capture in background
sniffer_thread = threading.Thread(target=capture_packets)
sniffer_thread.start()

# Wait briefly to ensure capture has started
time.sleep(1)

# Send ICMP Echo Request (ping)
print(f"[*] Sending ICMP ping to {target_ip}...")
response = sr1(IP(dst=target_ip)/ICMP(), timeout=2, verbose=0)

if response:
    print("[*] Ping response received:")
    response.show()
else:
    print("[!] No ping response received.")

# Wait for capture to finish
sniffer_thread.join()

# Save packets to pcap
if captured_packets:
    wrpcap(pcap_file, captured_packets)
    print(f"[*] Packets saved to {pcap_file}")
    print("[*] You can now open this file in Wireshark.")
else:
    print("[!] No packets captured.")
