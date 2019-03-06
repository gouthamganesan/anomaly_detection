import random
import csv

with open('dataset.csv','w') as data:
	writer = csv.writer(data)
	writer.writerows([['Latitude','Longitude','Time','Class']])
	for i in range(0,300000):
		temp = []
		lat = 12.82 + random.random() * 0.32
		lon = 79.93 + random.random() * 0.33
		time = int(random.random() * 43200)
		temp.append([lat, lon, time, 0])
		print(temp)
		writer.writerows(temp)
	for i in range(0,30000):
		temp = []
		lat = 12.82 + random.random() * 0.32
		lon = 79.93 + random.random() * 0.33
		time = int(43200 + random.random() * 43200)
		temp.append([lat, lon, time, 0])
		print(temp)
		writer.writerows(temp)
	for i in range(0,30000):
		temp = []
		lat = random.random() * 25
		lon = random.random() * 50
		time = int(random.random() * 43200)
		temp.append([lat, lon, time, 0])
		writer.writerows(temp)
	for i in range(0,3000):
		temp = []
		lat = random.random() * 25
		lon = random.random() * 50
		time = int(43200 + random.random() * 43200)
		temp.append([lat, lon, time, 1])
		writer.writerows(temp)