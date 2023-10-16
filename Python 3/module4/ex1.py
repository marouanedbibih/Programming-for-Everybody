from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import urllib.parse
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname =False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1782966.html'
html = urllib.request.urlopen(url,context=ctx).read()

soup = BeautifulSoup(html,'html.parser')

tags = soup('span')
numbers = list()
for tag in tags:
    tag = str(tag)
    nbr = re.findall('<span class="comments">([0-9]+)</span>',tag)
    for n in nbr :
        n = int(n)
    numbers.append(n)

for nb in numbers:
    somme = sum(numbers)

print(somme)

