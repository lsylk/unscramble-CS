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

# Assuming that records is referring to all numbers appearing on the texts and calls. 

phone_book = {}

for text in texts:
    if text[0] not in phone_book:
        phone_book[text[0]] = 1
    if text[1] not in phone_book:
        phone_book[text[1]] = 1

for call in calls:
    if call[0] not in phone_book:
        phone_book[call[0]] = 1
    if call[1] not in phone_book:
        phone_book[call[1]] = 1

total_contacts = len(phone_book)

print(f"There are {total_contacts} different telephone numbers in the records.")