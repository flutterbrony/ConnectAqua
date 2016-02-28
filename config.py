#!/usr/bin/env python
#coding: utf-8-

def get(param):
    if param == "time":
        config = open("./config.cfg", "r")
        dtime = config.readline()
        dtime = config.readline()
        config.close()
        heure = time.localtime(time.time())
        heure = time.strftime("%H:%M", heure)
        return (heure, dtime)
    elif param == "quality":
        config = open("./config.cfg", "r")
        dtime = config.readline()
        dtime = config.readline()
        config.close()
    elif param == "oxygen":
        config = open("./config.cfg", "r")
        dtime = config.readline()
        dtime = config.readline()
        config.close()
    elif param == "pH":
        config = open("./config.cfg", "r")
        dtime = config.readline()
        dtime = config.readline()
        config.close()
    elif param == "lum":
        config = open("./config.cfg", "r")
        dtime = config.readline()
        dtime = config.readline()
        config.close()
    elif param == "temp":
        config = open("./config.cfg", "r")
        dtime = config.readline()
        dtime = config.readline()
        config.close()
    elif param =="lang":
        config = open("./config.cfg", "r")
        language = config.readline()
        language = config.readline()
        config.close()
        return language
def write(param,text):
    if param == 
