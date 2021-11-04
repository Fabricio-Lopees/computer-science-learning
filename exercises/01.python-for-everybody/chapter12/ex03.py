# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL, (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document. Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

import urllib.request;
try:
	#url = input("Enter a url: ");
	url = "http://data.pr4e.org/romeo.txt"
	content = urllib.request.urlopen(url);
except:
	print("ERROR! \nImproperly formatted or non-existent URL");
	exit();

size = 0
result = b'';

while True:
    info = content.read(100000)
    if len(info) < 1 or len(info) >= 3000: break
    size = size + len(info)
    result = result + info;
    
print(result.decode())
print(size, 'characters copied.')