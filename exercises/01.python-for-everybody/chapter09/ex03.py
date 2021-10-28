# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

file_name = input('Enter a file name: ');
try:
	file = open(file_name);
except:
	print('Could not open the file!');
	exit();
histogram = {};
for line in file:
	if line.startswith('From '):
		email = line.split()[1];
		if email in histogram:
			histogram[email] = histogram[email] + 1;
		else:
			histogram[email] = 1;
print(histogram)