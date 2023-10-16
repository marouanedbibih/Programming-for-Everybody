# Read a web page (Facebook)

# Importation de urllib librerie
import urllib.request,urllib.error,urllib.parse

# request Facebook page by (urrllib.request) and get Html file by (urlopen()) 
facebook_file = urllib.request.urlopen('https://www.facebook.com')

# Looping in web page file and decode file in bytes to unicode by decode() method 
# strip() ---> clear the white space
for line in facebook_file:
    print(line.decode().strip())

