# pip install beautifulsoup4
# import beautifulsoup4
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import urllib.parse
import ssl

# Ignore SSL certificate errors

# crate default SSL context
ctx = ssl.create_default_context()

# cheking the hostname in SSL against the hostname URL
ctx.check_hostname = False

# disables the verification of SSL certificate
ctx.verify_mode = ssl.CERT_NONE

# By setting (check_hostname) to False and (verify_mode) to (ssl.CERT_NONE),
# the SSL certificate errors are ignored,
# and the HTTP request can be made even if the SSL certificate is invalid or not properly configured.

url = ' https://docs.python.org'
html = urllib.request.urlopen(url, context=ctx).read()

# 'html.parser' parser to parse the HTML data
soup = BeautifulSoup(html, 'html.parser')

# find all the tages <a> (link) using soup method soup('tag') and stores them in variables named tags
tags = soup('a')

# Looping in all links in tags variables and get value of href using 'tag'.get('href{attribute},None')
for tag in tags:
    hrefs = tag.get('href', None)
    print(hrefs)
