# 2) fullmatch()

# - Checks if the entire string matches the pattern. Returns a full matching object if fully matched, otherwise return 'None'.
# - Matches the entire string.

# VALIDATE 10 DIGIT MOBILE NUMBER

import re

# Case 1 (Valid Number)

# Validate 10 digit mobile number
mobile_number = "9852476120"
pattern = r"\d{10}"    # Using r-String because it throws error. Because \ is an escape character.
obj = re.fullmatch(pattern,mobile_number)
print(obj.group())   # 9852476120


# Case 2 (Invalid Number)

# Validate 10 digit mobile number
mobile_number = "985246120"
pattern = r"\d{10}"    # Using r-String because it throws error. Because \ is an escape character.
obj = re.fullmatch(pattern,mobile_number)
print(obj)   # None


# Case 3 (We can use if else statement)

# Validate 10 digit mobile number
mobile_number = "985246120"
pattern = r"\d{10}"    # Using r-String because it throws error. Because \ is an escape character.
obj = re.fullmatch(pattern,mobile_number)

if obj:
    print(obj.group())
else:
    print("Mobile number not matching")  # Mobile number not matching

#              X---------------X---------------X---------------X---------------X

# VALIDATE VEHICLE REGISTRATION NUMBER

# Case 1 (Valid Number)

vehicle_number = "MH12AB5559"
pattern = "[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}"   # Using Character Classes
obj2 = re.fullmatch(pattern,vehicle_number)

if obj2:
    print(obj2.group())   # MH12AB5559
else:
    print("Wrong vehicle number")


# Case 2 (Invalid Number)

vehicle_number = "MH12AB555"
pattern = "[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}"   # Using Character Classes
obj2 = re.fullmatch(pattern,vehicle_number)

if obj2:
    print(obj2.group())
else:
    print("Wrong vehicle number")    # Wrong vehicle number






