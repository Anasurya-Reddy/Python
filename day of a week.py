import datetime
d = int(input('Enter the date:'))
m = int(input('Enter the month:'))
y = int(input('Enter the year:'))
date=datetime.date(y,m,d)
print(date.strftime('The weekday is %A'))
