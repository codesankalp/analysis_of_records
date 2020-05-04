"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

tel_num = list()
for i in range(len(texts)):
    tel_num.append(texts[i][0])
    tel_num.append(texts[i][1])

for i in range(len(calls)):
    tel_num.append(calls[i][0])
    tel_num.append(calls[i][1])
    
print("There are {} different telephone numbers in the records".format(len(set(tel_num))))
    