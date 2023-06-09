import time
from datetime import datetime, date

dt = datetime(year=2023, month=5, day=5, hour=10, minute=40)
print(dt)
print(type(dt))

current_time = time.ctime()
current_datetime = datetime.now()
print(current_time, current_datetime)


d = date(year=2021, month=6, day=25)
print(d)

current_date = date.today()
print(current_date)
