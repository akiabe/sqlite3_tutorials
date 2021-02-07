import sqlite3

conn = sqlite3.connect("test_sqlite.db")

curs = conn.cursor()

#curs.execute('CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
#curs.execute('INSERT INTO persons(name) values("Mike")')

#curs.execute('INSERT INTO persons(name) values("Nancy")')
#curs.execute('INSERT INTO persons(name) values("Jun")')

curs.execute('UPDATE persons set name = "Michel" WHERE name = "Mike" ')
conn.commit()

curs.execute('SELECT * from persons')
print(curs.fetchall())

conn.close()