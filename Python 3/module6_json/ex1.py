import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving', url)

# Open the URL and read the data
uh = urllib.request.urlopen(url) # open URL
data = uh.read().decode() # read the data
print('Retrieved', len(data), 'characters')

# Parse the JSON data
try:
    js = json.loads(data)
except:
    js = None

# Extract the comment counts and compute the sum
if js:
    counts = js['comments']
    print('Count:', len(counts))
    sum = 0
    for item in counts:
        sum += item['count']
    print('Sum:', sum)
else:
    print('Failed to retrieve data from', url)
