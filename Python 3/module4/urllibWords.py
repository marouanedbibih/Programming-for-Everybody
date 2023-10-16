# Importation de urllib librerie
import urllib.request,urllib.error,urllib.parse

# request web page by (urrllib.request) and get Html file by (urlopen()) 
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# Create a dictionnaire
counts = dict()

# Looping in line of file
for line in fhand:

    # decode line in bytes to unicode and clear whitespace
    words = line.decode().split()
    # count the word and put in dicationnaire
    for word in words:
        counts[word] = counts.get(word,0) + 1

# display word and number of this word in file
print(counts)

