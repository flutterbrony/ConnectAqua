#!/usr/bin/env python
#coding: utf-8-

#importation des modules
import RPi.GPIO as GPIO
import time

#appel aux modules


#paramètrage
config = open("./config.cfg", "r")
dtime = config.readline()
dtime = config.readline()
config.close()
heure = time.localtime(time.time())
heure = time.strftime("%H:%M", heure)
if dtime is heure:
    miam.distrib(1)

#programme
def distrib(now):
    if now ==1:
        GPIO.output(18,1)
        time.sleep(4)
        dpsensor2 = GPIO.input(4)
        while dpsensor2 != 1:
            dpsensor = GPIO.input(4)
            print("Entrez dpsensor2")
            dpsensor2 = int(input())
            time.sleep(0.2)
        GPIO.output(18,0)

        
