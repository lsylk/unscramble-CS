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

call_durations = {}

for call in calls:
    duration = int(call[-1])

    if call[0] in call_durations:
        call_durations[call[0]] += duration
    else:
        call_durations[call[0]] = duration

    if call[1] in call_durations:
        call_durations[call[1]] += duration
    else:
        call_durations[call[1]] = duration
    
longest_call = {
    "phone_number": None,
    "duration": 0
}

for call in call_durations:
    if call_durations[call] > longest_call["duration"]:
        longest_call["phone_number"] = call
        longest_call["duration"] = call_durations[call]

print(f"{longest_call['phone_number']} spent the longest time, {longest_call['duration']} seconds, on the phone during September 2016.")