import sqlite3
import json

# Read JSON file
with open('roster.json') as f:
    data = json.load(f)

# Create SQLite database
conn = sqlite3.connect('roster.db')
cur = conn.cursor()

# Create User table
cur.execute('''CREATE TABLE IF NOT EXISTS User
               (id INTEGER PRIMARY KEY, name TEXT UNIQUE)''')

# Create Course table
cur.execute('''CREATE TABLE IF NOT EXISTS Course
               (id INTEGER PRIMARY KEY, title TEXT UNIQUE)''')

# Create Member table
cur.execute('''CREATE TABLE IF NOT EXISTS Member
               (user_id INTEGER, course_id INTEGER, role INTEGER, PRIMARY KEY(user_id, course_id))''')

# Populate User table
for user in data['users']:
    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES (?)''', (user['name'],))
    user_id = cur.lastrowid

# Populate Course table
for course in data['courses']:
    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''', (course['title'],))
    course_id = cur.lastrowid

# Populate Member table
for member in data['members']:
    cur.execute('''INSERT INTO Member (user_id, course_id, role) VALUES (?, ?, ?)''',
                (member['user_id'], member['course_id'], member['role']))

# Save changes and close connection
conn.commit()
conn.close()
