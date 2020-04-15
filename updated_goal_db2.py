# updates goaldb

import sqlite3
import datetime
import utility
from utility import week_number

year = str(datetime.date.today().year)
db_name = 'Work_' + year

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

cur.execute('SELECT * FROM ' + utility.db_name + ' WHERE week = ?', (week_number(),))
oldstudy = cur.fetchone()[1]
cur.execute('SELECT * FROM ' + utility.db_name + ' WHERE week = ?', (week_number(),))
oldtrain = cur.fetchone()[2]

cur.execute('UPDATE ' + utility.db_name + ' SET study_hours = ? WHERE week = ?', (oldstudy + study, week_number()))
cur.execute('UPDATE ' + utility.db_name +' SET bjj = ? WHERE week = ?', (oldtrain + train, week_number()))

conn.commit()
cur.close()

print('Database updated')

# prints days left in year
today = datetime.date.today()
future = datetime.date(2020, 12, 27)
diff = str(future - today)
print(diff[:3], 'days left in year')
