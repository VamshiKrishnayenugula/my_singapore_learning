from datetime import datetime
print('get full date and time')
time_now = datetime.now()
print(time_now)

print('get only time in  a specified manner')

print(time_now.strftime('%H:=%M:%S'))

from datetime import date

print('get only date :' , date.today())

"""get the current time 
using the datetime() module. The strftime() method formats 
time for the desired output. This code breaks down how you can 
use the datetime module with the strftime() method to get a 
formatted string of time in hours, minutes, and seconds format.

What if we want to return today’s date? We can use the date class 
from the datetime module. We use the today() method. 
"""