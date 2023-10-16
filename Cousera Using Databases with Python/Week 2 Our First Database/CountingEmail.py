import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
db_cursor = conn.cursor()

db_cursor.execute('DROP TABLE IF EXISTS Counts')
db_cursor.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

file_handle = open('mbox.txt', 'r')
for line in file_handle:
    if line.startswith('From '):
        email_domain_str = re.search("@[^\s]*", line).group()
        email_domain_str = email_domain_str.replace("@", "")
        db_cursor.execute("SELECT COUNT FROM COUNTS WHERE ORG = ?", (email_domain_str,))
        cnt = db_cursor.fetchone()
        if cnt is None:
            db_cursor.execute("INSERT INTO COUNTS (ORG, COUNT) VALUES (?, 1)", (email_domain_str,))
        else:
            db_cursor.execute("UPDATE COUNTS SET COUNT = COUNT + 1 WHERE ORG = ?", (email_domain_str,))
        conn.commit()
conn.commit()
conn.close()