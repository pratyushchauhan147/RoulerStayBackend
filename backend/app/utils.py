from django.conf import settings
from django.core.mail import send_mail

def sendmail(subject,email2,message):
    
    message = f'Hi , We are testing Our Backends You are a Test Subject we you got a message  from : {message}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email2]
    m =send_mail( subject, message, email_from, recipient_list )
    f = open("sent.txt", "w")
    f.write('\n'+message)
    f.close()
    

def verifymail(username,email2,otp):
    subject = 'welcome to RoulerStay'
    message = f'Welcome to RoulerStay , This is your 4 digit registration OTP :{otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email2]
    h = send_mail( subject, message, email_from, recipient_list )
    print(h)

