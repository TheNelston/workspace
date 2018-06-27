#!/usr/bin/env python3
#By nmu
#This program prints out every other letter capitalized, replaces all capped vowels with *, and checks for balanced parentheses
import math
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
	if len(s[1::])%2 == 1:
		print("Median: {}".format(s[len(((int(s[1::]))-1))/2]))
	else:
		print("")
def main(argv):
	min_func(argv)
	max_func(argv)
	mean_func(argv)
	median_func(argv)

main(sys.argv)