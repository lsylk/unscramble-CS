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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# bangalore_call_records = []

# for call in calls:
#   if "(080)" in call[0]:
#     bangalore_call_records.append(call)

# area_codes = set()

# def sanitize_area_codes(code):
#   return code.split(")")[0].replace("(", "")

# for call in bangalore_call_records:
#   if "("  in call[1] and ")" in call[1]:
#     code = sanitize_area_codes(call[1])
#     area_codes.add(code)

# # Part A Solution
# print(f"The numbers called by people in Bangalore have codes: ")
# for area_code in sorted(area_codes):
#   print(area_code, sep = '\n')


# total_bangalore_calls = len(bangalore_call_records)

# fixed_lines_counter = 0
# for record in bangalore_call_records:
#   if "(080)" in record[1]:
#     fixed_lines_counter +=1

# percentage_call = round((fixed_lines_counter / total_bangalore_calls) * 100, 2)

# # Part B Solution
# print("", sep = '\n')
# print(f"{percentage_call} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


############ REFACTORING:

total_bangalore_calls = 0
fixed_lines_counter = 0
area_codes = set()

def sanitize_area_codes(code):
  return code.split(")")[0].replace("(", "")

for call in calls:
  if "(080)" in call[0]:
    total_bangalore_calls += 1
    if "(080)" in call[1]:
      fixed_lines_counter +=1
    if "("  in call[1] and ")" in call[1]:
      code = sanitize_area_codes(call[1])
      area_codes.add(code) 

# Part A Solution
print(f"The numbers called by people in Bangalore have codes: ")
for area_code in sorted(area_codes):
  print(area_code, sep = '\n')
  

percentage_call = round((fixed_lines_counter / total_bangalore_calls) * 100, 2)

# Part B Solution
print("", sep = '\n')
print(f"{percentage_call} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")