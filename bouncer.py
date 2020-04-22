# ask for age 
age = input ("How old are you?")
if age:
	age = int (age)
	if (age) >= 18 and (age) < 21:
		print ("You can enter, but need a wristband!")

	elif (age) >= 21:
		print("You are good to enter and drink!")

	else:
		print ("You cannot enter little one!") 
else:
	print ("Please enter an age!")
