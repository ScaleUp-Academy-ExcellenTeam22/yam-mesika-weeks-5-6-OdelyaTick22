from datetime import datetime, timedelta
from random import randint


def vinaigrette(start_date: str, end_date: str) -> None:
    """
    A function that randomly rolls a new date that is between the two dates that the user entered as input.
    If the day drawn is Monday, the program will print "I do not have a vinaigrette".
    @param start_date: date in the configuration: YYYY-MM-DD.
    @param end_date: date in the configuration: YYYY-MM-DD.
    @return: None
    """

    start = datetime.strptime(start_date, "%Y-%m-%d")
    finish = datetime.strptime(end_date, "%Y-%m-%d")
    difference = finish - start
    random_number = randint(0, difference.days)
    delta = timedelta(days=random_number)
    rand_date = start + delta
    day = rand_date.strftime('%a')
    if day == "Mon":
        print("אין לי ויניגרט!")


"""
An example usage:
vinaigrette("2001-03-02", "2022-03-27")
return None Because the date drawn is not Monday
"""
