import urllib.request;
from bs4 import BeautifulSoup;
import ssl;

ctx = ssl.create_default_context();
ctx.check_hostname = False;
ctx.verify_mode = ssl.CERT_NONE;

url = input('Enter url: ');
html = urllib.request.urlopen(url, context=ctx).read();
soup = BeautifulSoup(html, 'html.parser');

tags = soup('p');
count = len(tags);
print(count);