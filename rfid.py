import RPi.GPIO as g
g.setwarnings(False)
g.setmode(g.BOARD)

import time as t
import serial as s

def auth():
	d=s.Serial("/dev/ttyAMA0",9600,timeout=1)
	a = d.readline()
	if(len(a)>3):
		print "\tYour RFID number is",  a
		return str(a)

def auth1():
	d=s.Serial("/dev/ttyAMA0",9600,timeout=1)
        a = d.readline()
        if(len(a)>3):
                print "\tYour RFID number is",  a
                return str(a)

		
