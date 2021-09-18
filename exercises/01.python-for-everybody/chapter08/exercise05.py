def show_mail_author(mail):
	file = open(mail)
	count = 0
	for line in file:
		if not line.startswith('From') or line.startswith('From:'): 
			continue
		else:
			words = line.split()
			print(words[1])
			count = count + 1
	print("There were "+str(count)+" lines in the file with From as the first word")

file_name = input("Enter a file name:")
show_mail_author(file_name)