import sys
import re
s = " ".join(sys.argv[1::])
x = []
i = 0
while i < len(s):
	if i%2 == 1:
		x.append(str.upper(s[i]))
	else:
		x.append(s[i])
	i += 1
print(''.join(x))