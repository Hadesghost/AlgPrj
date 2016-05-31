from generate import *
sensor = sorted(sensor, key=lambda sensor : sensor[0])
for i in range(num):
	print(sensor[i])

overlap = []
gap = []

diameter = radius*2

# if sensor[0][0]<radius:
# 	overlap.append(round(radius - sensor[0][0], 2))
if sensor[0][0]>radius:
	gap.append((round(sensor[0][0] - radius, 2), -1, 0))
for i in range(num - 1):
	# if(sensor[i + 1][0] - sensor[i][0]<diameter):
	# 	overlap.append(round(diameter - (sensor[i + 1][0] - sensor[i][0]), 2))
	if(sensor[i + 1][0] - sensor[i][0]>diameter):
		gap.append((round((sensor[i + 1][0] - sensor[i][0]) - diameter, 2), i, i + 1))

# for i in range(len(overlap)):
# 	print(overlap[i])

print('\n')

for i in range(len(gap)):
	print(gap[i])

l = len(gap)
