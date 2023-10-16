import sqlite3 as db
import xml.etree.ElementTree as ET

LIBRARY_FILE_PATH = './tracks/Library.xml'

db_connection = db.connect('trackdb.sqlite')
db_cursor = db_connection.cursor()

sqls_list = ['DROP TABLE IF EXISTS Artist;', 'DROP TABLE IF EXISTS Genre;', 'DROP TABLE IF EXISTS Album;',
             'DROP TABLE IF EXISTS Track;',
             'CREATE TABLE Artist ( id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name    TEXT UNIQUE );',
             'CREATE TABLE Genre ( id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name    TEXT UNIQUE );',
             'CREATE TABLE Album ( id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, artist_id  INTEGER, title   TEXT UNIQUE );',
             'CREATE TABLE Track ( id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title TEXT  UNIQUE, album_id  INTEGER, genre_id  INTEGER, len INTEGER, rating INTEGER, count INTEGER );']
for sql_string in sqls_list:
    db_cursor.execute(sql_string)

library_xml_file_handel = open(LIBRARY_FILE_PATH)


def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


stuff = ET.parse(library_xml_file_handel)
entries = stuff.findall('dict/dict/dict')
print('Dict count:', len(entries))
for entry in entries:
    if (lookup(entry, 'Track ID') is None): continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')

    if name is None or artist is None or album is None:
        continue

    print(name, artist, album, count, rating, length, genre, '\n')

    # Genre
    if genre is not None:
        db_cursor.execute('''INSERT OR IGNORE INTO Genre (name)
                VALUES ( ? )''', (genre,))
        db_cursor.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
        genre_id = db_cursor.fetchone()[0]

    # Artist
    db_cursor.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', (artist,))
    db_cursor.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = db_cursor.fetchone()[0]

    # Album table
    db_cursor.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', (album, artist_id))
    db_cursor.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = db_cursor.fetchone()[0]

    # Track table
    db_cursor.execute('''INSERT OR REPLACE INTO Track
        (title, album_id,genre_id, len, rating, count)
        VALUES ( ?, ?, ?,?, ?, ? )''',
                      (name, album_id, genre_id, length, rating, count,))

    db_connection.commit()
db_connection.close()
