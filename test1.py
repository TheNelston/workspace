import sys
import re
s = "i live only to suffer!"
x = []
i = 0
while i < len(s):
	if i%2 == 1:
		x.append(str.upper(s[i]))
	else:
		x.append(s[i])
	i += 1
vowrepl = re.sub(r'[AEIOU]','*', ''.join(x))
print(vowrepl)