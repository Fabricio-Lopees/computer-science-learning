text = input('Enter a text: ')
character = input('Enter a character that you can search in "'+text+'": ')

result = text.count(character)

print('The character "'+character+'" appears '+str(result)+' times in "'+text+'".')