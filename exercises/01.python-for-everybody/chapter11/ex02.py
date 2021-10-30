# Exercise 2: Write a program to look for lines of the form: New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

import re;
file_name = input('Enter a file name: ');
file = open(file_name);
total = 0;
count = 0;
average = 0;
for line in file:
	num = re.findall('New Revision: ([0-9]+)', line);
	if len(num) > 0:
		num = ' '.join(num);
		num = int(num);
		total = total + num;		
		count = count + 1;
if count > 0:
	average = int(total / count);
print(average)