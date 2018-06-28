s = ["elephant",1,2,3,4,5,6]
occurlist = []
for number in s[1::]:
	occurlist.append(str(s.count(number)))

if "".join(occurlist) == "1"*len(s[1::]):
	print("no mode")
else:
	print("mode!")