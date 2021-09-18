file_name = input('Enter file name: ')

try:
	file = open(file_name)
except:
	print('File cannot be opened')
	exit()

count = 0
numbers = 0
average = 0
for line in file:
	if line.startswith('X-DSPAM-Confidence'):
		colon_position = line.find(':')
		numbers = numbers + float(line[colon_position+1:])
		count = count + 1

if count != 0:
	average = numbers / count

print(average)