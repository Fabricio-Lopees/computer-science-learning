# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

total = 0;
count = 0;
average = 0;

while True:
	entry = input('Enter a number: ');

	if entry.lower() == 'done':
		if count > 0:
			average = total / count;
		print('Total:',total,'\nCount:',count,'\nAverage:',average);
		break;
	else:
		try:
			value = float(entry);
			total = total + value;
			count = count + 1;
		except:
			print("Invalid input!");