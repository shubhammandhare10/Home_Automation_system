import rfid as r
import pir as p
import soil as s
import ledmotion as l
import time as t
import temperature as temp
import motor1 as mo
import datetime
import dbms as db

db.connect()
counter = 3
print("\t\t\t\t\tWaiting for RFID authentication")
while(counter>0):
	flag = 0
	a = r.auth()
	rfidno=str(a)
	if(a=='45004155C293'):					 #rfid
		curtime0=datetime.datetime.time(datetime.datetime.now())
		curtime1=curtime0.strftime("%H:%M:%S")
		print(curtime1)
		status='S'
		print("\t\t\t\tAccess granted")
		a = ''
		while(1):
			m = p.motion()                          #motion
                        if(m==1):
				curtime=datetime.datetime.time(datetime.datetime.now())
				curtime9=curtime.strftime("%H:%M:%S")
				db.motion(curtime9)
                                print("\tMotion detected, turning lights on\n")
                                l.startMotion()
				break

		while(1):					#outer while for authorization
		
			x = s.moisture()			#moisture

			if(x==0):				#no moisture start led
				l.stopSoil()
			elif(x==1):
				l.startSoil()		
			
			currtemp = temp.read_temp()
			
			if(flag==0):
				if currtemp>25:
					print("\n\tCurrent temp : {}").format(currtemp)
					print("\tTurning AC on to 25\n")
					flag = 1
					db.temperature(currtemp)
				elif currtemp<25:
					print("\n\tCurrent temp: {}").format(currtemp)
					print("\tTurning heater on to 25\n")
					flag = 1

			ctime = datetime.datetime.now()
			
			sotime,sotime1,sctime,sctime1 = db.motor()

			if ctime>sotime and ctime<sotime1: 
				print("\n\n\tCurtains opening as scheduled")
				mo.clockwise()
			
			elif ctime>sctime and ctime<sctime1:
				print("\tCurtains closing as scheduled")
				mo.anticlockwise()	

			t.sleep(0.3)

			aexit = r.auth1()
			if(aexit == '45004155C293'):
				curtime0=datetime.datetime.time(datetime.datetime.now())
				curtime2=curtime0.strftime("%H:%M:%S")
				print(curtime2)
				db.rfid(rfidno,curtime1,curtime2,status)
				print("\n\n\t\t\t\tGoodbye, have a nice day!")
				aexit = 0
				db.temperature_csv()
				db.rfidno_csv()
				db.motion_csv()
				print("\t\t------------------------------------------------------------------------------")
				t.sleep(3)
				break	


	elif(a == None):
		a = '0'

	else:
		counter -= 1
		print("{} tries left").format(counter)
