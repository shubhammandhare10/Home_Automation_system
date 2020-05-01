import matplotlib.pyplot as plt
import numpy as np
import csv

def analyze():
	file = open('temperature_data.csv', 'r')
	reader = csv.DictReader(file)

	temp = []
	dates = []

	d = np.arange(1,30)
	for r in reader:
		dates.append(str(r['Date']))
		temp.append(float(r['Temp']))

	plt.plot(dates, temp)
	plt.ylabel('Temperature')
	plt.xlabel('Date')
	plt.title(label = 'Average temperature', loc='center')
	plt.show()
