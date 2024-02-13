import datetime

today = datetime.datetime.today()

print(today)

year= lambda x: x.year
month= lambda x: x.month
day= lambda x: x.day
time= lambda x: x.time()

print(year(today))
print(month(today))
print(day(today))
print(time(today))
