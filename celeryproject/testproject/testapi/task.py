 
import logging
from django.core.mail import send_mail
from django.conf import settings
from testproject.celery import app
import traceback
from celery.task.schedules import crontab
from celery.decorators import periodic_task


@periodic_task(run_every=(crontab(hour=18, minute=36)), name="some_task", ignore_result=True)
def some_task():
    try:
        print("hello")
        subject = 'Thank you for registering to our site'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['abhishekinnotical@gmail.com']
        send_mail( subject, message, email_from, recipient_list )
    except Exception as error:
        traceback.print_exc()

@app.task
def send_verification_email():
    try:
        subject = 'Thank you for registering to our site'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['abhishekinnotical@gmail.com']
        send_mail( subject, message, email_from, recipient_list )
    except Exception as error:
        traceback.print_exc()

    