file_name = input("Enter a file name: ")

try:
	file = open(file_name)
except:
	print("The file cannot be opened")
	exit()

for line in file:
	print(line.upper().strip())