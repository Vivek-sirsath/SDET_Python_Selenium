a = 10
b = 15.5
c = "Selenium"
d = 'k'

# type() - Returns the data type
print(a) # 10
print(b) # 10.5

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'str'>

# In Python every dataType has its own class.

p = q = 100

print(p)  # 100
print(q)  # 100

a,b = 5,10 # a and b redefined
print(a)  # 5
print(b)  # 10

# 1st way :-
# Swapping data using + and - operator
a = a+b   # 5+10=15
b = a-b   # 15-10=5
a = a-b   # 15-5=10
print(a)
print(b)

# 2nd Way :-
# Swapping data using * and // operator
a = a*b
b = a//b
a = a//b
print(a)
print(b)

# 3rd Way :-
m = 1
n = 2
print("Before swapping :", m ,n)

n,m = m,n
print("After swapping :", m ,n)

################################################################
# del Keyword :-
# If we delete anything in Python, it will be permanently deleted.
# 'del' is an unbind operation.

x = 30
y = 12
print(x)
del x
#print(x)   # NameError: name 'x' is not defined

# Instead of 'del' we can use 'None' keyword
# None --> Nothing
# If we assign 'None' to any variable,
# a = None  ---> Eligible for garbage collection. (Ready for delete operation)
# a = None (occupy 16 to 24 bytes of Python memory)

x = 56   # Here x is redefined after deleting
print(x)
x = None
print(x)  # None
#print(x + y)   # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

################################################################
# CODE STUDIO :-

a = 15
b = 10

print(a+b)  # 25

a = 7
b = 8

print(7+8)  # 15




