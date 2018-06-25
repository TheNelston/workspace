while True:
	import random
	import shutil
	import time
	columns = shutil.get_terminal_size().columns
	input("Welcome to Scattegories Lite! Press enter to start.".center(columns))
	input("Press enter to get your category.".center(columns))
	cats = ["Sciences", "Politics", "Failures", "Life", "What?"]
	cat = random.choice(cats)
	print("Your catgory is: {}".format(cat).center(columns))
	input("Press enter to begin.".center(columns))
	start = time.time()
	print("Type your answers next to the prompt!".center(columns))
	nums = [1,2,3,4,5,6,7,8,9,10]
	answers = []
	for num in nums:
		print("{}".format(cat).center(columns))
		print("")
		answers.append(input("{}.".format(num)))
	end = time.time()
	print("Done!".center(columns))
	print("Your answers were:".center(columns))
	space = len(max(answers))+10
	print(("="*(space)).center(columns))
	for ans in answers:
		print(ans.center(columns))
	print(("="*(space)).center(columns))
	time = end - start
	print("Your time was: {}s".format(time).center(columns))
	response = input("Play again? (y/n): ")
	if response == "y":
		continue
	else:
		print("Thanks for playing!")
		break