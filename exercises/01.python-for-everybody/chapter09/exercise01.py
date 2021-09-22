file = open('words.txt')

word_list = []
words = {}

for line in file:
	word_list = word_list + line.split()

for word in word_list:
	words[word] = value


print(words)
print('\n','daily' in words)