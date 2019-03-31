import smtplib 

def send_mail(email,password,message,whereto):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email,password)
    server.sendmail(email,whereto,message)
    server.quit

email = raw_input("Enter your mail >> ")
password = raw_input("EnterYourPassowrd >> ")
whereto = raw_input("Enter the email where you want to send the result >> ")
message = raw_input("Message >> ")

send_mail(email,password,message,whereto)
