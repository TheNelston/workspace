#!/usr/bin/env python3
#By nmu
#This program displays your text in rainbow colors! 
import sys
def write_colorful_text():
	print( '\x1b[1;31;40m R \x1b[0m', end="")
	print( '\x1b[1;32;40m A \x1b[0m', end="")
	print( '\x1b[1;33;40m I \x1b[0m', end="")
	print( '\x1b[1;34;40m N \x1b[0m', end="")
	print( '\x1b[1;35;40m B \x1b[0m', end="")
	print( '\x1b[1;36;40m O \x1b[0m', end="")
	print( '\x1b[1;37;40m W \x1b[0m')
def main(argv):
	write_colorful_text()
main(sys.argv)