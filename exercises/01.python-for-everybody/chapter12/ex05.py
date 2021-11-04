# Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received. Remember that recv receives characters (newlines and all), not lines.

import socket;

try:
	url = input('Enter url: ');
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

response = mysocket.recv(5000);
pos = response.find(b'\r\n\r\n');
content = response[pos+4:].decode();

print(content)