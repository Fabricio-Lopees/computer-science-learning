# Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

import socket;
try:
	url = input("Enter a url: ");
	hostname = url.split('/')[2];
	port = 80;
	request = 'GET '+url+' HTTP/1.0\r\n\r\n';
	request = request.encode();

	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	mysocket.connect((hostname, port));
	mysocket.send(request);
except:
	print("ERROR! \nImproperly formatted or non-existent URL");
	exit();

count = 0;
document = b'';

while True:
	response = mysocket.recv(5120);
	if len(response) < 1 or len(response) >= 3000:
		break;
	count = count + len(response);
	print(len(response), count);
	document = document + response;

mysocket.close;

print(document.decode(),'\nCharacters: ',len(document.decode()))