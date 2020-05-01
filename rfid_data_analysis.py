import matplotlib.pyplot as plt
import csv

def analyze():
	file = open('rfidno_data.csv', 'r')
	reader = csv.DictReader(file)

	pos = 0
	neg = 0

	for r in reader:
		if int(r['Status']) == 1:
			pos = pos + 1

		elif int(r['Status']) == 0:
			neg = neg + 1

	sizes = [pos, neg]
	labels = ['Successful', 'Unsuccessful']
	colors = ['green', 'red']

	plt.pie(sizes, labels=labels, colors=colors, autopct = '%1.1f%%')
	plt.title('RFID Authentication Analysis')
	plt.axis('equal')
	plt.show()