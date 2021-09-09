try:
	hours=float(input("Enter hours worked: "))
	rate=float(input("Enter rate: "))
	if hours > 40:
		rate=rate*1.5
	total=hours*rate
	print("Total (R$): ",total)
except:
	print("Error, please enter numeric input!")