"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from datetime import datetime as dt

call_time = {}

for i in calls:
    date = dt.strptime(i[2],"%d-%m-%Y %H:%M:%S")
    if date.year == 2016 and date.month == 9:
        if i[0] not in call_time:
            call_time[i[0]] = int(i[3])
        else:
            call_time[i[0]] += int(i[3])
        if i[1] not in call_time:
            call_time[i[1]] = int(i[3])
        else:
            call_time[i[1]] += int(i[3])
        

max = 0          
for key,value in call_time.items():
    if value>max:
        max = value
        num = key
    
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(num,max))
    
