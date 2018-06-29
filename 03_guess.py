#!/usr/bin/env python3
#By nmu
#This program plays a simple guessing game!
import random
import string

def play_guess(): 
	wordlist = ["broke", "annoy", "crack", "marry", "night", "zebra", "crazy", "apple"]
	randomword = random.choice(wordlist)
	print("The first letter of the word is: {}".format((list(randomword))[0]))
	i = 0
	while i < 10:
		inputtedword = input("GUESS: ")
		if (list(randomword))[0] == (list(inputtedword))[0]:
			if len(inputtedword) == 5:
				if len(inputtedword) > 1:
					if inputtedword == randomword:
						print("You got the word correct!")
						break
					else:
						print("You have {} guesses left!".format(9-i))
				else:
					print("You wasted a guess!")
					i += 1
			else:
				print("0, 1, 2, 3, 4 that's how we count to five!")
				i +=1
		else:
			print("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
			i += 1
	print("The correct word was: {}".format(randomword))
	if i >= 10:
		print("You didn't get the word :c")

def main():
	play_guess()

main()