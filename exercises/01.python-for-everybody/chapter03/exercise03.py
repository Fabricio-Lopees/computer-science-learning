try:
	number=float(input("Enter a number between 0.0 and 1.0: "))
	if number < 0 or number > 1:
		print("Bad score!")
	elif number >= 0.9:
		print("A")
	elif number >= 0.8:
		print("B")
	elif number >= 0.7:
		print("C")
	elif number >= 0.6:
		print("D")
	else:
		print("F")
except:
	print("Bad score!")