import sys
import shutil
import random
columns = shutil.get_terminal_size().columns
termnames = ["Now {}{} less illegal!".format(random.randint(0,100), "%"),"Hustle or be broke!","An almost perfect embodiment of frustration!","Get rich slow!", "Does anyone read these?"]
sys.stdout.write("\x1b]2;Investables: {}\x07".format(termnames[random.randint(0,4)]))
print("Welcome to Investables: The Quest for Money!".center(columns))
input("Press enter to begin.".center(columns))
def exit():
	print("Thanks for playing!\n")
	quit()
def start():
	i = 0
	while i == i:
		print("Enter s to start the game, t to run through a tutorial, and q to quit the game.".center(columns))
		startint = input("> ")
		if startint == "s":
			game()
		elif startint == "t":
			tutorial()
		elif startint == "q":
			exit()
		else:
			print("That's not a valid input... try again!")
			i += 1
def tutorial():
	print("This feature hs not been added yet! Sorry :(")
	start()
def game():
	backtomain = input("Welcome to the world of Investables! Press enter to begin the game, or input 'quit' to return to the main menu.".center(columns))
	if backtomain == "quit":
		start()
	complist = ["GroFast & Co. (agrc)", "BerryGood Inc. (agrc)", "AgVest Inc. (agrc)", 
	"LiteSpd Technologies & Co. (tech)", "Ping Inc. (tech)", "TechVest Inc. (tech)",
	"QuickBurger Co. (serv)", "OnDemTV Inc. (serv)", "SerVest Inc (serv)",
	"EZHome Co. (cons)", "BuildItUp Inc. (cons)", "ConVest Inc. (cons)"]
	agrcstocks = [0,0,0]
	techstocks = [0,0,0]
	servstocks = [0,0,0]
	consstocks = [0,0,0]
	agrcmarketvalues = [50.00,75.00,60.00]
	techmarketvalues = [50.00,75.00,60.00]
	servmarketvalues = [50.00,75.00,60.00]
	consmarketvalues = [50.00,75.00,60.00]
	money = [1000.00]
	turns = 0
	eventnum = 0
	disupplim = 1
	disasternum = -1
	i = 0
	while i == i:
		i = 0
		while i == i:
			disasternum = -1
			if turns >= 2:
				disasterchance = random.randint(1,disupplim)
				if disasterchance == 1:
					disaster = ["DISASTER!!! Locusts develop at an unbelievable pace, wiping out 80 percent of the world's crops.",
								"DISASTER!!! A powerful solar flare has struck Earth, frying the majority of the world's electronics.",
								"DISASTER!!! CloudNET AI systems have been ransacked by angry unemployed service workers; service companies are scrambling to meet demand while all service systems are down.",
								"DISASTER!!! A global effort led by environmentalists to destroy all heavy machinery has been successful; 95 percent of all construction equipment are completely totaled."]
					disnum = random.randint(0,3)
					disname = disaster[disnum]
					print("")
					input("Emergency Broadcast:".center(columns))
					input("{}".format(disname).center(columns))
					if disnum == 0:
						agrc1 = (random.uniform(0.3, 0.65))
						agrc2 = (random.uniform(0.4, 0.75))
						agrc3 = (random.uniform(0.6, 0.9))
						tech1 = (random.uniform(0.8, 1.00))
						tech2 = (random.uniform(0.8, 1.00))
						tech3 = (random.uniform(0.8, 1.00))
						serv1 = (random.uniform(0.8, 1.00))
						serv2 = (random.uniform(0.8, 1.00))
						serv3 = (random.uniform(0.8, 1.00))
						cons1 = (random.uniform(0.8, 1.00))
						cons2 = (random.uniform(0.8, 1.00))
						cons3 = (random.uniform(0.8, 1.00))
						agrcmarketvalues = [agrcmarketvalues[0]*agrc1,agrcmarketvalues[1]*agrc2,agrcmarketvalues[2]*agrc3]
						techmarketvalues = [techmarketvalues[0]*tech1,techmarketvalues[1]*tech2,techmarketvalues[2]*tech3]
						servmarketvalues = [servmarketvalues[0]*serv1,servmarketvalues[1]*serv2,servmarketvalues[2]*serv3]
						consmarketvalues = [consmarketvalues[0]*cons1,consmarketvalues[1]*cons2,consmarketvalues[2]*cons3]
						sharerise = {"GroFast & Co. (agrc)":agrc1, "BerryGood Inc. (agrc)":agrc2, "AgVest Inc. (agrc)":agrc3, 
						"LiteSpd Technologies & Co. (tech)":tech1, "Ping Inc. (tech)":tech2, "TechVest Inc. (tech)":tech3,
						"QuickBurger Co. (serv)":serv1, "OnDemTV Inc. (serv)":serv2, "SerVest Inc (serv)":serv3,
						"EZHome Co. (cons)":cons1, "BuildItUp Inc. (cons)":cons2, "ConVest Inc. (cons)":cons3}
						for company in complist:
							if sharerise[company] < 1:
								print(("{}'s stock value has fallen {}%".format(company,(100-(sharerise[company]*100)))).center(columns))
							else:
								print(("{}'s stock value has risen {}%".format(company,((sharerise[company]*100)-100))).center(columns))
					if disnum == 1:
						agrc1 = (random.uniform(0.8, 1.00))
						agrc2 = (random.uniform(0.8, 1.00))
						agrc3 = (random.uniform(0.8, 1.00))
						tech1 = (random.uniform(0.3, 0.65))
						tech2 = (random.uniform(0.4, 0.75))
						tech3 = (random.uniform(0.6, 0.9))
						serv1 = (random.uniform(0.8, 1.00))
						serv2 = (random.uniform(0.8, 1.00))
						serv3 = (random.uniform(0.8, 1.00))
						cons1 = (random.uniform(0.8, 1.00))
						cons2 = (random.uniform(0.8, 1.00))
						cons3 = (random.uniform(0.8, 1.00))
						agrcmarketvalues = [agrcmarketvalues[0]*agrc1,agrcmarketvalues[1]*agrc2,agrcmarketvalues[2]*agrc3]
						techmarketvalues = [techmarketvalues[0]*tech1,techmarketvalues[1]*tech2,techmarketvalues[2]*tech3]
						servmarketvalues = [servmarketvalues[0]*serv1,servmarketvalues[1]*serv2,servmarketvalues[2]*serv3]
						consmarketvalues = [consmarketvalues[0]*cons1,consmarketvalues[1]*cons2,consmarketvalues[2]*cons3]
						sharerise = {"GroFast & Co. (agrc)":agrc1, "BerryGood Inc. (agrc)":agrc2, "AgVest Inc. (agrc)":agrc3, 
						"LiteSpd Technologies & Co. (tech)":tech1, "Ping Inc. (tech)":tech2, "TechVest Inc. (tech)":tech3,
						"QuickBurger Co. (serv)":serv1, "OnDemTV Inc. (serv)":serv2, "SerVest Inc (serv)":serv3,
						"EZHome Co. (cons)":cons1, "BuildItUp Inc. (cons)":cons2, "ConVest Inc. (cons)":cons3}
						for company in complist:
							if sharerise[company] < 1:
								print(("{}'s stock value has fallen {}%".format(company,(100-(sharerise[company]*100)))).center(columns))
							else:
								print(("{}'s stock value has risen {}%".format(company,((sharerise[company]*100)-100))).center(columns))
					if disnum == 2:
						agrc1 = (random.uniform(0.8, 1.00))
						agrc2 = (random.uniform(0.8, 1.00))
						agrc3 = (random.uniform(0.8, 1.00))
						tech1 = (random.uniform(0.8, 1.00))
						tech2 = (random.uniform(0.8, 1.00))
						tech3 = (random.uniform(0.8, 1.00))
						serv1 = (random.uniform(0.3, 0.65))
						serv2 = (random.uniform(0.4, 0.75))
						serv3 = (random.uniform(0.6, 0.9))
						cons1 = (random.uniform(0.8, 1.00))
						cons2 = (random.uniform(0.8, 1.00))
						cons3 = (random.uniform(0.8, 1.00))
						agrcmarketvalues = [agrcmarketvalues[0]*agrc1,agrcmarketvalues[1]*agrc2,agrcmarketvalues[2]*agrc3]
						techmarketvalues = [techmarketvalues[0]*tech1,techmarketvalues[1]*tech2,techmarketvalues[2]*tech3]
						servmarketvalues = [servmarketvalues[0]*serv1,servmarketvalues[1]*serv2,servmarketvalues[2]*serv3]
						consmarketvalues = [consmarketvalues[0]*cons1,consmarketvalues[1]*cons2,consmarketvalues[2]*cons3]
						sharerise = {"GroFast & Co. (agrc)":agrc1, "BerryGood Inc. (agrc)":agrc2, "AgVest Inc. (agrc)":agrc3, 
						"LiteSpd Technologies & Co. (tech)":tech1, "Ping Inc. (tech)":tech2, "TechVest Inc. (tech)":tech3,
						"QuickBurger Co. (serv)":serv1, "OnDemTV Inc. (serv)":serv2, "SerVest Inc (serv)":serv3,
						"EZHome Co. (cons)":cons1, "BuildItUp Inc. (cons)":cons2, "ConVest Inc. (cons)":cons3}
						for company in complist:
							if sharerise[company] < 1:
								print(("{}'s stock value has fallen {}%".format(company,(100-(sharerise[company]*100)))).center(columns))
							else:
								print(("{}'s stock value has risen {}%".format(company,((sharerise[company]*100)-100))).center(columns))
					if disnum == 3:
						agrc1 = (random.uniform(0.8, 1.00))
						agrc2 = (random.uniform(0.8, 1.00))
						agrc3 = (random.uniform(0.8, 1.00))
						tech1 = (random.uniform(0.8, 1.00))
						tech2 = (random.uniform(0.8, 1.00))
						tech3 = (random.uniform(0.8, 1.00))
						serv1 = (random.uniform(0.8, 1.00))
						serv2 = (random.uniform(0.8, 1.00))
						serv3 = (random.uniform(0.8, 1.00))
						cons1 = (random.uniform(0.3, 0.65))
						cons2 = (random.uniform(0.4, 0.75))
						cons3 = (random.uniform(0.6, 0.9))
						agrcmarketvalues = [agrcmarketvalues[0]*agrc1,agrcmarketvalues[1]*agrc2,agrcmarketvalues[2]*agrc3]
						techmarketvalues = [techmarketvalues[0]*tech1,techmarketvalues[1]*tech2,techmarketvalues[2]*tech3]
						servmarketvalues = [servmarketvalues[0]*serv1,servmarketvalues[1]*serv2,servmarketvalues[2]*serv3]
						consmarketvalues = [consmarketvalues[0]*cons1,consmarketvalues[1]*cons2,consmarketvalues[2]*cons3]
						sharerise = {"GroFast & Co. (agrc)":agrc1, "BerryGood Inc. (agrc)":agrc2, "AgVest Inc. (agrc)":agrc3, 
						"LiteSpd Technologies & Co. (tech)":tech1, "Ping Inc. (tech)":tech2, "TechVest Inc. (tech)":tech3,
						"QuickBurger Co. (serv)":serv1, "OnDemTV Inc. (serv)":serv2, "SerVest Inc (serv)":serv3,
						"EZHome Co. (cons)":cons1, "BuildItUp Inc. (cons)":cons2, "ConVest Inc. (cons)":cons3}
						for company in complist:
							if sharerise[company] < 1:
								print(("{}'s stock value has fallen {}%".format(company,(100-(sharerise[company]*100)))).center(columns))
							else:
								print(("{}'s stock value has risen {}%".format(company,((sharerise[company]*100)-100))).center(columns))
			if turns > 0:
				events = ("Food shortage in the USA leads to increased wages for farmers.","STEM initiatives see a national surge in interest.","More teenagers are starting to take summer jobs in restaurants.","Housing demand skyrockets as the population booms.","Market is a bit shaky; analysts are unsure what to expect.")
				eventnum = random.randint(0,len(events)-1)
				print("")
				input(("{}".format(events[eventnum])).center(columns))
				print("")
			i = 0
			while i == i:	
				print("Turn: {}".format(turns).center(columns))
				print("")
				print("Balance:".center(columns))
				print(("${}".format(str(money[0]))).center(columns))
				print("")
				print("You currently have:".center(columns))
				print("")
				print("{} stocks in GroFast & Co. (agrc)".format(agrcstocks[0]).center(columns))
				print("{} stocks in BerryGood Inc. (agrc)".format(agrcstocks[1]).center(columns))
				print("{} stocks in AgVest Inc. (agrc)".format(agrcstocks[2]).center(columns))
				print("{} stocks in LiteSpd Technologies & Co. (tech)".format(techstocks[0]).center(columns))
				print("{} stocks in Ping Inc. (tech)".format(techstocks[1]).center(columns))
				print("{} stocks in TechVest Inc. (tech)".format(techstocks[2]).center(columns))
				print("{} stocks in QuickBurger Co. (serv)".format(servstocks[0]).center(columns))
				print("{} stocks in OnDemTV Inc. (serv)".format(servstocks[1]).center(columns))
				print("{} stocks in SerVest Inc. (serv)".format(servstocks[2]).center(columns))
				print("{} stocks in EZHome Co. (cons)".format(consstocks[0]).center(columns))
				print("{} stocks in BuildItUp Inc. (cons)".format(consstocks[1]).center(columns))
				print("{} stocks in ConVest Inc. (cons)".format(consstocks[2]).center(columns))
				print("")
				print("Current market values:".center(columns))
				print("")
				print("${} for a stock in Grofast & Co. (agrc)".format(agrcmarketvalues[0]).center(columns))
				print("${} for a stock in BerryGood Inc. (agrc)".format(agrcmarketvalues[1]).center(columns))
				print("${} for a stock in AgVest Inc. (agrc)".format(agrcmarketvalues[2]).center(columns))
				print("${} for a stock in LiteSpd Technologies & Co. (tech)".format(techmarketvalues[0]).center(columns))
				print("${} for a stock in Ping Inc. (tech)".format(techmarketvalues[1]).center(columns))
				print("${} for a stock in TechVest Inc. (tech)".format(techmarketvalues[2]).center(columns))
				print("${} for a stock in QuickBurger Co. (serv)".format(servmarketvalues[0]).center(columns))
				print("${} for a stock in OnDemTV Inc. (serv)".format(servmarketvalues[1]).center(columns))
				print("${} for a stock in SerVest Inc (serv)".format(servmarketvalues[2]).center(columns))
				print("${} for a stock in EZHome Co. (cons)".format(consmarketvalues[0]).center(columns))
				print("${} for a stock in BuildItUp Inc. (cons)".format(consmarketvalues[1]).center(columns))
				print("${} for a stock in ConVest Inc. (cons)".format(consmarketvalues[2]).center(columns))
				print("")
				print("Would you like to buy or sell stocks? Input done if you're done.")
				buyorsell = input("> ")
				if buyorsell == "buy":
					print("What industry would you like to buy stocks in? Input done if you're done.".center(columns))
					selection = input("> ")
					if selection == "agrc":
						i = 0
						while i == i:
							print("Balance:".center(columns))
							print(("${}".format(str(money[0]))).center(columns))
							print("")
							print("You currently have:".center(columns))
							print("")
							print("{} stocks in GroFast & Co. (1)".format(agrcstocks[0]).center(columns))
							print("{} stocks in BerryGood Inc. (2)".format(agrcstocks[1]).center(columns))
							print("{} stocks in AgVest Inc. (3)".format(agrcstocks[2]).center(columns))
							print("")
							print("Current market values:".center(columns))
							print("")
							print("${} for a stock in Grofast & Co.".format(agrcmarketvalues[0]).center(columns))
							print("${} for a stock in BerryGood Inc.".format(agrcmarketvalues[1]).center(columns))
							print("${} for a stock in AgVest Inc.".format(agrcmarketvalues[2]).center(columns))
							print("")
							print("Which company's stock would you like to buy (hint: the number in parentheses next to the company name is the number of that company)? Input done if you're done.".center(columns))
							inputted = input("> ")
							if inputted == "1":
								a = 0
								while a == a:
									print(("How many stocks would you like to buy? You can currently buy up to {} stocks.").format(int(money[0]/agrcmarketvalues[0])).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if num != 0:
												if (money[0]/(num*agrcmarketvalues[0])) >= 0:
													agrcstocks = [agrcstocks[0]+num,agrcstocks[1],agrcstocks[2]]
													money = [money[0]-(num*agrcmarketvalues[0])]
													break
												else:
													print("Oops, that's not a valid option! Please make sure you have enough to buy all that.")
													break
											else:
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "2":
								a = 0
								while a == a:
									print(("How many stocks would you like to buy? You can currently buy up to {} stocks.").format(int(money[0]/agrcmarketvalues[1])).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if num != 0:
												if (money[0]/(num*agrcmarketvalues[1])) >= 0:
													agrcstocks = [agrcstocks[0],agrcstocks[1]+num,agrcstocks[2]]
													money = [money[0]-(num*agrcmarketvalues[1])]
													break
												else:
													print("Oops, that's not a valid option! Please make sure you have enough to buy all that.")
													break
											else:
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "3":
								a = 0
								while a == a:
									print(("How many stocks would you like to buy? You can currently buy up to {} stocks.").format(int(money[0]/agrcmarketvalues[2])).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if num != 0:
												if (money[0]/(num*agrcmarketvalues[2])) >= 0:
													agrcstocks = [agrcstocks[0],agrcstocks[1],agrcstocks[2]+num]
													money = [money[0]-(num*agrcmarketvalues[2])]
													break
												else:
													print("Oops, that's not a valid option! Please make sure you have enough to buy all that.")
													break
											else:
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "done":
								break
							else:
								print("Oops, that's not a valid option! Pick either 1, 2, or 3, or input 'done'")
								i += 1
						i += 1
					elif selection == "tech":
						i = 0
						while i == i:
							print("Balance:".center(columns))
							print(("${}".format(str(money[0]))).center(columns))
							print("")
							print("You currently have:".center(columns))
							print("{} stocks in LiteSpd Technologies & Co. (1)".format(techstocks[0]).center(columns))
							print("{} stocks in Ping Inc. (2)".format(techstocks[1]).center(columns))
							print("{} stocks in TechVest Inc. (3)".format(techstocks[2]).center(columns))
							print("")
							print("Current market values:")
							print("${} for a stock in LiteSpd Technologies & Co.".format(techmarketvalues[0]).center(columns))
							print("${} for a stock in Ping Inc.".format(techmarketvalues[1]).center(columns))
							print("${} for a stock in TechVest Inc.".format(techmarketvalues[2]).center(columns))
							print("")
							print("Which company's stock would you like to buy (hint: the number in parentheses next to the company name is the number of that company)? Input done if you're done.")
							inputted = input("> ")
							if inputted == "1":
								a = 0
								while a == a:
									print(("How many stocks would you like to buy? You can currently buy up to {} stocks.").format(int(money[0]/techmarketvalues[0])).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if num != 0:
												if (money[0]/(num*techmarketvalues[0])) >= 0:
													techstocks = [techstocks[0]+num,techstocks[1],techstocks[2]]
													money = [money[0]-(num*techmarketvalues[0])]
													break
												else:
													print("Oops, that's not a valid option! Please make sure you have enough to buy all that.")
													break
											else:
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "2":
								a = 0
								while a == a:
									print(("How many stocks would you like to buy? You can currently buy up to {} stocks.").format(int(money[0]/techmarketvalues[1])).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if num != 0:
												if (money[0]/(num*techmarketvalues[1])) >= 0:
													techstocks = [techstocks[0],techstocks[1]+num,techstocks[2]]
													money = [money[0]-(num*techmarketvalues[1])]
													break
												else:
													print("Oops, that's not a valid option! Please make sure you have enough to buy all that.")
													break
											else:
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "3":
								a = 0
								while a == a:
									print(("How many stocks would you like to buy? You can currently buy up to {} stocks.").format(int(money[0]/techmarketvalues[2])).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if num != 0:
												if (money[0]/(num*techmarketvalues[2])) >= 0:
													techstocks = [techstocks[0],techstocks[1],techstocks[2]+num]
													money = [money[0]-(num*techmarketvalues[2])]
													break
												else:
													print("Oops, that's not a valid option! Please make sure you have enough to buy all that.")
													break
											else:
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "done":
								break
							else:
								print("Oops, that's not a valid option! Pick either 1, 2, or 3, or input 'done'")
								i += 1
						i += 1
					elif selection == "serv":
						i = 0
						while i == i:
							print("Balance:".center(columns))
							print(("${}".format(str(money[0]))).center(columns))
							print("")
							print("You currently have:".center(columns))
							print("{} stocks in QuickBurger Co. (1)".format(servstocks[0]).center(columns))
							print("{} stocks in OnDemTV Inc. (2)".format(servstocks[1]).center(columns))
							print("{} stocks in SerVest Inc. (3)".format(servstocks[2]).center(columns))
							print("")
							print("Current market values:".center(columns))
							print("${} for a stock in QuickBurger Co.".format(servmarketvalues[0]).center(columns))
							print("${} for a stock in OnDemTV Inc.".format(servmarketvalues[1]).center(columns))
							print("${} for a stock in SerVest Inc.".format(servmarketvalues[2]).center(columns))
							print("")
							print("Which company's stock would you like to buy (hint: the number in parentheses next to the company name is the number of that company)? Input done if you're done.")
							inputted = input("> ")
							if inputted == "1":
								a = 0
								while a == a:
									print(("How many stocks would you like to buy? You can currently buy up to {} stocks.").format(int(money[0]/servmarketvalues[0])).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if num != 0:
												if (money[0]/(num*servmarketvalues[0])) >= 0:
													servstocks = [servstocks[0]+num,servstocks[1],servstocks[2]]
													money = [money[0]-(num*servmarketvalues[0])]
													break
												else:
													print("Oops, that's not a valid option! Please make sure you have enough to buy all that.")
													break
											else:
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "2":
								a = 0
								while a == a:
									print(("How many stocks would you like to buy? You can currently buy up to {} stocks.").format(int(money[0]/servmarketvalues[1])).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if num != 0:	
												if (money[0]/(num*servmarketvalues[1])) >= 0:
													servstocks = [servstocks[0],servstocks[1]+num,servstocks[2]]
													money = [money[0]-(num*servmarketvalues[1])]
													break
												else:
													print("Oops, that's not a valid option! Please make sure you have enough to buy all that.")
													break
											else:
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "3":
								a = 0
								while a == a:
									print(("How many stocks would you like to buy? You can currently buy up to {} stocks.").format(int(money[0]/servmarketvalues[2])).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if num != 0:
												if (money[0]/(num*servmarketvalues[2])) >= 0:
													servstocks = [servstocks[0],servstocks[1],servstocks[2]+num]
													money = [money[0]-(num*servmarketvalues[2])]
													break
												else:
													print("Oops, that's not a valid option! Please make sure you have enough to buy all that.")
													break
											else:
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "done":
								break
							else:
								print("Oops, that's not a valid option! Pick either 1, 2, or 3, or input 'done'")
								i += 1
						i += 1
					elif selection == "cons":
						i = 0
						while i == i:
							print("Balance:".center(columns))
							print(("${}".format(str(money[0]))).center(columns))
							print("")
							print("You currently have:".center(columns))
							print("{} stocks in EZHome Co. (1)".format(consstocks[0]).center(columns))
							print("{} stocks in BuildItUp Inc. (2)".format(consstocks[1]).center(columns))
							print("{} stocks in ConVest Inc. (3)".format(consstocks[2]).center(columns))
							print("")
							print("Current market values:".center(columns))
							print("${} for a stock in EZHome Co.".format(consmarketvalues[0]).center(columns))
							print("${} for a stock in BuildItUp Inc.".format(consmarketvalues[1]).center(columns))
							print("${} for a stock in ConVest Inc.".format(consmarketvalues[2]).center(columns))
							print("")
							print("Which company's stock would you like to buy (hint: the number in parentheses next to the company name is the number of that company)? Input done if you're done.".center(columns))
							inputted = input("> ")
							if inputted == "1":
								a = 0
								while a == a:
									print(("How many stocks would you like to buy? You can currently buy up to {} stocks.").format(int(money[0]/consmarketvalues[0])).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if num != 0:
												if (money[0]/(num*consmarketvalues[0])) >= 0:
													consstocks = [consstocks[0]+num,consstocks[1],consstocks[2]]
													money = [money[0]-(num*consmarketvalues[0])]
													break
												else:
													print("Oops, that's not a valid option! Please make sure you have enough to buy all that.")
													break
											else:
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "2":
								a = 0
								while a == a:
									print(("How many stocks would you like to buy? You can currently buy up to {} stocks.").format(int(money[0]/consmarketvalues[1])).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if num != 0:
												if (money[0]/(num*consmarketvalues[1])) >= 0:
													consstocks = [consstocks[0],consstocks[1]+num,consstocks[2]]
													money = [money[0]-(num*consmarketvalues[1])]
													break
												else:
													print("Oops, that's not a valid option! Please make sure you have enough to buy all that.")
													break
											else:
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "3":
								a = 0
								while a == a:
									print(("How many stocks would you like to buy? You can currently buy up to {} stocks.").format(int(money[0]/consmarketvalues[2])).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if num != 0:
												if (money[0]/(num*consmarketvalues[2])) >= 0:
													consstocks = [consstocks[0],consstocks[1],consstocks[2]+num]
													money = [money[0]-(num*consmarketvalues[2])]
													break
												else:
													print("Oops, that's not a valid option! Please make sure you have enough to buy all that.")
													break
											else:
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "done":
								break
							else:
								print("Oops, that's not a valid option! Pick either 1, 2, or 3, or input 'done'")
								i += 1
						i += 1
					elif selection == "done":
						break
					else:
						print("Oops, that's not a valid option! Your choices are: agrc for Agriculture, tech for Technology, serv for Services, and cons for Construction. Alternatively, you can input 'done' to move on.")
						i += 1
				elif buyorsell == "sell":
					print("What industry would you like to sell stocks in? Input done if you're done.".center(columns))
					selection = input("> ")
					if selection == "agrc":
						i = 0
						while i == i:
							print("Balance:".center(columns))
							print(("${}".format(str(money[0]))).center(columns))
							print("")
							print("You currently have:".center(columns))
							print("")
							print("{} stocks in GroFast & Co. (1)".format(agrcstocks[0]).center(columns))
							print("{} stocks in BerryGood Inc. (2)".format(agrcstocks[1]).center(columns))
							print("{} stocks in AgVest Inc. (3)".format(agrcstocks[2]).center(columns))
							print("")
							print("Current market values:".center(columns))
							print("${} for a stock in Grofast & Co.".format(agrcmarketvalues[0]).center(columns))
							print("${} for a stock in BerryGood Inc.".format(agrcmarketvalues[1]).center(columns))
							print("${} for a stock in AgVest Inc.".format(agrcmarketvalues[2]).center(columns))
							print("")
							print("Which company's stock would you like to sell (hint: the number in parentheses next to the company name is the number of that company)? Input done if you're done.".center(columns))
							inputted = input("> ")
							if inputted == "1":
								a = 0
								while a == a:
									print("How many stocks would you like to sell? You can currently sell up to {} stocks.".format(agrcstocks[0]).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if agrcstocks[0]-num >= 0:
												agrcstocks = [agrcstocks[0]-num,agrcstocks[1],agrcstocks[2]]
												money = [money[0]+(num*agrcmarketvalues[0])]
												break
											else:
												print("Oops, that's not a valid option! Please make sure you have enough to sell.")
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "2":
								a = 0
								while a == a:
									print("How many stocks would you like to sell? You can currently sell up to {} stocks.".format(agrcstocks[1]).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:	
											if agrcstocks[1]-num >= 0:
												agrcstocks = [agrcstocks[0],agrcstocks[1]-num,agrcstocks[2]]
												money = [money[0]+(num*agrcmarketvalues[1])]
												break
											else:
												print("Oops, that's not a valid option! Please make sure you have enough to sell.")
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "3":
								a = 0
								while a == a:
									print("How many stocks would you like to sell? You can currently sell up to {} stocks.".format(agrcstocks[2]).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if agrcstocks[2]-num >= 0:
												agrcstocks = [agrcstocks[0],agrcstocks[1],agrcstocks[2]-num]
												money = [money[0]+(num*agrcmarketvalues[2])]
												break
											else:
												print("Oops, that's not a valid option! Please make sure you have enough to sell.")	
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "done":
								break
							else:
								print("Oops, that's not a valid option! Pick either 1, 2, or 3, or input 'done'")
								i += 1
						i += 1
					elif selection == "tech":
						i = 0
						while i == i:
							print("Balance:".center(columns))
							print(("${}".format(str(money[0]))).center(columns))
							print("")
							print("You currently have:".center(columns))
							print("{} stocks in LiteSpd Technologies & Co. (1)".format(techstocks[0]).center(columns))
							print("{} stocks in Ping Inc. (2)".format(techstocks[1]).center(columns))
							print("{} stocks in TechVest Inc. (3)".format(techstocks[2]).center(columns))
							print("")
							print("Current market values:".center(columns))
							print("${} for a stock in LiteSpd Technologies & Co.".format(techmarketvalues[0]).center(columns))
							print("${} for a stock in Ping Inc.".format(techmarketvalues[1]).center(columns))
							print("${} for a stock in TechVest Inc.".format(techmarketvalues[2]).center(columns))
							print("")
							print("Which company's stock would you like to sell (hint: the number in parentheses next to the company name is the number of that company)? Input done if you're done.")
							inputted = input("> ")
							if inputted == "1":
								a = 0
								while a == a:
									print("How many stocks would you like to sell? You can currently sell up to {} stocks.".format(techstocks[0]).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if techstocks[0]-num >= 0:
												techstocks = [techstocks[0]-num,techstocks[1],techstocks[2]]
												money = [money[0]+(num*techmarketvalues[0])]
												break
											else:
												print("Oops, that's not a valid option! Please make sure you have enough to sell.")	
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "2":
								a = 0
								while a == a:
									print("How many stocks would you like to sell? You can currently sell up to {} stocks.".format(techstocks[1]).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if techstocks[1]-num >= 0:
												techstocks = [techstocks[0],techstocks[1]-num,techstocks[2]]
												money = [money[0]+(num*techmarketvalues[1])]
												break
											else:
												print("Oops, that's not a valid option! Please make sure you have enough to sell.")	
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "3":
								a = 0
								while a == a:
									print("How many stocks would you like to sell? You can currently sell up to {} stocks.".format(techstocks[2]).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if techstocks[2]-num >= 0:
												techstocks = [techstocks[0],techstocks[1],techstocks[2]-num]
												money = [money[0]+(num*techmarketvalues[2])]
												break
											else:
												print("Oops, that's not a valid option! Please make sure you have enough to sell.")	
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "done":
								break
							else:
								print("Oops, that's not a valid option! Pick either 1, 2, or 3, or input 'done'")
								i += 1
						i += 1
					elif selection == "serv":
						i = 0
						while i == i:
							print("Balance:".center(columns))
							print(("${}".format(str(money[0]))).center(columns))
							print("")
							print("You currently have:".center(columns))
							print("{} stocks in QuickBurger Co. (1)".format(servstocks[0]).center(columns))
							print("{} stocks in OnDemTV Inc. (2)".format(servstocks[1]).center(columns))
							print("{} stocks in SerVest Inc. (3)".format(servstocks[2]).center(columns))
							print("")
							print("Current market values:".center(columns))
							print("${} for a stock in QuickBurger Co.".format(servmarketvalues[0]).center(columns))
							print("${} for a stock in OnDemTV Inc.".format(servmarketvalues[1]).center(columns))
							print("${} for a stock in SerVest Inc.".format(servmarketvalues[2]).center(columns))
							print("")
							print("Which company's stock would you like to sell (hint: the number in parentheses next to the company name is the number of that company)? Input done if you're done.")
							inputted = input("> ")
							if inputted == "1":
								a = 0
								while a == a:
									print("How many stocks would you like to sell? You can currently sell up to {} stocks.".format(servstocks[0]).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if servstocks[0]-num >= 0:
												servstocks = [servstocks[0]-num,servstocks[1],servstocks[2]]
												money = [money[0]+(num*servmarketvalues[0])]
												break
											else:
												print("Oops, that's not a valid option! Please make sure you have enough to sell.")	
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "2":
								a = 0
								while a == a:
									print("How many stocks would you like to sell? You can currently sell up to {} stocks.".format(servstocks[1]).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if servstocks[1]-num >= 0:
												servstocks = [servstocks[0],servstocks[1]-num,servstocks[2]]
												money = [money[0]+(num*servmarketvalues[1])]
												break
											else:
												print("Oops, that's not a valid option! Please make sure you have enough to sell.")	
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "3":
								a = 0
								while a == a:
									print("How many stocks would you like to sell? You can currently sell up to {} stocks.".format(servstocks[2]).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if servstocks[2]-num >= 0:
												servstocks = [servstocks[0],servstocks[1],servstocks[2]-num]
												money = [money[0]+(num*servmarketvalues[2])]
												break
											else:
												print("Oops, that's not a valid option! Please make sure you have enough to sell.")	
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "done":
								break
							else:
								print("Oops, that's not a valid option! Pick either 1, 2, or 3, or input 'done'")
								i += 1
						i += 1
					elif selection == "cons":
						i = 0
						while i == i:
							print("Balance:".center(columns))
							print(("${}".format(str(money[0]))).center(columns))
							print("")
							print("You currently have:".center(columns))
							print("{} stocks in EZHome Co. (1)".format(consstocks[0]).center(columns))
							print("{} stocks in BuildItUp Inc. (2)".format(consstocks[1]).center(columns))
							print("{} stocks in ConVest Inc. (3)".format(consstocks[2]).center(columns))
							print("")
							print("Current market values:".center(columns))
							print("${} for a stock in EZHome Co.".format(consmarketvalues[0]).center(columns))
							print("${} for a stock in BuildItUp Inc.".format(consmarketvalues[1]).center(columns))
							print("${} for a stock in ConVest Inc.".format(consmarketvalues[2]).center(columns))
							print("")
							print("Which company's stock would you like to sell (hint: the number in parentheses next to the company name is the number of that company)? Input done if you're done.".center(columns))
							inputted = input("> ")
							if inputted == "1":
								a = 0
								while a == a:
									print("How many stocks would you like to sell? You can currently sell up to {} stocks.".format(consstocks[0]).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if consstocks[0]-num >= 0:
												consstocks = [consstocks[0]-num,consstocks[1],consstocks[2]]
												money = [money[0]+(num*consmarketvalues[0])]
												break
											else:
												print("Oops, that's not a valid option! Please make sure you have enough to sell.")	
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "2":
								a = 0
								while a == a:
									print("How many stocks would you like to sell? You can currently sell up to {} stocks.".format(consstocks[1]).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if consstocks[1]-num >= 0:
												consstocks = [consstocks[0],consstocks[1]-num,consstocks[2]]
												money = [money[0]+(num*consmarketvalues[1])]
												break
											else:
												print("Oops, that's not a valid option! Please make sure you have enough to sell.")
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "3":
								a = 0
								while a == a:
									print("How many stocks would you like to sell? You can currently sell up to {} stocks.".format(consstocks[2]).center(columns))
									num = int(input("> "))
									a1 = 0
									while a1 == a1:
										if num >= 0:
											if consstocks[2]-num >= 0:
												consstocks = [consstocks[0],consstocks[1],consstocks[2]-num]
												money = [money[0]+(num*consmarketvalues[2])]
												break
											else:
												print("Oops, that's not a valid option! Please make sure you have enough to sell.")	
												break
										else:
											print("Oops, that's not a valid option! Please pick a positive integer.")
											a1 += 1
									break
							elif inputted == "done":
								break
							else:
								print("Oops, that's not a valid option! Pick either 1, 2, or 3, or input 'done'")
								i += 1
						i += 1
					elif selection == "done":
						break
					else:
						print("Oops, that's not a valid option! Your choices are: agrc for Agriculture, tech for Technology, serv for Services, and cons for Construction. Alternatively, you can input 'done' to move on.")
						i += 1
				elif buyorsell == "done":
					break
				else:
					print("Oops, that's not a valid option! Please input either 'buy' or 'sell'.")
					i += 1
			print("Balance:".center(columns))
			print(("${}".format(str(money[0]))).center(columns))
			print("")
			print("You currently have:".center(columns))
			print("")
			print("{} stocks in GroFast & Co. (agrc)".format(agrcstocks[0]).center(columns))
			print("{} stocks in BerryGood Inc. (agrc)".format(agrcstocks[1]).center(columns))
			print("{} stocks in AgVest Inc. (agrc)".format(agrcstocks[2]).center(columns))
			print("{} stocks in LiteSpd Technologies & Co. (tech)".format(techstocks[0]).center(columns))
			print("{} stocks in Ping Inc. (tech)".format(techstocks[1]).center(columns))
			print("{} stocks in TechVest Inc. (tech)".format(techstocks[2]).center(columns))
			print("{} stocks in QuickBurger Co. (serv)".format(servstocks[0]).center(columns))
			print("{} stocks in OnDemTV Inc. (serv)".format(servstocks[1]).center(columns))
			print("{} stocks in SerVest Inc. (serv)".format(servstocks[2]).center(columns))
			print("{} stocks in EZHome Co. (cons)".format(consstocks[0]).center(columns))
			print("{} stocks in BuildItUp Inc. (cons)".format(consstocks[1]).center(columns))
			print("{} stocks in ConVest Inc. (cons)".format(consstocks[2]).center(columns))
			print("")
			print("Would you like to restart market forces and continue the game?".center(columns))
			moveon = input("> ")
			if moveon == "yes":
				break
			elif moveon == "y":
				break
			elif moveon == "no":
				i += 1
			elif moveon == "n":
				i += 1
			else:
				print("Oops, that's not a valid option! Please enter 'done', then choose either 'yes' or 'y' to continue the game, or 'no' or 'n' to continue investing.")
				break
		if money[0] < 50.00:
			if agrcstocks == [0,0,0]:
				if techstocks == [0,0,0]:
					if 	servstocks == [0,0,0]:
						if consstocks == [0,0,0]:
							print("Game over. You have no money, and no stocks, what will you do? RIP :(".center(columns))
							quit()
		if money[0] < -75:
			i = 0
			while i < 25:
				print("")
				i += 1
			print("  |/|".center(columns))
			print("  | |".center(columns))
			print("  |/|".center(columns))
			print("  | |".center(columns))
			print("  |/|".center(columns))
			print("  | |".center(columns))
			print("  (___)".center(columns))
			print("  (___)".center(columns))
			print("  (___)".center(columns))
			print("  (___)".center(columns))
			print("  (___)".center(columns))
			print(r"  // \\".center(columns))
			print(r" //   \\".center(columns))
			print(" ||     ||".center(columns))
			print(" ||     ||".center(columns))
			print(" ||     ||".center(columns))
			print(r" \\___//".center(columns))
			print("  -----".center(columns))
			print("")
			print("")
			print("")
			print("Game over. You hanged yourself after seeing how much debt you were in, and left your pitiful stocks to your children.".center(columns))
			a = 0 
			while a <10:
				print("")
				a += 1
			input("")
			quit()
		if turns == 0:
			input("All stock prices see significant gains in market value; just in time for your first trade!".center(columns))
			agrc1 = (random.uniform(1.05,1.65))
			agrc2 = (random.uniform(1.25,1.30))
			agrc3 = (random.uniform(1.15,1.50))
			tech1 = (random.uniform(1.05,1.65))
			tech2 = (random.uniform(1.25,1.45))
			tech3 = (random.uniform(1.15,1.50))
			serv1 = (random.uniform(1.05,1.65))
			serv2 = (random.uniform(1.25,1.45))
			serv3 = (random.uniform(1.15,1.50))
			cons1 = (random.uniform(1.05,1.65))
			cons2 = (random.uniform(1.25,1.45))
			cons3 = (random.uniform(1.15,1.50))
			agrcmarketvalues = [50.00*agrc1,75.00*agrc2,60.00*agrc3]
			techmarketvalues = [50.00*tech1,75.00*tech2,60.00*tech3]
			servmarketvalues = [50.00*serv1,75.00*serv2,60.00*serv3]
			consmarketvalues = [50.00*cons1,75.00*cons2,60.00*cons3]
			sharerise = {"GroFast & Co. (agrc)":agrc1, "BerryGood Inc. (agrc)":agrc2, "AgVest Inc. (agrc)":agrc3, 
			"LiteSpd Technologies & Co. (tech)":tech1, "Ping Inc. (tech)":tech2, "TechVest Inc. (tech)":tech3,
			"QuickBurger Co. (serv)":serv1, "OnDemTV Inc. (serv)":serv2, "SerVest Inc (serv)":serv3,
			"EZHome Co. (cons)":cons1, "BuildItUp Inc. (cons)":cons2, "ConVest Inc. (cons)":cons3}
			for company in complist:
				print(("{}'s stock value has risen {}%".format(company,((sharerise[company]*100)-100))).center(columns))
		if turns > 0:	
			if eventnum == 0:
				agrc1 = (random.uniform(1.00,1.65))
				agrc2 = (random.uniform(1.15,1.50))
				agrc3 = (random.uniform(1.05,1.25))
				tech1 = (random.uniform(0.80, 1.00))
				tech2 = (random.uniform(0.90, 1.00))
				tech3 = (random.uniform(0.95, 1.10))
				serv1 = (random.uniform(0.80, 1.00))
				serv2 = (random.uniform(0.90, 1.00))
				serv3 = (random.uniform(0.95, 1.10))
				cons1 = (random.uniform(0.80, 1.00))
				cons2 = (random.uniform(0.90, 1.00))
				cons3 = (random.uniform(0.95, 1.10))
				sharerise = {"GroFast & Co. (agrc)":agrc1, "BerryGood Inc. (agrc)":agrc2, "AgVest Inc. (agrc)":agrc3, 
				"LiteSpd Technologies & Co. (tech)":tech1, "Ping Inc. (tech)":tech2, "TechVest Inc. (tech)":tech3,
				"QuickBurger Co. (serv)":serv1, "OnDemTV Inc. (serv)":serv2, "SerVest Inc (serv)":serv3,
				"EZHome Co. (cons)":cons1, "BuildItUp Inc. (cons)":cons2, "ConVest Inc. (cons)":cons3}
				agrcmarketvalues = [agrcmarketvalues[0]*agrc1,agrcmarketvalues[1]*agrc2,agrcmarketvalues[2]*agrc3]
				techmarketvalues = [techmarketvalues[0]*tech1,techmarketvalues[1]*tech2,techmarketvalues[2]*tech3]
				servmarketvalues = [servmarketvalues[0]*serv1,servmarketvalues[1]*serv2,servmarketvalues[2]*serv3]
				consmarketvalues = [consmarketvalues[0]*cons1,consmarketvalues[1]*cons2,consmarketvalues[2]*cons3]
				for company in complist:
					if sharerise[company] < 1:
						print(("{}'s stock value has fallen {}%".format(company,(100-(sharerise[company]*100)))).center(columns))
					else:
						print(("{}'s stock value has risen {}%".format(company,((sharerise[company]*100)-100))).center(columns))
			if eventnum == 1:
				agrc1 = (random.uniform(0.80, 1.00))
				agrc2 = (random.uniform(0.90, 1.00))
				agrc3 = (random.uniform(0.95, 1.10))
				tech1 = (random.uniform(1.00,1.65))
				tech2 = (random.uniform(1.15,1.50))
				tech3 = (random.uniform(1.10,1.50))
				serv1 = (random.uniform(0.80, 1.00))
				serv2 = (random.uniform(0.90, 1.00))
				serv3 = (random.uniform(0.95, 1.10))
				cons1 = (random.uniform(0.80, 1.00))
				cons2 = (random.uniform(0.90, 1.00))
				cons3 = (random.uniform(0.95, 1.10))
				sharerise = {"GroFast & Co. (agrc)":agrc1, "BerryGood Inc. (agrc)":agrc2, "AgVest Inc. (agrc)":agrc3, 
				"LiteSpd Technologies & Co. (tech)":tech1, "Ping Inc. (tech)":tech2, "TechVest Inc. (tech)":tech3,
				"QuickBurger Co. (serv)":serv1, "OnDemTV Inc. (serv)":serv2, "SerVest Inc (serv)":serv3,
				"EZHome Co. (cons)":cons1, "BuildItUp Inc. (cons)":cons2, "ConVest Inc. (cons)":cons3}
				agrcmarketvalues = [agrcmarketvalues[0]*agrc1,agrcmarketvalues[1]*agrc2,agrcmarketvalues[2]*agrc3]
				techmarketvalues = [techmarketvalues[0]*tech1,techmarketvalues[1]*tech2,techmarketvalues[2]*tech3]
				servmarketvalues = [servmarketvalues[0]*serv1,servmarketvalues[1]*serv2,servmarketvalues[2]*serv3]
				consmarketvalues = [consmarketvalues[0]*cons1,consmarketvalues[1]*cons2,consmarketvalues[2]*cons3]
				for company in complist:
					if sharerise[company] < 1:
						print(("{}'s stock value has fallen {}%".format(company,(100-(sharerise[company]*100)))).center(columns))
					else:
						print(("{}'s stock value has risen {}%".format(company,((sharerise[company]*100)-100))).center(columns))
			if eventnum == 2:
				agrc1 = (random.uniform(0.80, 1.00))
				agrc2 = (random.uniform(0.90, 1.00))
				agrc3 = (random.uniform(0.95, 1.10))
				tech1 = (random.uniform(0.80, 1.00))
				tech2 = (random.uniform(0.90, 1.00))
				tech3 = (random.uniform(0.95, 1.10))
				serv1 = (random.uniform(1.00,1.65))
				serv2 = (random.uniform(1.15,1.50))
				serv3 = (random.uniform(1.10,1.50))
				cons1 = (random.uniform(0.80, 1.00))
				cons2 = (random.uniform(0.90, 1.00))
				cons3 = (random.uniform(0.95, 1.10))
				sharerise = {"GroFast & Co. (agrc)":agrc1, "BerryGood Inc. (agrc)":agrc2, "AgVest Inc. (agrc)":agrc3, 
				"LiteSpd Technologies & Co. (tech)":tech1, "Ping Inc. (tech)":tech2, "TechVest Inc. (tech)":tech3,
				"QuickBurger Co. (serv)":serv1, "OnDemTV Inc. (serv)":serv2, "SerVest Inc (serv)":serv3,
				"EZHome Co. (cons)":cons1, "BuildItUp Inc. (cons)":cons2, "ConVest Inc. (cons)":cons3}
				agrcmarketvalues = [agrcmarketvalues[0]*agrc1,agrcmarketvalues[1]*agrc2,agrcmarketvalues[2]*agrc3]
				techmarketvalues = [techmarketvalues[0]*tech1,techmarketvalues[1]*tech2,techmarketvalues[2]*tech3]
				servmarketvalues = [servmarketvalues[0]*serv1,servmarketvalues[1]*serv2,servmarketvalues[2]*serv3]
				consmarketvalues = [consmarketvalues[0]*cons1,consmarketvalues[1]*cons2,consmarketvalues[2]*cons3]
				for company in complist:
					if sharerise[company] < 1:
						print(("{}'s stock value has fallen {}%".format(company,(100-(sharerise[company]*100)))).center(columns))
					else:
						print(("{}'s stock value has risen {}%".format(company,((sharerise[company]*100)-100))).center(columns))
			if eventnum == 3:
				agrc1 = (random.uniform(0.80, 1.00))
				agrc2 = (random.uniform(0.90, 1.00))
				agrc3 = (random.uniform(0.95, 1.10))
				tech1 = (random.uniform(0.80, 1.00))
				tech2 = (random.uniform(0.90, 1.00))
				tech3 = (random.uniform(0.95, 1.10))
				serv1 = (random.uniform(0.80, 1.00))
				serv2 = (random.uniform(0.90, 1.00))
				serv3 = (random.uniform(0.95, 1.10))
				cons1 = (random.uniform(1.00,1.65))
				cons2 = (random.uniform(1.15,1.50))
				cons3 = (random.uniform(1.10,1.50))
				sharerise = {"GroFast & Co. (agrc)":agrc1, "BerryGood Inc. (agrc)":agrc2, "AgVest Inc. (agrc)":agrc3, 
				"LiteSpd Technologies & Co. (tech)":tech1, "Ping Inc. (tech)":tech2, "TechVest Inc. (tech)":tech3,
				"QuickBurger Co. (serv)":serv1, "OnDemTV Inc. (serv)":serv2, "SerVest Inc (serv)":serv3,
				"EZHome Co. (cons)":cons1, "BuildItUp Inc. (cons)":cons2, "ConVest Inc. (cons)":cons3}
				agrcmarketvalues = [agrcmarketvalues[0]*agrc1,agrcmarketvalues[1]*agrc2,agrcmarketvalues[2]*agrc3]
				techmarketvalues = [techmarketvalues[0]*tech1,techmarketvalues[1]*tech2,techmarketvalues[2]*tech3]
				servmarketvalues = [servmarketvalues[0]*serv1,servmarketvalues[1]*serv2,servmarketvalues[2]*serv3]
				consmarketvalues = [consmarketvalues[0]*cons1,consmarketvalues[1]*cons2,consmarketvalues[2]*cons3]
				for company in complist:
					if sharerise[company] < 1:
						print(("{}'s stock value has fallen {}%".format(company,(100-(sharerise[company]*100)))).center(columns))
					else:
						print(("{}'s stock value has risen {}%".format(company,((sharerise[company]*100)-100))).center(columns))
			if eventnum == 4:
				agrc1 = (random.uniform(0.75, 1.25))
				agrc2 = (random.uniform(0.75, 1.25))
				agrc3 = (random.uniform(0.75, 1.25))
				tech1 = (random.uniform(0.75, 1.25))
				tech2 = (random.uniform(0.75, 1.25))
				tech3 = (random.uniform(0.75, 1.25))
				serv1 = (random.uniform(0.75, 1.25))
				serv2 = (random.uniform(0.75, 1.25))
				serv3 = (random.uniform(0.75, 1.25))
				cons1 = (random.uniform(0.75, 1.25))
				cons2 = (random.uniform(0.75, 1.25))
				cons3 = (random.uniform(0.75, 1.25))
				agrcmarketvalues = [agrcmarketvalues[0]*agrc1,agrcmarketvalues[1]*agrc2,agrcmarketvalues[2]*agrc3]
				techmarketvalues = [techmarketvalues[0]*tech1,techmarketvalues[1]*tech2,techmarketvalues[2]*tech3]
				servmarketvalues = [servmarketvalues[0]*serv1,servmarketvalues[1]*serv2,servmarketvalues[2]*serv3]
				consmarketvalues = [consmarketvalues[0]*cons1,consmarketvalues[1]*cons2,consmarketvalues[2]*cons3]
				sharerise = {"GroFast & Co. (agrc)":agrc1, "BerryGood Inc. (agrc)":agrc2, "AgVest Inc. (agrc)":agrc3, 
				"LiteSpd Technologies & Co. (tech)":tech1, "Ping Inc. (tech)":tech2, "TechVest Inc. (tech)":tech3,
				"QuickBurger Co. (serv)":serv1, "OnDemTV Inc. (serv)":serv2, "SerVest Inc (serv)":serv3,
				"EZHome Co. (cons)":cons1, "BuildItUp Inc. (cons)":cons2, "ConVest Inc. (cons)":cons3}
				for company in complist:
					if sharerise[company] < 1:
						print(("{}'s stock value has fallen {}%".format(company,(100-(sharerise[company]*100)))).center(columns))
					else:
						print(("{}'s stock value has risen {}%".format(company,((sharerise[company]*100)-100))).center(columns))
		money = [money[0]+(0.05*agrcstocks[0]*agrcmarketvalues[0])+(0.05*agrcstocks[1]*agrcmarketvalues[1])+(0.05*agrcstocks[2]*agrcmarketvalues[2])+
		(0.05*techstocks[0]*techmarketvalues[0])+(0.05*techstocks[1]*techmarketvalues[1])+(0.05*techstocks[2]*techmarketvalues[2])+
		(0.05*servstocks[0]*servmarketvalues[0])+(0.05*servstocks[1]*servmarketvalues[1])+(0.05*servstocks[2]*servmarketvalues[2])+
		(0.05*consstocks[0]*consmarketvalues[0])+(0.05*consstocks[1]*consmarketvalues[1])+(0.05*consstocks[2]*consmarketvalues[2])-25]
		i += 1
		turns += 1
start()