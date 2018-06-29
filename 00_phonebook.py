#!/usr/bin/env python3
#By nmu
#This program displays 
import collections
import re
f = open('classmates.txt')
h = open('condensedcm.txt')
d = dict(x.rstrip().split(None, 1) for x in f)
classmates = h.read().split(',')
f.close()
h.close()
firstnames = []
lastnames = []
for name in classmates[1::]:
	if classmates.index(name)%2 == 1:
		firstnames.append(name)
	else:
		lastnames.append(name)
fnoccurcount = collections.Counter()
for firstname in firstnames:
	fnoccurcount[firstname] += 1
commonfnames = []
commfnames = {}
commfnamelnames = []
for word in fnoccurcount:
	if fnoccurcount[word] > 1:
		commonfnames.append(word)
for name in classmates[1::]:
	if name in commonfnames:
		commfnamelnames.append(classmates[(classmates.index(name)+1)])
for name in commonfnames:
	l = []
	i = 0
	while i < fnoccurcount[name]:
		l.append(classmates[classmates.index(name)+1])
		classmates.remove(classmates[classmates.index(name)])
		i += 1
	commfnames.update(dict.fromkeys(l, name))
for key in commfnames.keys():
  print(key)
#print(commfnames['Rohan'])
#print(commfnames)
#myDict = {}
#myDict.update(dict.fromkeys(['a', 'b', 'c'], 10))
#myDict.update(dict.fromkeys(['b', 'e'], 20))