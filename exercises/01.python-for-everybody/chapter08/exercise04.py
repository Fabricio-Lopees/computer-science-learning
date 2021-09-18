file = open('romeo.txt')
words_list = []

for line in file:
	temporary_list = line.split()
	for word in temporary_list:
		exist = word in words_list
		if exist == True: 
			continue
		else:
			words_list.append(word)

words_list.sort()
print(words_list)