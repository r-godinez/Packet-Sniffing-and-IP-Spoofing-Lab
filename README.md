# Packet Sniffing and IP Spoofing Lab

## Overview

This lab explores two critical techniques—**packet sniffing** and **IP spoofing**—that demonstrate the vulnerabilities and threats to network security.

### Packet Sniffing
Packet sniffing involves capturing and analyzing network traffic, providing essential insights for network performance and troubleshooting. However, it can also be exploited to intercept sensitive data, such as passwords and private communications, making it a powerful tool in both network diagnostics and cyberattacks.

### IP Spoofing
IP spoofing involves manipulating the source IP address in a packet to masquerade as another device on the network. This technique is often used in cyberattacks such as **man-in-the-middle** and **denial-of-service (DoS)** attacks. Understanding the mechanics of IP spoofing is critical to building strong defenses in network security.

## Importance to Network Security
By studying and implementing these techniques in a controlled environment, this lab provides valuable hands-on experience in understanding network vulnerabilities. This knowledge is key to developing effective strategies for securing networks, including encryption, intrusion detection systems, and network monitoring solutions.

## Educational Goals
This lab aims to:
- Provide a practical understanding of network traffic monitoring via packet sniffing.
- Illustrate how IP spoofing can be used in cyberattacks and why it is a significant threat.
- Equip learners with the skills to design and implement security measures to counteract these vulnerabilities.


## Network Diagram for Virtual Environment
![Alt text](imgs/4309_network_diagram.png)

## Running the Lab
### Setup Virtual Machines (VM)
#### Download the virtual machine file (VM):
https://drive.google.com/file/d/138fqx0F8bThLm9ka8cnuxmrD6irtz_4m/view

### Virtual Machine Setup:
https://github.com/seed-labs/seed-labs/blob/master/manuals/vm/seedvm-manual.md

#### Once VM is setup, verify VMs is up-to-date with the following commands: 
***Run this command on all of the VMs***
 ```console
 ~$ sudo apt-get update && sudo apt-get dist-upgrade
 ```

#### Verify the **Attacker** VM has ***Python*** and ***Scapy*** library installed
*Verify if Python is installed with either of the following command:*
```console
~$ python3 --version 
```
or
```console
~$ python --version
```
*Install Python using the following link:*
**https://www.python.org/downloads/**

*Install Scapy with the following command:*
```console
~$ python3 install scapy
```
or
```console
~$ python install scapy
```

## Run Python scripts on the Attacker VM
**Use Python files from src folder**

*Make Python file an executable file:* 
```console
~$ chmod a+x sniff_and_spoof.py
```

*Must become root user to run sniffer script:*
```console
~$ sudo -i
```
*Run python script:*
```console
~% python3 sniff_and_spoof.py
```
or
```console
~$ python sniff_and_spoof.py
```