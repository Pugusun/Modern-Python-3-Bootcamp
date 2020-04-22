age = 21
# 2-8 2 dollar ticket 
# over 65 5 dollar ticket 
# 10 dollars for eveyone else 

age >= 2 and age<= 8
age >= 65
if not ((age >= 2 and age <= 8) or age >= 65):
	print ("YOU PAY 10 DOLLARS and ARE NOT A CHILD OR OLDIE!")
	