# creates database for goal tracking, 52 weeks

import sqlite3

conn = sqlite3.connect('goaldb.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Work_2019''')
cur.execute('''CREATE TABLE Work_2019 (week INTEGER, study_hours INTEGER,
                bjj INTEGER)''')

weeks = list(range(1,53))

for each in weeks :
    cur.execute('''INSERT INTO Work_2019(week, study_hours, bjj)
                        VALUES (?, 0, 0)''', (each,))

conn.commit()
cur.close()

print('Database created')
