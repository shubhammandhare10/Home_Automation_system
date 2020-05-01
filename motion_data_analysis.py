import matplotlib.pyplot as plt
import numpy as np
import csv

def analyze():
	file = open('motion_data.csv', 'r')
	reader = csv.DictReader(file)

	time8_12 = []
	time12_16 = []
	time16_20 = []
	time20_24 = []

	time = []
	dates = []

	d = np.arange(1,30)
	for r in reader:
		dates.append(str(r['Date']))
		time.append(int(r['Time']))
		if int(r['time']) > 8 and int(r['time']) < 12:
			time8_12.append(int(r['time']))
		elif int(r['time']) > 12 and int(r['time']) < 16:
			time12_16.append(int(r['time']))
		elif int(r['time']) > 16 and int(r['time']) < 20:
			time16_20.append(int(r['time']))
		elif int(r['time']) > 20 and int(r['time']) < 24:
			time20_24.append(int(r['time']))

	l = [len(time8_12), len(time12_16), len(time16_20), len(time20_24)]
	xaxes = ['8-12','12-16','16-20','20-24']
	index = np.arange(len(xaxes))
	plt.bar(index, l)
	plt.xticks(index, xaxes)
	plt.xlabel('Time')
	plt.ylabel('Count')
	plt.title('Motion detection analysis')
	plt.show()