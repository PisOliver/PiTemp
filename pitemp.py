#! /usr/bin/env python3.7

import os
import time
from datetime import datetime
from mailsender import sendemail

gputempcmd = "sudo vcgencmd measure_temp"
cputempcmd = "cat /sys/class/thermal/thermal_zone0/temp"
date = datetime.now()

def runcommand(command):
    stream = os.popen(command)
    return stream

def writefile(content):
    file = open("templog.txt", 'a')
    date = datetime.now()
    formdate= date.strftime("%d/%m/%Y %H:%M:%S")
    file.write(formdate)
    file.write(" ")
    file.write(content)
    return

def removetext(bem):
    num = bem.replace('temp=', '')
    num = num.replace("'C", '')
    return num

def high(temp):
    if float(temp) > 65.0:
        return True
    else:
        return False

while 1:
    gputemp = removetext(runcommand(gputempcmd).read())
    cputemp = float(runcommand(cputempcmd).read())/1000
    writefile("CPU temp: " + cputemp + " 'C, GPU Temp: " + gputemp + "'C")
    if high(gputemp):
        sendemail("high", gputemp)
    time.sleep(15)

