#!/usr/bin/env python3
#By nmu
#This program prints out every other letter capitalized, replaces all capped vowels with *, and checks for balanced parentheses
import sys
import re
def alternate_case(s):
	alllower = list(map(str.lower, s))
	altup = list(map(str.upper, s[::2]))
	altupstr = str(altup)
def vowel_repl(s):
	vowrepl = re.sub(r'[AEIOU]','*', s)
	print(vowrepl)