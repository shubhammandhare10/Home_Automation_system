import RPi.GPIO as g
import time as t
g.setmode(g.BOARD)

def startMotion():
	g.setwarnings(False)
	g.setup(40,g.OUT)
	g.output(40,True)        
	t.sleep(5)
	g.setup(40,g.OUT)
	g.output(40,False)


def startSoil():
	g.setwarnings(False)
	g.setup(22,g.OUT)
	g.output(22,True)

def stopSoil():
	g.setup(22,g.OUT)
	g.output(22,False)

def stopMotion():
	g.setwarnings(False)
	g.setup(40,g.OUT)
	g.output(40,False)
