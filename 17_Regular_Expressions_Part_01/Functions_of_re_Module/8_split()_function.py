# 8) split()
# - This function splits the string and returns the list of tokens (words).

import re

# Split a sentence into words. (Based on space '\s' character)
text = "Python  is      very   interesting"
pattern = r"\s+"    # '+' is quantifier for any number of spaces in string.
print(re.split(pattern,text))   # ['Python', 'is', 'very', 'interesting']


# Split CSV line in a list of values.
text = "apple, kiwi, grapes, banana, mango, orange"
pattern = r",\s"
print(re.split(pattern,text))    # ['apple', 'kiwi', 'grapes', 'banana', 'mango', 'orange']


# Split the string with any number of spaces including zero space. Based on (_) character.
text = "IMG_  12062025_  121045_      NYC"
pattern = r"_\s*"
print(re.split(pattern,text))    # ['IMG', '12062025', '121045', 'NYC']











