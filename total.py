# shows totals for year

import datetime
import sqlite3

def week_number() : # returns integer of current week number
    day = datetime.date.today()
    strday = str(day)
    lst = strday.split('-')

    year = int(lst[0])
    month = int(lst[1])
    day = int(lst[2])

    week = datetime.date(year, month, day).isocalendar()[1]
    return week

conn = sqlite3.connect('goaldb.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM WORK_2019')
data = cur.fetchall()

study_count = 0
bjj_count = 0
for each in data :
    study_count = study_count + each[1]
    bjj_count = bjj_count + each[2]

print('(2019)Total study hours: ' + str(study_count))
print('(2019)Total bjj days: ' + str(bjj_count))
print('======================')

cur.execute('SELECT * FROM WORK_2019 WHERE week = ?', (week_number(),))
week_total = cur.fetchall()

print('Week', week_number(), 'totals - ')
print('Study hours:', week_total[0][1])
print('bjj days:', week_total[0][2])
print(52 - week_number(), 'weeks left in year')

cur.close()
