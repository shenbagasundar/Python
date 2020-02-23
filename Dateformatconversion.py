#!/bin/python3
# function to convert user provided date format

from datetime import datetime

#get input from user
date_input = input('Enter a date(MM/DD/YYYY): ')
print(date_input)
object = datetime.strptime(date_input, '%m/%d/%Y')
print(object)
print(object.strftime('%Y%m%d'))

#end