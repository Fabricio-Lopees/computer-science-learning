# Exercise 1: Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
import re;
entry = input('Enter a regular expression: ');
file = open('../chapter07/mbox.txt');
count = 0;
for line in file:
	if re.search(entry, line):
		count = count + 1;
print('mbox.txt had',count,'lines that matched', entry);