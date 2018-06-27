s = ["1","2","3","4","56"]
x = []
for number in s:
	x.append(list(number))
y = []
for element in x:
	y.append(int("".join(element)))
print((sum(y))/(len(y)))
#for letter in x:
	#print(int(letter))