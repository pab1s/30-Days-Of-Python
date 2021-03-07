from datetime import datetime, date

# Exercise 1
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(now, day, month, year, hour, minute, second, timestamp)

# Exercise 2
american_format = now.strftime("%m/%d/%Y, %H:%M:%S")
print(american_format)
print(f'{month}/{day}/{year}, {hour}:{minute}:{second}')

# Exercise 3
date_string = 'Today is 7 March, 2021'
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "Today is %d %B, %Y")
print("date_object =", date_object)

# Exercise 4
today = date.today()
new_year = date(year=2022, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

# Exercise 5
t1 = now
t2 = datetime(year = 1970, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t1 - t2
print('Time difference:', diff)

# Exercise 6
# We can use it to create a schedule, register logins and logouts...