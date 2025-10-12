# 3) search()

# - Finds the first occurrence of a pattern in a string. If found, returns a matching object otherwise returns 'None'.
import re

# CHECK IF AN EMAIL CONTAINS "@gmail.com"

# Case 1 (Valid Domain)

email = "mmr123@gmail.com"
pattern = "@gmail.com"
searchObj = re.search(pattern,email)
if searchObj:
    print(searchObj.start())    # 6 --> start() returns the index from where the pattern starts.
else:
    print("Invalid gmail address")



# Case 2 (Invalid Domain)

email = "mmr123@gmail.co.in"
pattern = "@gmail.com"
searchObj = re.search(pattern,email)
if searchObj:
    print(searchObj.start())
else:
    print("Invalid gmail address")   # Invalid gmail address

#              X---------------X---------------X---------------X---------------X



# CHECK IF THE URL CONTAINS "https"

# Case 1 (Valid Protocol)

url = "https://www.redbus.com"
pattern = "https"
obj2 = re.search(pattern,url)
if obj2:
    print(obj2.group())   # https
else:
    print("Invalid protocol")


# Case 2 (Invalid Protocol)

url = "jttps://www.redbus.com"
pattern = "https"
obj2 = re.search(pattern,url)
if obj2:
    print(obj2.group())
else:
    print("Invalid protocol")   # Invalid protocol



