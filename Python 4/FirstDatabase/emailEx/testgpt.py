import sqlite3

conn = sqlite3.connect('gptdb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

org_counts = dict()

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]
    org_counts[org] = org_counts.get(org, 0) + 1

org_list = list(org_counts.keys())

for org in org_list:
    cur.execute('INSERT INTO Counts (org, count) VALUES (?, ?)', (org, org_counts[org]))

conn.commit()


sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print("Counts:")
total = 0
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    total = total + int(row[1])

print('Total : ',total)

cur.close()
