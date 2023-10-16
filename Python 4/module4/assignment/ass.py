import json
import sqlite3

# Create SQLite database and cursor
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Drop existing tables if they exist
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
''')

# Create User table
cur.execute('''
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
)
''')

# Create Course table
cur.execute('''
CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
)
''')

# Create Member table
cur.execute('''
CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Read JSON data from file
file_name = 'roster_data.json'
with open(file_name) as file:
    json_data = json.load(file)

# Insert data into User, Course, and Member tables
for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    # Insert or ignore into User table
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    # Insert or ignore into Course table
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    # Insert or replace into Member table
    cur.execute('''
        INSERT OR REPLACE INTO Member (user_id, course_id, role)
        VALUES (?, ?, ?)
    ''', (user_id, course_id, role))

# Save changes and close the database connection
conn.commit()
conn.close()

# Connect to the database again to run queries
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Query 1: SELECT User.name, Course.title, Member.role
cur.execute('''
SELECT User.name, Course.title, Member.role FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY User.name DESC, Course.title DESC, Member.role DESC
LIMIT 2
''')

# Print query 1 results
print("Query 1 Results:")
for row in cur.fetchall():
    print(row[0], row[1], row[2])

# Query 2: SELECT 'XYZZY' || hex(User.name || Course.title || Member.role) AS X
cur.execute('''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY X
LIMIT 1
''')

# Print query 2 result
print("Query 2 Result:")
print(cur.fetchone()[0])

# Close the database connection
conn.close()
