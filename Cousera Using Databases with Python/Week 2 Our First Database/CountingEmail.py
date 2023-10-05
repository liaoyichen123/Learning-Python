import sqlite3 as db
import re

db_connection = db.connect('CountingEmail.db')
db_cursor = db_connection.cursor()

db_cursor.execute('DROP TABLE IF EXISTS Counts')
db_cursor.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

file_handle = open('mbox.txt', 'r')
for line in file_handle:
    if line.startswith('From '):
        email_domain_str = re.findall('(?<=@).*$').strip()
        print(line)