a = [False,True,True,None,True,None,None,False,False,None,True,False]
b = ["or","or","or","==","!=","==","and","==","!=","and","!=","and"]
c = [False,False,None,None,True,True,False,True,None,False,True,None]
i = 0
while i < 12:
	if bool("{}".format(a[i]) + " " + "{}".format(b[i]) + " " + "{}".format(c[i])) == True:
		print("{}".format(a[i]) + " " + "{}".format(b[i]) + " " + "{}".format(c[i]) + " => True")
	elif bool("{}".format(a[i]) + " " + "{}".format(b[i]) + " " + "{}".format(c[i])) == False:
		print("{}".format(a[i]) + " " + "{}".format(b[i]) + " " + "{}".format(c[i]) + " => False")
	else:
		print("This is not physically possible.")
	i += 1