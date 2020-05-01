import RPi.GPIO as g
g.setwarnings(False)
g.setmode(g.BOARD)

g.setup(38,g.IN)

import time as t

def moisture():
        moist=g.input(38)
	if moist == 1:
		print("\tPlease water your plants")

	return moist

