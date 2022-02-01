import smtplib
import textwrap
from datetime import datetime
from logger import *


def notify(a, b):
    # Login Credintials

    gmail_user = "fazalahmadqureshi4@gmail.com"
    gmail_password = "fazal12345"

    send_from = gmail_user
    send_to = ["fazalahmadqureshi4@gmail.com"]
    subject = b
    body = a

    # ACHTUNG Protocol Text is hard stricted formatted --> Capital/Small, Spaces etc
    email_text = textwrap.dedent(f"""\
    From: {send_from}
    To: {send_to}
    Subject: {subject}
    {body}
    """)

    try:

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        #start the connection
        server.ehlo() # Hello message to the server (extended hello), kind of a protocol connection command

        #login to the server
        server.login(gmail_user, gmail_password)

        #send data
        server.sendmail(send_from, send_to, email_text)

        # close connection
        server.close()

        logger.info("Email notification sent") #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~logger

    except:
        print("Something went wrong !!!")

