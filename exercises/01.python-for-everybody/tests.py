# count how many times a letter appears in a word

word = 'brontosaurus'
word_in_dictionary = {}
for letter in word:
	if letter in word_in_dictionary:
		word_in_dictionary[letter] = word_in_dictionary[letter] + 1
	else:
		word_in_dictionary[letter] = 1

print(word_in_dictionary)