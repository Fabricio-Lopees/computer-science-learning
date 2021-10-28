# Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195

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
maximum = 0;
most_messages = None;
for email in histogram:
	if histogram[email] > maximum:
		most_messages = email;
		maximum = histogram[email]
print('Email:',most_messages,'\nMessages sent:',maximum);