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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_record_text = texts[0]
last_record_calls = calls[-1]

incoming_num_text, answering_num_text, timestamp_text = first_record_text
incoming_num_call, answering_num_call, timestamp_call, duration_call = last_record_calls

print(f"First record of texts, {incoming_num_text} texts {answering_num_text} at time {timestamp_text}")

print(f"Last record of calls, {incoming_num_call} calls {answering_num_call} at time {timestamp_call}, lasting {duration_call} seconds")


