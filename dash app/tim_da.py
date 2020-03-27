import datetime
from datetime import date

date_object = datetime.date.today()
print(date_object)

timestamp = date.fromtimestamp(1367444364)
print("Date =", timestamp)

# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

import time

print("This is printed immediately.")
time.sleep(5.4)
print("This is printed after 2.4 seconds.")

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
