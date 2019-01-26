import optparse
import subprocess
import re

def mac_changer(interface,new_mac):
	print("[+] changing mac address of " + interface + " to " + new_mac)
	subprocess.call(["ifconfig", interface ,"down"])
	subprocess.call(["ifconfig", interface ,"hw","ether",new_mac])
	subprocess.call(["ifconfig", interface ,"up"])

def parsing():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface",dest = "interface",help = "Enter the Interface to change mac address")
	parser.add_option("-m","--mac",dest = "new_mac",help = "Enter the new mac address")
	options = parser.parse_args()[0]
	if not options.interface:
		print("[-] Please enter the Interface, Type --help for more options")
	elif not options.new_mac:
		print("[-] Please enter the Mac Address, Type --help for more options")
	return options

def get_current_mac(interface):
	result_ifconfig = subprocess.check_output(["ifconfig",interface])
	mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result_ifconfig)
	if mac_address:
		return mac_address.group(0)
	else:
		print("[-] could not read mac address")

options = parsing()
print("current mac >> " + str(options.new_mac))
mac_changer(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
	print("[+] mac address successfully changed")
else:
	print("[-] something wrong")


