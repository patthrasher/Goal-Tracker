# creates database for goal tracking, 52 weeks

import sqlite3
import datetime
import utility

conn = sqlite3.connect('goaldb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS ' + utility.db_name)
cur.execute('CREATE TABLE ' + utility.db_name + '(week INTEGER, study_hours INTEGER, bjj INTEGER)')

weeks = list(range(1,53))

for each in weeks :
    cur.execute('INSERT INTO ' + utility.db_name + '(week, study_hours, bjj) VALUES (?, 0, 0)', (each,))

conn.commit()
cur.close()

print('Database created')
