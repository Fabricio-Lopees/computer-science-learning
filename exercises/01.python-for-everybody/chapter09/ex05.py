# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

file_name = input('Enter a file name: ');
try:
	file = open(file_name);
except:
	print('Could not open the file!');
	exit();
domain_names = {};
for line in file:
	if line.startswith('From '):
		email = line.split()[1];
		at_position = email.find('@');
		domain_name = email[at_position+1:];
		if domain_name in domain_names:
			domain_names[domain_name] = domain_names[domain_name] + 1;
		else:
			domain_names[domain_name] = 1;
print(domain_names)