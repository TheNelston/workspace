import sys
arglen = len(sys.argv)
l = sys.argv
i = 1
while i < arglen:
	sort_key = lambda s: (-len(s), s)
	l.sort(key=sort_key)
	print(l[i])
	i += 1