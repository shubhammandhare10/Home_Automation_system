import time as t
import RPi.GPIO as g
g.setmode(g.BOARD)
g.setup(16,g.OUT)
g.setup(18,g.OUT)
g.setwarnings(False)

def clockwise():
        g.output(16,1)
        g.output(18,0)
        t.sleep(5)
        g.output(16,0)
        g.output(18,0)

def anticlockwise():
        g.output(16,0)
        g.output(18,1)
        t.sleep(5)
	g.output(16,0)
	g.output(18,0)
