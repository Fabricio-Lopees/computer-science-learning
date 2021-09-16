fhand = open('new_file.txt')
count = 0
for line in fhand:
	words = line.split()
	#print('Debug:', words)
   #if len(words) == 0 : continue       <---- OLD LINE
	if len(words) < 3 : continue      # <---- NEW LINE
	if words[0] != 'From' : continue
	print(words[2])
print(count)