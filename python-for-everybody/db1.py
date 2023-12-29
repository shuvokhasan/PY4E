import sqlite3

conn = sqlite3.connect('music.sqlite')
curr = conn.cursor()

curr.execute('DROP TABLE IF EXISTS Tracks')
curr.execute('CREATE TABLE Tracks (title TEXTS, plays INTEGER)')

conn.close()