#!/usr/bin/env python3
#By nmu
#This program prints out every other letter capitalized, replaces all capped vowels with *, and checks for balanced parentheses
import sys
import re

def do_all_this(s):
	string = " ".join(sys.argv[1::])
	x = []
	i = 0
	while i < len(string):
		if i%2 == 1:
			x.append(str.upper(string[i]))
		else:
			x.append(string[i])
		i += 1
	print("".join(x))
	a = "".join(x)
	vowrepl = re.sub(r'[AEIOU]','*', a)
	print(vowrepl)
	openpara = vowrepl.count("(")
	closepara = vowrepl.count(")")
	if openpara == closepara:
		print("Balanced? True")
	else:
		print("Balanced? False")

def main(argv):
	do_all_this(argv)

main(sys.argv)