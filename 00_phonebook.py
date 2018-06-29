#!/usr/bin/env python3
#By nmu
#This program displays all repeating first names and last names with repetitions and the corresponding individuals.
#Requires file condensedcm.txt to run.
import collections
import re
import ast

def first_name_rep():
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
	fnoccurcount = collections.Counter()
	for firstname in firstnames:
		fnoccurcount[firstname] += 1
	commonfnames = []
	commfnamelnames = []
	for word in fnoccurcount:
		if fnoccurcount[word] > 1:
			commonfnames.append(word)
	for name in classmates[1::]:
		if name in commonfnames:
			commfnamelnames.append(classmates[(classmates.index(name)+1)])
	testlist = []
	for name in commonfnames:
		l = []
		i = 0
		while i < fnoccurcount[name]:
			l.append(appendfnlist[appendfnlist.index(name)+1])
			appendfnlist.remove(appendfnlist[appendfnlist.index(name)])
			i += 1
		fncombos = str(l)
		testlist.append("'{}':{}".format(name,fncombos))
	mappedfnames = ast.literal_eval((", ".join(testlist)).replace("'Warren']", "'Warren']}").replace("'Kevin':[", "{'Kevin':["))
	print("Repeat first names: ")
	for name in commonfnames[1::]:
		print(("{} ({}): {}").format(name, fnoccurcount[name], mappedfnames[name]))

def last_name_rep():
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
	print("Repeat last names:")
	for name in commonlnames[1::]:
		print(("{} ({}): {}").format(name, lnoccurcount[name], mappedlnames[name]))

def main():
	first_name_rep()
	last_name_rep()

main()