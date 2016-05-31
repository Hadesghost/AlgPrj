import random

file = open('Data.txt', 'w')
length = round(float(input("input the length will be covered.")),2)
file.write(str(length)+'\n')
num = int(input("input the number of sensors."))
file.write(str(num)+'\n')
radius = round(float(input("input the radius of sensor.")),2)
file.write(str(radius)+'\n')
print(length, num, radius)

sensor = []
for i in range(num):
	sensor.append((round(random.uniform(0,length),2),round(random.uniform(0,length),2)))
#	print(sensor[i])
	file.write(str(sensor[i])+'\n')

file.close()