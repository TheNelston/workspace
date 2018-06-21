import string
print("What word or phrase do you want to check for symmetry?")
inputted = input(">")
removepunct = str.maketrans('', '', string.punctuation)
nopunct = inputted.translate(removepunct)
removespace = str.maketrans('', '', string.whitespace)
nocaps = nopunct.translate(removespace)
inputstring = str.lower(nocaps)
backwords = inputstring[::-1]
if backwords == inputstring:
	print("It's a palindrome :D")
else:
	print("Not a palindrome :c")