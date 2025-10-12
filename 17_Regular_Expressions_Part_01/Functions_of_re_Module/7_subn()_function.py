# 7) subn()
# - Same as sub() but it returns a tuple consist of 'Modified string' and  'No. of replacements'
#   (a,b)
#   a = Modified string
#   b = Number of replacements made.

import re

# Formatting a phone number to a standard format - (XXX) XXX-XXXX
text = "Call me on 984-562-1473 or 874-692-1126."
pattern = r"(\d{3})-(\d{3})-(\d{4})"
formatted_numbers = re.subn(pattern,r"(\1) (\2)-(\3)", text)
print(formatted_numbers)

# ('Call me on (984) (562)-(1473) or (874) (692)-(1126).', 2)   ----->   Tuple
