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
tel_num = list()
call_time = dict()

for i in range(len(calls)):
    tel_num.append((calls[i][0],calls[i][3]))
    tel_num.append((calls[i][1],calls[i][3]))

for num,time in set(tel_num):
    if num not in call_time: call_time[num] = 0
    else: call_time[num] += int(time)
max = 0
for k,v in call_time.items():
    if v>max:
        info = k
        max = v

print(f"{info} spent the longest time, {max} seconds, on the phone during September 2016.")
    
