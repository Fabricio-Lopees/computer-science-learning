hours=int(input("Enter hors worked: "))
rate=float(input("Enter rate: "))
if hours > 40:
	rate=rate*1.5
total=hours*rate
print("Total (R$): ",total)