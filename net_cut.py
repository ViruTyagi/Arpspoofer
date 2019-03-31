import netfilterqueue
import subprocess
try:
    def packet_printer(packet):
        print(packet)
        packet.accept()
    
    subprocess.call("iptables -I INPUT -j NFQUEUE --queue-num 2",shell = True)
    subprocess.call("iptables -I OUTPUT -j NFQUEUE --queue-num 2",shell = True)
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(2,packet_printer)
    queue.run()
except KeyboardInterrupt:
    subprocess.call("iptables --flush",shell = True)
    print("\n[-] Detected Ctrl + C , Now quiting .../ ")
