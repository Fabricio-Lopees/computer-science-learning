mail_file = open('chapter7/mbox-short.txt')
text_file = open('file.txt','w')
text = ''
for line in mail_file:
	if line.startswith('From'):
		text = text + line
text_file.write(text)
text_file.close()