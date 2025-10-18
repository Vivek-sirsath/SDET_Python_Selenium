# 5) finditer()
# - Returns matching details of --> Matching Objects, start() index, end() index
# - It returns multiple matches if present.
# Also it returns the starting index position and ending index position of the matching object.
# String indexing starts from 0 - 'zero'

import re

print("========= Find all contact numbers and all their positions in a string ========")

text = "My contact numbers are 9856425174 and 9475896213"
pattern = r"\d{10}"
numbers = re.finditer(pattern,text)

# print(numbers)   # <callable_iterator object at 0x0000020148E144F0>

for number in numbers:
    print(number.group(), number.start(), number.end())

# 9856425174 23 33
# 9475896213 38 48

print("========= Find all hashtag and all their positions in social media account ========")

post = "Loving the #sunset and #beachvibes on this amazing trip! #travel #nature"
pattern = r"#\w+"
matches = re.finditer(pattern,post)

for match in matches:
    print(match.group(), match.start(), match.end())






