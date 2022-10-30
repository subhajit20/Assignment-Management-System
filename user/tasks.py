from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

@shared_task(bind=True)
def Sending_Emails(self,email_handle):
    subject = 'welcome to Assignment Management Application world'
    message = 'Hi  thank you for registering in Assignment system application :)'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_handle,]
    send_mail(subject, message, email_from, recipient_list)

    return 1

@shared_task(bind=True)
def Sending_Emails_For_Reseting_Password(self,email_handle,link):
    subject = 'Password reset'
    message = f'click this link to reset your password =>  {link}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_handle,]
    send_mail(subject, message, email_from, recipient_list)

    return 1