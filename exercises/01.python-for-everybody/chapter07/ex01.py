# Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows:

file = open('mbox-short.txt');

for line in file:
	line = line.rstrip().upper()
	print(line);