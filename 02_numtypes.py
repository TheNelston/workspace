import sys
dividend = int(sys.argv[1])
divisor = int(sys.argv[2])
q, r = divmod(dividend, divisor)
print("The quotient of {} divided by".format(dividend), "{} is:".format(divisor), "{},".format(q), "and the remainder is:", "{}.".format(r))
a = 10
b = 10.99
c = 4+3j
d = 2^50
l = [a,b,c,d]
for num in l:
	if isinstance(num, int) == True:
		print(("{} is an integer").format(num))
	elif isinstance(num, float) == True:
		print(("{} is a floating point number").format(num))
	elif isinstance(num, complex) == True:
		numb = str(num)
		s = numb.replace("(", "") 
		f = s.replace(")", "")
		print(("{} is a complex number").format(f))
	elif isinstance(num, long) == True:
		print(("{} is a long integer").format(num))
	else:
		print("This is literally impossible...")