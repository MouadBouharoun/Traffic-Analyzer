#!/bin/python3
import sqlite3
from scapy.all import *
import datetime
from datetime import date
connection = sqlite3.connect("database_projet.db")
cursor = connection.cursor()
packet = rdpcap("capture_packet.pcap")
cursor.execute('create table packet_ip(id int, mac_dst char(12),mac_src char(12),ip_src char(12),ip_dst char(12),protocol char(10),version char(10),ttl char(10),chksum char(10),date Date)')
for pkt in packet:
    if pkt.haslayer(IP):
        a = cursor.lastrowid
        b = pkt[Ether].dst
        c = pkt[Ether].src
        d = pkt[IP].src
        e = pkt[IP].dst
        f = pkt[IP].proto
              
        g = pkt[IP].version
        h = pkt[IP].ttl
        i = pkt[IP].chksum
        j = date.today()
        new_datagrame=(a,b,c,d,e,f,g,h,i,j)
        cursor.execute('insert into packet_ip values(?,?,?,?,?,?,?,?,?,?)', new_datagrame)

cursor.execute('select * from packet_ip')
connection.commit()
print(cursor.fetchall())

connection.close()