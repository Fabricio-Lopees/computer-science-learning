# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary. After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits

file_name = input('Enter a file name: ');
try:
	file = open(file_name);
except:
	print('Could not open the file!');
	exit();
histogram = {};
for line in file:
	if line.startswith('From '):
		address = line.split()[1];
		if address in histogram:
			histogram[address] = histogram[address] + 1;
		else:
			histogram[address] = 1;
emails = list();
for address in histogram:
	emails.append((histogram[address], address));
emails.sort(reverse=True)
print('Email:',emails[0][1],'\nMessages sent:',emails[0][0]);
