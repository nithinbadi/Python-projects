import datetime as dt
i = input('Enter date in YYYY-MM-DD format: ')
year,month,day=map(int,i.split('-'))
y=dt.date(year,month,day)
j = input('Enter date in YYYY-MM-DD format: ')
year2,month2,day2=map(int,j.split('-'))
x=dt.date(year2,month2,day2)
print(abs(x-y))
