# shows totals for year

import datetime
import sqlite3
import utility
from utility import week_number

conn = sqlite3.connect('goaldb.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM ' + utility.db_name)
data = cur.fetchall()

study_count = 0
bjj_count = 0
for each in data :
    study_count = study_count + each[1]
    bjj_count = bjj_count + each[2]

print('('+utility.year+')Total study hours: ' + str(study_count))
print('('+utility.year+')Total bjj days: ' + str(bjj_count))
print('======================')

cur.execute('SELECT * FROM ' + utility.db_name + ' WHERE week = ?', (week_number(),))
week_total = cur.fetchall()

print('Week', week_number(), 'totals - ')
print('Study hours:', week_total[0][1])
print('bjj days:', week_total[0][2])
print(52 - week_number(), 'weeks left in year')

cur.close()
