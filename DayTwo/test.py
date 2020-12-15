import re

class passwordVal:
	def __init__(self, minPol, maxPol, char, val):
		self.minPol = minPol
		self.maxPol = maxPol
		self.char = char
		self.val = val

passwords = []
with open('inputDayTwo') as f:
	for line in f:
		x = re.split('-|: | |\n',line)
		data = passwordVal(int(x[0]),int(x[1]),x[2],x[3])
		passwords.append(data)

validPass = 0
for password in passwords:
	count = 0
	for i in (range(len(password.val))):
		if password.val[i] == password.char:
			count+=1
	
	if count >= password.minPol	and count <= password.maxPol:
		validPass+=1

print("Valid Passwords pt1: ",validPass)

validPass = 0
for password in passwords:
	if password.val[password.minPol-1] == password.char or password.val[password.maxPol-1] == password.char:
		if password.val[password.minPol-1] != password.val[password.maxPol-1]:
			validPass+=1

print("Valid Passwords pt2: ",validPass)
