from generate import *
import _tkinter
import tkinter as tk

def draw(sensor, height, top, cvs):
        
        color=("#FFB6C1", "#FFC0CB", "#DC143C", "#FFF0F5", "#DB7093", "#FF69B4", "#FF1493", "#C71585", "#DA70D6", "#D8BFD8", "#DDA0DD", "#EE82EE", "#FF00FF")
        for i in range(num):
                cvs.create_oval((sensor[i][0]-radius)*300/length, (height-radius)*300/length, (sensor[i][0]+radius)*300/length, (height+radius)*300/length, fill = color[i] )
        
        

top = tk.Tk()
cvs = tk.Canvas(top, width = 300, height = 800)
cvs.pack()
sensor = sorted(sensor, key=lambda sensor : sensor[0])
for i in range(num):
	print(sensor[i])

draw(sensor, radius, top, cvs)
overlap = []
gap = []

diameter = radius*2

if sensor[0][0]<radius:
	overlap.append([round(radius - sensor[0][0], 2),-1,0])
if sensor[0][0]>radius:
	gap.append([round(sensor[0][0] - radius, 2), -1, 0, -1])
for i in range(num - 1):
	if(sensor[i + 1][0] - sensor[i][0]<diameter):
		overlap.append([round(diameter - (sensor[i + 1][0] - sensor[i][0]), 2), i, i + 1])
	if(sensor[i + 1][0] - sensor[i][0]>diameter):
		gap.append([round((sensor[i + 1][0] - sensor[i][0]) - diameter, 2), i, i + 1, len(overlap) - 1])

if sensor[num - 1][0]>length - radius:
	overlap.append([round(sensor[num - 1][0] + radius - length, 2), num - 1, num])
if sensor[num - 1][0]<length - radius:
	gap.append([round(length - radius - sensor[num - 1][0], 2), num - 1, num, len(overlap) - 1])

print('\n')

for i in range(len(overlap)):
	print(overlap[i])

print('\n')

for i in range(len(gap)):
	print(gap[i])



l = len(gap)

print(l)

newSensor = [list(t) for t in sensor]
count = 0

for i in range(l):
 	while gap[i][0]>0:

 		leftCost = length * num
 		jl = gap[i][3]
 		while jl>-1 and overlap[jl][0]<=0:
	 		jl = jl - 1
	 	if(jl>-1):
	 		leftCover = min(gap[i][0], overlap[jl][0])
 			leftCost = (gap[i][1] - overlap[jl][2] + 1) * leftCover
 		print(gap[i][0], "L:", leftCost, jl)

 		rightCost = length * num
 		jr = gap[i][3] + 1
 		while jr<len(overlap) and overlap[jr][0]<=0:
 			jr = jr + 1
 		if(jr<len(overlap)):
 			rightCover = min(gap[i][0], overlap[jr][0])
 			rightCost = (overlap[jr][1] - gap[i][2] + 1) * rightCover
 		print(gap[i][0], "R:", rightCost, jr)

 		if(leftCost < rightCost):
 			print("Choose Left.")
 			gap[i][0] = gap[i][0] - leftCover
 			overlap[jl][0] = overlap[jl][0] - leftCover
 			for k in range(overlap[jl][2], gap[i][1] + 1):
 				newSensor[k][0] = round(newSensor[k][0] + leftCover, 2)
 		if(leftCost > rightCost):
 			print("Choose Right.")
 			gap[i][0] = gap[i][0] - rightCover
 			overlap[jr][0] = overlap[jr][0] - rightCover
 			for k in range(gap[i][2], overlap[jr][1] + 1):
 				newSensor[k][0] = round(newSensor[k][0] - rightCover, 2)
 		draw(newSensor, radius * 2 * (count + 1) + radius, top, cvs)
 		tmp = input("press any key to continue")
 		count = count + 1

 	print("-------------")
 	print(newSensor)
 	
 	print("-------------")
	 

print(sensor)
tmp = input("press any key to exit")
top.destroy()
top.mainloop()
exit()
