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


# Telemarketers' numbers have no parentheses or space, but they start
# with the area code 140.

leads = set()
telemarketers = set()

for call in calls:
    leads.add(call[1])

for text in texts:
    leads.add(text[1])

for call in calls:
    if not call[0] in leads:
        telemarketers.add(call[0])

for text in texts:
    if text[0] in telemarketers:
        telemarketers.remove(text[0])


sorted_telemarketers = sorted(telemarketers)

print(f"These numbers could be telemarketers: ")
for telemarketer in sorted_telemarketers:
    print(telemarketer, sep = '\n')

