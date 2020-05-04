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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
possible_tele = set()           # tele => telemarketers
not_tele = set()

for i in texts:
    not_tele.add(i[0])
    not_tele.add(i[1])
for i in calls:
    not_tele.add(i[1])
    possible_tele.add(i[0])

tele = []
for i in possible_tele:
    if i not in not_tele:
        tele.append(i)
        
tele = sorted(tele)
print("These numbers could be telemarketers: ")
print("\n".join(tele))
