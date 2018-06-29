#!/usr/bin/env python3
#By nmu
#This program outputs the minimum/maximum value, mean, median, mode, and range of a command line input of numbers
import sys

def min_func(s):
	minval = min(s[1::])
	print("Min: {}".format(minval))

def max_func(s):
	maxval = max(s[1::])
	print("Max: {}".format(maxval))

def mean_func(s):
	x = []
	for number in s[1::]:
		x.append(list(number))
	y = []
	for element in x:
		y.append(int("".join(element)))
	print("Mean: {}".format((sum(y))/(len(y))))

def median_func(s):
	orderedlist = sorted(s[1::])
	orderlen = len(orderedlist)
	quot, rem = divmod(orderlen, 2)
	if rem:
		print("Median: {}".format(orderedlist[quot]))
	else:
		print("Median: {}".format(((int(s[quot]))+(int(s[-quot])))/2.0))

def mode_func(s):
	occurlist = []
	for number in s[1::]:
		occurlist.append(str(s.count(number)))
	occurlistones = []
	for x in occurlist:
		occurlistones.append(str(int(int(x)/(int(max(set(occurlist), key=occurlist.count))))))
	if "".join(occurlistones) == "1"*len(s[1::]):
		print("Mode: N/A")
	else:
		print("Mode: {}".format(max(set(s), key=s.count)))

def range_func(s):
	print("Range: {}".format(int(max(s[1::]))-int(min(s[1::]))))

def main(argv):
	min_func(argv)
	max_func(argv)     
	mean_func(argv)
	median_func(argv)
	mode_func(argv)
	range_func(argv)

main(sys.argv)