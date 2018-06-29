import sys
s = sys.argv
w = []
xd = []
for word in s[1::]:
	w.append(list(word))
for words in w:
	z = []
	i = 0
	for letter in words:
		xyz = []
		while i < len(words):
			if i%2 == 1:
				xyz.append(letter.upper())
			else:
				xyz.append(letter.lower())
			i += 1
		z.append("".join(xyz))
	xd.append("".join(z))
print(" ".join(xd))
#	x = "".join(words)
#	xd.append(x)
#print(" ".join(xd))
#for aword in w:
#	for letter in aword:
#		z = []
#		i = 0
#		while i < len(s):
#			if  i%2 == 1:
#				z.append(letter.upper())
#			else:
#				z.append(letter.lower())
#			i += 1
#		xd.append(z)		
#print(xd)