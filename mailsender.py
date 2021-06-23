#! /usr/bin/env python3.7

import ssl
import smtplib
from email.message import EmailMessage

port = 465
password = "Sender Email Password"
senderemail = "Sender Email Address"
receivemail = "Receiver Email Address"

def sendemail(hol, temp):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    msg = EmailMessage()
    msg['From'] = senderemail
    msg['To'] = receivemail
    if hol == "high":
        msg['Subject'] = 'Warning about high temperature'
        msg.set_content('Be safe! Your Raspberry Pi temperature is high, it is ' + str(temp) + " 'C")

    server.login(senderemail, password)
    server.send_message(msg)
    server.quit()

