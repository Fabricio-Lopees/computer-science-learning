file = open('words.txt')

word_list = []

words = {}

for line in file:
	word_list = word_list + line.split()


value = 0
for word in word_list:
	words[word] = value
	value = value + 1


print(words)
print('\n','daily' in words)