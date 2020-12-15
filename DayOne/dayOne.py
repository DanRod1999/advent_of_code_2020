#!/usr/bin/env python3


dataInt = []
with open('inputDayOne') as f:
	for line in f:
		dataInt.append(int(line))

dataInt.sort()
listLen = len(dataInt)
start = 0
end = listLen-1
for x in dataInt:
	if dataInt[start]+dataInt[end] < 2020:
		start = start + 1
	if dataInt[start]+dataInt[end] > 2020:
		end = end - 1
	if dataInt[start]+dataInt[end] == 2020:
		print(dataInt[start]*dataInt[end])


start = 0
end = listLen-1
i = 0
for x in dataInt:
	for y in dataInt:
		for z in dataInt:
			if (x + y + z) == 2020:
				print(x*y*z)
