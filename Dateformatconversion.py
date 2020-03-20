# function to convert user provided date format

from datetime import datetime

# get input from user
date_input = input('Enter a date(MM/DD/YYYY): ')

obj = datetime.strptime(date_input, '%m/%d/%Y')

print(obj)

print(obj.strftime('%m%d%y'))