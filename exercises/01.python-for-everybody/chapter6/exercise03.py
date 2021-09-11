def count(txt, char):
	count = 0

	for x in txt:
		if x == char:
			count = count + 1

	return count

text = input('Enter a text: ')
character = input('Enter a character that you can search in "'+text+'": ')

result = count(text, character)

print('The character "'+character+'" appears '+str(result)+' times in "'+text+'".')