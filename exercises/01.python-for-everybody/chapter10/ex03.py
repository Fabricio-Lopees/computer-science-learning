# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

file_name = '../chapter09/words.txt';
try:
	file = open(file_name);
except:
	print('Could not open the file!');
	exit();
letter_guide = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
letters = dict();
delimeter = ' ';
for line in file:
	sentence = line.split();
	sentence = delimeter.join(sentence).lower();
	sentence = list(sentence)
	for element in sentence:
		if element in letter_guide:
			if element in letters:
				letters[element] = letters[element] + 1;
			else:
				letters[element] = 1;
		else:
			continue;

letters_list = list();
for letter in letters:
	letters_list.append((letters[letter], letter));
letters_list.sort(reverse=True);
print(letters_list)