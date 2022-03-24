from datetime import datetime, timedelta
from random import randint


def vinaigrette(date1, date2):
    start = datetime.strptime(date1, "%Y-%m-%d")
    finish = datetime.strptime(date2, "%Y-%m-%d")
    diff = finish-start
    r = randint(0,diff.days)
    delta = timedelta(days=r)
    randDate = start+delta
    day = randDate.strftime('%a')
    if day == "Mon":
        print("אין לי ויניגרט!")