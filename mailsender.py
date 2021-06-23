#! /usr/bin/env python3.7

import ssl
import smtplib
from email.message import EmailMessage

port = 465
password = "Sender Email Password"
senderemail = "Sender Email Address"
receivemail = "Receiver Email Address"

def sendemail(ishigh, cputemp, gputemp):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    msg = EmailMessage()
    msg['From'] = senderemail
    msg['To'] = receivemail
    if ishigh:
        msg['Subject'] = 'Warning about high temperature'
        msg.set_content('Be safe! Your Raspberry Pi temperature is high, its GPU temp is  ' + str(gputemp) + " 'C, its CPU temp is " + str(cputemp) + "'C")
    server.login(senderemail, password)
    server.send_message(msg)
    server.quit()

