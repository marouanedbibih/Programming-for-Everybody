import sqlite3

conn = sqlite3.connect('email_db.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Email')

cur.execute('''
CREATE TABLE Email (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From'): continue
    words = line.split()
    email = words[1]
    org = email.split('@')[1]
    cur.execute('SELECT count FROM Email WHERE org = ? ', (org,))
    resultat = cur.fetchall()
    if resultat is None:
        cur.execute('''INSERT INTO Email (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE email SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Email ORDER BY count DESC LIMIT 10'
rows = cur.execute(sqlstr)
total = 0
for row in rows :
    print(str(row[0]), row[1])
    total = total + int(row[1])

print('Total : ',total)
cur.close()