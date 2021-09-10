maximum = 0;
minimum = 0;
guard = None;

while guard != "done":
	try:
		number = input("Enter a number: ").lower()

		if number == "done":
			print("Highest number entered: ", maximum)
			print("Lowest number entered: ", minimum)
			guard = number
		else:
			number = float(number)
			if number > maximum:
				maximum = number

			if number < minimum:
				minimum = number
	except:
		print("Bad input!")

print("Program finished!")