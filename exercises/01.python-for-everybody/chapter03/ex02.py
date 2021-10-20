# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

try:
	hours = int(input('Enter hours: '));
	rate = float(input('Enter rate: '));
except:
	print('Error, please enter numeric input.');
	exit()

if hours > 40:
	rate = rate * 1.5;
pay = hours * rate;
print('Pay:',pay)