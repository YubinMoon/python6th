from datetime import timedelta, date, datetime

td = timedelta(days=10)
print(td)

d1 = date(2023, 5, 5)
d2 = date(2023, 6, 9)

print(d1 == d2)
print(d1 < d2)
print(d1 > d2)

dt = datetime.today()

formatted_datetime = dt.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)
