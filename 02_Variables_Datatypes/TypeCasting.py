# TYPE CASTING
# Converting from one data type to another data type
# Functions to convert any data type --> int(), float(), complex(), bool(), str()

a = 10
print(type(a))  # <class 'int'>
b = str(a)  # passing a as an argument.
print(type(b))  # <class 'str'>

print("--------------------")

x = "10"
print(type(a))  # <class 'str'>
y = int(x)
print(type(y))  # <class 'int'>

print("--------------------")

p = "5"
print(type(int(p)))  # <class 'int'>

print("--------------------")

z = "Ten"
print(type(z))  # <class 'str'>
print(type(int(z)))  # ValueError: invalid literal for int() with base 10: 'Ten'








