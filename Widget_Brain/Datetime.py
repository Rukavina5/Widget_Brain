import datetime

d = datetime.date(2018, 3, 3)

print (d)

mill = datetime.date(2000, 1, 1)
delta = datetime.timedelta(100)
print(mill + delta)

launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

print(launch_date)
print(launch_time)
print(launch_datetime)

moon_landing = '7/20/1969'
moon_landing_datetime = datetime.datetime.strptime(moon_landing, '%m/%/d/%Y')
print(moon_landing)
