#!/usr/bin/env python
#coding: utf-8-

#importation des modules
import RPi.GPIO as GPIO

#paramètrage des broches
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)

