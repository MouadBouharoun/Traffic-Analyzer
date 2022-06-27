#!/bin/python3
from scapy.all import *
from scapy.utils import PcapWriter
p=sniff(iface="eth0", count=20)
pktdump = PcapWriter("capture_packet.pcap", append=True, sync=True)
pktdump.write(p)