# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

try:
	hours = int(input('Enter hours: '));
	rate = float(input('Enter rate: '));
except: 
	print('Error!');
	exit();

def computepay(h, r):
	return h * r;

pay = computepay(hours, rate);
print('Pay:',pay);