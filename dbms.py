import MySQLdb as sql
import datetime
from datetime import date
import csv

db = sql.connect("localhost", 'cn', 'Happy@123')

def motor():
	cr=db.cursor()
	cr.execute("SELECT * FROM motor")
	data = cr.fetchall()

        for row in data:
            a = row[0]
            b = row[1]
            c =	row[2]
	    d = row[3]	 		
	
	a_sec = a.total_seconds()
	b_sec = b.total_seconds()
	c_sec = c.total_seconds()
	d_sec = d.total_seconds()

	a_hrs = int(a_sec/3600)
	a_min = int(a_sec/60)%60	

	b_hrs = int(b_sec/3600)
	b_min = int(b_sec/60)%60

	c_hrs = int(c_sec/3600)
	c_min = int(c_sec/60)%60

	d_hrs = int(d_sec/3600)
	d_min = int(d_sec/60)%60


	atime = datetime.datetime.combine(datetime.datetime.today(),datetime.time(a_hrs,a_min,int(a_sec%60)))	
	btime = datetime.datetime.combine(datetime.datetime.today(),datetime.time(b_hrs,b_min,int(b_sec%60)))
	ctime = datetime.datetime.combine(datetime.datetime.today(),datetime.time(c_hrs,c_min,int(c_sec%60)))
	dtime = datetime.datetime.combine(datetime.datetime.today(),datetime.time(d_hrs,d_min,int(d_sec%60)))

        cr.close()
 	return atime,btime,ctime,dtime
	

# function for rfid sensor
def rfid(rfidno, entry_time, exit_time, status):
    cr = db.cursor()
    command1 = "CREATE TABLE rfid (rfidno VARCHAR(16),todays_date DATE,entry_time TIME,exit_time TIME,status VARCHAR(2) );"
    command2 = """INSERT INTO rfid VALUES('%s',CURDATE(),'%s','%s','%s')""" % \
               (rfidno, entry_time, exit_time, status)

    # if table doesnt exist,create and then insert
    try:
        cr.execute(command1)
        cr.execute(command2)
        print("command 1 and 2 executed ")
        db.commit()

    # if table extist,only insert
    except:
        cr.execute(command2)
        print("command 2 executed ")
        db.commit()
    cr.close()

# function for temperature sensor
def temperature(temp):
    cr = db.cursor()
    command1 = "CREATE TABLE temperature (todays_date DATE,temp FLOAT(2) );"
    command2 = """INSERT INTO temperature VALUES(CURDATE(),%s)""" % \
               (temp)

    # todays date
    #  todays_date=date.today()

    # converting date to string
    # td=str(todays_date)

    # taking dd from yyyy-mm-dd
    # td=td[-2:]

    # if equal to 01 then it means new month,therfore drop
    # if td=='01' :
    #   command3="DROP TABLE temperature"
    #  cr.execute(command3)
    # print("Temparature data of previous month deleted...")

    # if table doesnt exist,create and then insert
    try:
        cr.execute(command1)
        cr.execute(command2)
        print("command 1 and 2 executed ")
        db.commit()

    # if table extist,only insert
    except:
        cr.execute(command2)
        print("command 2 executed ")
        db.commit()
    cr.close()


# function for retrieving in csv file of motion from db
def rfidno_csv():
    cr = db.cursor()
    cr.execute("SELECT rfidno,status FROM rfid")
    # fetches all rows from databases
    data = cr.fetchall()

    with open('rfidno_data.csv', 'w') as csvfile:
        fwriter = csv.writer(csvfile)
	fwriter.writerow(['No','Status'])
        for row in data:
            a = row[0]
            b = row[1]
            # i th row of db
            l1 = (list((a, b)))
            # write i th row in .csv
            fwriter.writerow(l1)
    cr.close()


# function for retrieving in csv file of temperature from db
def temperature_csv():
    cr = db.cursor()
    cr.execute("SELECT * FROM temperature")
    # fetches all rows from databases
    data = cr.fetchall()

    with open('temperature_data.csv', 'w') as csvfile:
        fwriter = csv.writer(csvfile)
        flag = 0;
        sum = 0;
        count = 0;
	fwriter.writerow(['Date','Temp'])
        for row in data:
            a = row[0]
            b = row[1]

            if (flag == 0):
                z = str(a)
                flag = 1;

            if (str(a) == z):
                sum = sum + b;
                count = count + 1;
                continue

            l1 = (list((z, (sum / count))))
            fwriter.writerow(l1)
            z = str(a)
            sum = 0;
            count = 1;
            sum = sum + b;

        l1 = (list((z, (sum / count))))
        fwriter.writerow(l1)
    cr.close()


def motion(motion_time):
    cr = db.cursor()


    command1 = "CREATE TABLE motion (motion_time TIME);"
    command2 = """INSERT INTO motion VALUES('%s')""" % \
           (motion_time)

# if table doesnt exist,create and then insert
    try:
        cr.execute(command1)
        cr.execute(command2)
        print("command 1 and 2 executed ")
        db.commit()

# if table extist,only insert
    except:
        cr.execute(command2)
        print("command 2 executed ")
        db.commit()
    cr.close()


def motion_csv():
    cr = db.cursor()
    cr.execute("SELECT motion_time FROM motion")
    # fetches all rows from databases
    data = cr.fetchall()

    with open('motion_data.csv', 'w') as csvfile:
        fwriter = csv.writer(csvfile)
	fwriter.writerow(['Time'])
        l1=[]
        for row in data:
            a = row[0]
            a=str(a)
            a=a[:2]
            l1=[]
            l1.append(a)
            fwriter.writerow(l1)
    cr.close()


# connect user cn with pass Happy@123
def connect():
    cr = db.cursor()

    dbname = "homeautomation2"

    command1 = "CREATE DATABASE %s " % (dbname)
    command2 = "USE %s" % (dbname)

    try:
        # creating database and using the same.
        cr.execute(command1)
        cr.execute(command2)
    except:
        # if database exist ,use that db
        cr.execute(command2)

    cr.close()

#connect()
#rfid('14' , '11:00:00' , '22:00:00','U')
# flame('01:00:00' , '05:00:00')
#temperature(54)
# motor('00:07:00','06:00:05')
#motion('23:00:56')
#temperature_csv()
#motion_csv()
#rfidno_csv()






