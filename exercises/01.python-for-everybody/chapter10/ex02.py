# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour.

file_name = input('Enter a file name: ');
try:
	file = open(file_name);
except:
	print('Could not open the file!');
	exit();
hours = {};
for line in file:
	if line.startswith('From '):
		colon_position = line.find(':');
		hour = (line[colon_position - 2:colon_position])
		if hour in hours:
			hours[hour] = hours[hour] + 1;
		else:
			hours[hour] = 1;

hours_list = [];
for h in hours:
	hours_list.append((h, hours[h]))
hours_list.sort()

for hour in hours_list:
	print('Hour:',hour[0],'|',hour[1],'emails sent.');