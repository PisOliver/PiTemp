#! /usr/bin/env python3.7

import os
import time
from datetime import datetime
from mailsender import sendemail

gputempcmd = "sudo vcgencmd measure_temp"
cputempcmd = "cat /sys/class/thermal/thermal_zone0/temp"
date = datetime.now()
starttime = 0

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
    num = num.replace("\n", '')
    return num

def high(temp):
    if float(temp) > 72.0:
        return True
    else:
        return False

while 1:
    gputemp = removetext(runcommand(gputempcmd).read())
    cputemp = float(runcommand(cputempcmd).read())/1000
    filetext = "CPU temp: " + str(cputemp) + "'C, GPU Temp: " + str(gputemp) + "'C\n"
    writefile(filetext)
    if high(cputemp) or high(gputemp):
        if starttime % 60 == 0:
            sendemail(True, cputemp, gputemp)
    starttime += 15
    time.sleep(15)

