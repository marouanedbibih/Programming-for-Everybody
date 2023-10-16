import urllib.request
import urllib.error
import urllib.parse
import xml.etree.ElementTree as tr
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname =False
ctx.verify_mode = ssl.CERT_NONE

url = ' http://py4e-data.dr-chuck.net/comments_1782968.xml'
url_file = urllib.request.urlopen(url,context=ctx).read()
print('Retrieved :',len(url_file),'characters')

xml_file = url_file.decode()

xml = tr.fromstring(xml_file)
counts = xml.findall('comments/comment')
print('Counts :',len(counts))

somme = 0
for item in counts:
    count = int(item.find('count').text)
    somme = somme + count

print('Sum :',somme)

