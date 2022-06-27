#!/bin/python3
import sqlite3
from scapy.all import *
from socket import  *
import datetime
from datetime import date
from tkinter import ttk
import tkinter as tk
 
def View():
    packet = rdpcap("capture_packet.pcap")

    connection = sqlite3.connect("database_projet.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM packet_ip")

    rows = cursor.fetchall()    

    for row in rows:

        print(row) 

        tree.insert("", tk.END, values=row)        

    connection.close()


# connect to the database



window = tk.Tk()

tree = ttk.Treeview(window, column=("c1", "c2", "c3","c4", "c5", "c6","c7", "c8", "c9","c10",), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="ID")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="Mac Destination")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="Mac Source")

tree.column("#4", anchor=tk.CENTER)

tree.heading("#4", text="IP Source")

tree.column("#5", anchor=tk.CENTER)

tree.heading("#5", text="IP Destination")

tree.column("#6", anchor=tk.CENTER)

tree.heading("#6", text="protocol")

tree.column("#7", anchor=tk.CENTER)

tree.heading("#7", text="Version")

tree.column("#8", anchor=tk.CENTER)

tree.heading("#8", text="TTL")

tree.column("#9", anchor=tk.CENTER)

tree.heading("#9", text="Checksum")

tree.column("#10", anchor=tk.CENTER)

tree.heading("#10", text="Date")

tree.pack()

button1 = tk.Button(text="Display data", command=View)

button1.pack(pady=10)




window.mainloop()