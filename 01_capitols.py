#!/usr/bin/env python3
#By nmu
#This program displays the capital of an inputted state. Requires capitols.txt and capitolsreform.txt to run.
h = open('capitolsreform.txt')
statesandcaps = h.read().split(',')
h.close()
states = []
capitals = []
for place in statesandcaps[1::]:
	if statesandcaps.index(place)%2 == 1:
		states.append(place)
	else:
		capitals.append(place)
statemapcap = dict(zip(states,capitals))
i = 0
while i < i+1:
	inputted = input("Ready: ")
	if inputted in states:
		print(statemapcap[inputted])
		i += 1
	elif inputted == "Done":
		break
	else:
		print("nil")
		i += 1
