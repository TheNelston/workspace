#!/usr/bin/env python3
#By nmu
#This program displays the capital of an inputted state. Requires capitols.txt and capitolsreform.txt to run.
f = open('capitols.txt')
h = open('capitolsreform.txt')
d = dict(x.rstrip().split(None, 1) for x in f)
statesandcaps = h.read().split(',')
f.close()
h.close()
states = []
for state in statesandcaps:
	if statesandcaps.index(state)%2 == 1:
		states.append(state)
	else:
		continue
i = 0
while i < i+1:
	inputted = input("Ready: ")
	if inputted in states:
		print(d[inputted])
		i += 1
	elif inputted == "Done":
		break
	else:
		print("nil")
		i += 1
