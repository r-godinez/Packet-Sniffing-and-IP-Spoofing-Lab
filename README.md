# Packet-Sniffing-and-IP-Spoofing
**Final Project for 4309 Fundamentals of Cybersecurity - Fall 2023**

## Virtual Network Diagram 
![Alt text](imgs/4309_network_diagram.png)

### Set-up Virtual Machines (VM)
#### Download the virtual machine file (VM):
https://drive.google.com/file/d/138fqx0F8bThLm9ka8cnuxmrD6irtz_4m/view

#### Virtual Machine set-up:
https://github.com/seed-labs/seed-labs/blob/master/manuals/vm/seedvm-manual.md

#### Once VM are set up, verify VMs are up-to-date with the following commands: 
**% sudo apt-get update**

**% sudo apt-get dist-upgrade**

#### We must ensure python and scapy library is installed on the ATTACKER VM. You can check to see if python is already installed, use the following command:
**% python3 --version or % python --version**

#### If your machine doesn't have python installed, you can download from the following link: 
**https://www.python.org/downloads/**

#### For the scapy library, use the following command to install Scapy:
**% python3 install scapy**

#### Run scripts on Attacker VM
Make python file an executable: **% chmod a+x sniff_and_spoof.py**

Become root user to run sniffer script: **% sudo -i**

Run python script: **% python3 sniff_and_spoof.py**