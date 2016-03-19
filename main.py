#!/usr/bin/env python
#coding: utf-8-

#importation des modules
import sys
path = "./"
sys.path.append(path)
import time
import RPi.GPIO as GPIO
from tkinter import *
#import server.py
import miam
import pH
import oxygen
import temp
import server
import config
import quali

#paramètrage des broches
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)      #capteur de position distributeur
GPIO.setup(18,GPIO.OUT)     #commande distributeur
GPIO.setup(19,GPIO.OUT)

#variables
evening = 18
morning = 8

#appel aux modules
while True:
    #configuration

    #nourriture
    heure = config.get(foodtime)
    
    print (heure)
    print("Entrez dtime")
    dtime = int(input())
    if dtime is heure:
        miam.distrib(1)
    time.sleep(0.2)
    #oxigen
    
    #pH
    
    #server
    
    #cam
    
    #lum
    dtime = date(hour)
    if dtime is morning:
        GPIO.output(19,HIGH)
    elif dtime = evening:
        GPIO.output(19,LOW)
    
    #temp

#test des GPIO


#fin du programme
GPIO.cleanup()
exit()
