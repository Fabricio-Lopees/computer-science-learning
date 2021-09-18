try:
	hours=float(input("Enter hours worked: "))
	rate=float(input("Enter rate: "))
	total=0;

	def extra():
		extra_hour=hours-40
		extra_rate=extra_hour*rate

		computepay(hours,rate,extra_rate)

	def computepay(h,r,extra):
		total=h*r+extra
		print("Total: ",total)

	if hours > 40:
		extra();
	else:
		computepay(hours, rate, 0)
except:
	print("ERROR! Please enter numbers.")