import xml.etree.ElementTree as tr
import sqlite3 as sq3

db = sq3.connect('trackdb.sqlite')
cur = db.cursor()

cur.executescript("""

DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
""")

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

file = input("Enter the file : ")
if len(file) < 1:
    file = 'Library.xml'

fl = tr.parse(file)
data = fl.findall("dict/dict/dict")

for dict in data:
    if ( lookup(dict, 'Track ID') is None ) : continue

    name = lookup(dict, 'Name')
    artist = lookup(dict, 'Artist')
    album = lookup(dict, 'Album')
    count = lookup(dict, 'Play Count')
    rating = lookup(dict, 'Rating')
    length = lookup(dict, 'Total Time')

    if name is None or artist is None or album is None : 
        continue

    print(name, artist, album, count, rating, length)

    cur.execute(''' insert or ignore into Artist(name) 
        values ( ? )''', ( artist, ) )
    cur.execute('select id from Artist where name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''insert or ignore into Album (title, artist_id) 
        values ( ?, ? )''', ( album, artist_id ) )
    cur.execute('select id from Album where title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''insert or ignore into Track
        (title, album_id, len, rating, count) 
        values ( ?, ?, ?, ?, ? )''', 
        ( name, album_id, length, rating, count ) )
    db.commit()