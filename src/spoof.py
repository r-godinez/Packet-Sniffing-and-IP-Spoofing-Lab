# spoof script
#!/usr/local/bin/python3
from scapy.all import *

a=IP()
a.src='192.168.254.254' # spoofed IP
a.dst='192.168.144.131' # destination IP ( server )
b=ICMP()
packet=a/b
send(packet)