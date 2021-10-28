# Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt. Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

file = open('words.txt');
count = 0;
words = {};
for line in file:
	line_words = line.split();
	for word in line_words:
		words[word] = count;
		count = count + 1;
print('and' in words)