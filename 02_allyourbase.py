def binary():
	binarynum = input("What base-10 number would you like to conver to binary?: ")
	binarynum = int(binarynum)
	testlist = []
	while binarynum != 1:
	  if binarynum == 0:
	    break
	  testnum = binarynum % 2
	  binarynum = int(binarynum / 2)
	  testlist.append(testnum)
	testnum = binarynum % 2
	binarynum = int(binarynum / 2)
	testlist.append(testnum)
	testlistflip = (((str(testlist[::-1]).replace(", ","")).replace("[", "")).replace("]", ""))
	print(testlistflip)
def main():
	binary()
main()
