# Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

total = 0;
count = 0;
average = 0;
minimum = None;
maximum = None;

while True:
	entry = input('Enter a number: ');

	if entry.lower() == 'done':
		if count > 0:
			average = total / count;
		print('Minimum:',minimum,'\nMaximum:',maximum,'\nTotal:',total,'\nCount:',count,'\nAverage:',average);
		break;
	else:
		try:
			value = float(entry);
			total = total + value;
			count = count + 1;

			if minimum == None or value < minimum:
				minimum = value;

			if maximum == None or value > maximum:
				maximum = value;
		except:
			print('Invalid input!');