# packet sniffing
#!/usr/local/bin/python3
from scapy.all import *

print ("SNIFFING PACKETS...")

def print_pkt(pkt):
    pkt.show()

pkt=sniff(iface=['ens33','ens34'],filter='icmp',prn=print_pkt)
