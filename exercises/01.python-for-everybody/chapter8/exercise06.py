array = []

def evaluate_numbers():
	number = input("Enter a number: ")
	if number.lower() == 'done':
		if len(array) == 0: 
			print('Maximum: None')
			print('Minimum: None')
		else:
			print('Maximum: ',max(array))
			print('Minimum: ',min(array))
	else:
		try:
			array.append(float(number))
			evaluate_numbers()
		except:
			print("ERROR! Only enter a NUMBER!")
			evaluate_numbers()
	

evaluate_numbers()