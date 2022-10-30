from django.conf import settings
from django.core.mail import send_mail

def Sending_Emails():
    subject = 'welcome to Assignment Management Application world'
    message = 'Hi  thank you for registering in Assignment system application :)'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["subhajitstudent8@gmail.com", ]
    flag = send_mail(subject, message, email_from, recipient_list)
    return flag

