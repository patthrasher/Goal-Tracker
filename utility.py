import datetime

# functions

def week_number() : # returns integer of current week number
    day = datetime.date.today()
    strday = str(day)
    lst = strday.split('-')

    year = int(lst[0])
    month = int(lst[1])
    day = int(lst[2])

    week = datetime.date(year, month, day).isocalendar()[1]
    return week

# variables

year = str(datetime.date.today().year)
db_name = 'Work_' + year
