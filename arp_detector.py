import scapy.all as scapy

def get_mac(ip):
	request = scapy.ARP(pdst = ip)
	brodcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
	arp_brodcast = brodcast/request
	useful = scapy.srp(arp_brodcast, timeout = 1,verbose = False)[0]
	return useful[0][1].hwsrc

def sniff(interface):
    scapy.sniff(iface = interface,store = False,prn = process)

def process(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op = 2:
        try:
            real_mac = get_mac[packet[scapy.ARP].psrc]
            response_mac = packet[scapy.ARP].hwsrc

            if real_mac != response_mac:
                print("[+] You are under attack")
        except IndexError:
            pass

sniff("wlp2s0")


        