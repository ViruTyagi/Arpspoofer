import scapy.all as scapy
import optparse

def scan(ip):
	request = scapy.ARP(pdst = ip)
	brodcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
	arp_brodcast = brodcast/request
	useful = scapy.srp(arp_brodcast, timeout = 1,verbose = False)[0]
	client_list = []
	for i in useful:
		client_dict = {"ip":i[1].psrc , "mac":i[1].hwsrc}
		client_list.append(client_dict)
	return client_list

def get_ip():
	parser = optparse.OptionParser()
	parser.add_option("-i","--ip",dest = "ip",help = "Enter the ip to search for")
	option  = parser.parse_args()[0]
	return option

def pf(listt):
	print("IP \t\t\t Mac\n -----------------------------")
	for i in listt:
		print(i["ip"] + "\t\t" + i["mac"])

option = get_ip()
listt = scan(option.ip)
pf(listt)
