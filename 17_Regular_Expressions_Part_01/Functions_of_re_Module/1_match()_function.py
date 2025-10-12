# 1) match()

# - Checks if a string starts with a pattern. Returns a matching object if found, otherwise None.
# - Only matches start of a string.

print("======== Check if a filename starts with a letter (Either lowercase OR uppercase) ========")
import re  # re - regular expression module

# Case 1 (Valid Filename)

filename = "Report2025.pdf"
pattern = "[a-zA-Z]"
matchObj = re.match(pattern,filename)

if matchObj:
    print("Valid file name :", matchObj.group())   # Valid file name : R
else:
    print("Invalid file name, it should start with a letter.")



# Case 2 (Invalid Filename)

filename = "1Report2025.pdf"
pattern = "[a-zA-Z]"
matchObj = re.match(pattern,filename)

if matchObj:
    print("Valid file name :", matchObj.group())
else:
    print("Invalid file name, it should start with a letter.")  # Invalid file name, it should start with a letter.

#              X---------------X---------------X---------------X---------------X

print("============ Check if a username starts with a character ============")

# Case 1 (Valid Username)

username = "akg4512"
pattern = "[a-zA-Z]"
matchObj = re.match(pattern,username)
print(matchObj.group())  # a



# Case 2 (Invalid Username)

username = "1akg4512"
pattern = "[a-zA-Z]"
matchObj = re.match(pattern,username)
print(matchObj)  # None