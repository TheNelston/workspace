#!/usr/bin/env python3
#By nmu
#This program displays 
import collections
import re
import ast
h = open('condensedcm.txt')
classmates = h.read().split(',')
appendfnlist = classmates
appendlnlist = classmates
h.close()
firstnames = []
lastnames = []
for name in classmates[1::]:
	if classmates.index(name)%2 == 1:
		firstnames.append(name)
	else:
		lastnames.append(name)
lnoccurcount = collections.Counter()
for lastname in lastnames:
	lnoccurcount[lastname] += 1
commonlnames = []
commlnames = {}
commlnamefnames = []
for word in lnoccurcount:
	if lnoccurcount[word] > 1:
		commonlnames.append(word)
for name in classmates[1::]:
	if name in commonlnames:
		commlnamefnames.append(classmates[(classmates.index(name)-1)])
testlistz = []
for name in commonlnames:
	l = []
	i = 0
	while i < lnoccurcount[name]:
		l.append(appendlnlist[appendlnlist.index(name)-1])
		appendlnlist.remove(appendlnlist[appendlnlist.index(name)])
		i += 1
	lncombos = str(l)
	testlistz.append("'{}':{}".format(name,lncombos))
mappedlnames = ast.literal_eval(", ".join(testlistz).replace("['Tony', 'Tony']", "['Tony', 'Tony']}").replace("'Brill':","{'Brill':"))
for name in commonlnames[1::]:
	print(("{} ({}): {}").format(name, lnoccurcount[name], mappedlnames[name]))