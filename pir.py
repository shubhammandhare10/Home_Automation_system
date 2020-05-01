import RPi.GPIO as g
g.setwarnings(False)
g.setmode(g.BOARD)
g.setup(24,g.IN) # PIR SENSOR 

import time as t

def motion():
        PIR=g.input(24)
        return PIR       

