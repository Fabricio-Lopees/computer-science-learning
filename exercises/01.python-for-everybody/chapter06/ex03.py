# Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

car = 'chevrolet chevette';

def count(string, letter):
	count = 0;
	for x in string:
		if x == letter:
			count = count + 1;
	return count;

result = count(car, 't');
print(result)