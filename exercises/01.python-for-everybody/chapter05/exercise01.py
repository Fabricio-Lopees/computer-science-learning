total = 0
count = 0
average = 0
guard = None;

while guard != "done":
	number = input("Enter a number: ").lower()
	if number != "done":
		try:
			number = float(number)
			total = total + number
			count = count + 1
		except:
			print("Bad data!")
	else:
		if count == 0:
			print("Numbers entered: ",count," numbers.")
			print("Total: ",total,".")
			print("Average: ",average,".")
		else:
			average = total / count
			print("Numbers entered: ",count," numbers.")
			print("Total: ",total,".")
			print("Average: ",average,".")
		guard = number

print("Program finished!")