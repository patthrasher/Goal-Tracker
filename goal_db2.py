# updates goaldb

import sqlite3
import datetime

def week_number() : # returns integer of current week number
    day = datetime.date.today()
    strday = str(day)
    lst = strday.split('-')

    year = int(lst[0])
    month = int(lst[1])
    day = int(lst[2])

    week = datetime.date(year, month, day).isocalendar()[1]
    return week

strstudy = input('Study hours: ')
strtrain = input('Bjj days: ')

try :
    study = float(strstudy)
    train = int(strtrain)
except :
    print('Enter numbers')
    quit()

conn = sqlite3.connect('goaldb.sqlite')
cur = conn.cursor()

cur.execute('''SELECT * FROM Work_2019 WHERE week = ?''', (week_number(),))
oldstudy = cur.fetchone()[1]
cur.execute('''SELECT * FROM Work_2019 WHERE week = ?''', (week_number(),))
oldtrain = cur.fetchone()[2]

cur.execute('''UPDATE Work_2019 SET study_hours = ? WHERE week = ?''',
                (oldstudy + study, week_number()))
cur.execute('''UPDATE Work_2019 SET bjj = ? WHERE week = ?''',
                (oldtrain + train, week_number()))

conn.commit()
cur.close()

print('Database updated')

# prints days left in year
today = datetime.date.today()
future = datetime.date(2019, 12, 29)
diff = str(future - today)
print(diff[:3], 'days left in year')
