print("=============== Data Types In Python ====================")

x = 10  # Integer - int
y = 20.5   # Float - float
s = "Hello"   # String - str
c = 'A'    # Character as String - str
b = True  # Boolean - bool
xx = "12345"  # Numeric String - str
yy = [1,2,3,4,5]  # list
zz = (1,2,3,4,5)  # tuple


print(type(x))
print(type(y))
print(type(s))
print(type(c))
print(type(b))
print(type(xx))
print(type(yy))
print(type(zz))

print("================ Data Types by indently.io (YouTube) ===============")

# Data Types by indently.io (YouTube)

number : int =  10
decimal : float = 2.5
text : str = "Hello, World"
active : bool = False or True

names : list = ["Bob", "Anna", "John"]  # --> mutable, Duplicates allowed
coordinates : tuple = (1.5,2.5)  # --> immutable
unique : set = {2,5,7,6}  # --> Duplicates not allowed
data : dict = {'name' : 'Bob', 'age' : 20}  # --> stores data with key-value pairs.

print("=============== Variable Declaration In Python ====================")

# Variable Declaration :
# a = 15
# b = 54
# s = "Nisha"

# We can declare multiple variables in single line too.

a,b,s = 10,20,"Nisha"
print(type(a))
print(type(b))
print(type(s))

print("=============== Swapping of variables ====================")

x = 3
y = 5
print(x,y)  # 3 5

# SWAPPING

y,x = x,y
print(x,y)  # 5 3

print("=============== Deleting variables ====================")
del b
# print(b)  # NameError: name 'b' is not defined
print("================ Defining variables using Type annotation ================")

# Defining variables using Type annotation

name = "Bob"   # Allowed, No need to specify string data type
age = 'Eleven'  # Editor not giving any warning, Wrong data type inserted

# Editor can give warning if we specify data types with declaration
# age: int = 'Eleven'  # --> Here editor is giving warning (Expected type 'int', got 'str' instead)
AGE:int = 13   # --> By this way we can not insert wrong data by mistake.
print(AGE)
Date:int = True
print(Date)

print("=================================== Final Variable ==========================================")

# Creating Constants

from typing import Final

VERSION: Final[str] = '1.0.13'  # --> Correct way to define constants.
PI: Final[float] = 3.14   # --> Correct way to define constants.

# We can still change the values of constants but editor will give the warnings, if we define as above.
PI = 2.20   # WARNING - 'PI' is 'Final' and could not be reassigned

print("===================================== Reusable function ========================================")

# How we can create reusable code using function?

from datetime import datetime

# print("This is the current date and time:")
# print(datetime.now())

# print("This is the current date time:") # ..... statement changed
# print(datetime.now())

# To print again we have to copy again. Also, the statement can be changed everytime.
# To avoid this, we can use function.
# In Python function can be defined using 'def'

def show_datetime() -> None :
    print("This is the current date and time:")
    print(datetime.now())

show_datetime()
show_datetime()
show_datetime()   # This way we can use any function multiple times.

print("==================================== Parameterized function =========================================")

# Parameterized function
def greet(surname: str) -> None:
    print(f"Ciao, {surname}!")

    # We can use single quotes also ('') # Replace 'Hello' by 'Ciao'
    # Reflect the changes at all places.

greet("Shirsath")
greet("Patil")

# Instead of 'Hello', we can change to 'Ciao'

print("==================================== Functions can return some data =========================================")

# Functions can return some data
def add(x: float, y: float) -> float:
    return x + y

print(add(1,2))  # 3

print("=================================== Classes and Objects ==========================================")

# Classes and Objects
# Car is class and volvo, bmw are objects of class

class Car:
    def __init__(self, color: str, horsepower: int) -> None:
        self.color = color
        self.horsepower = horsepower  # self refers to instance of class

volvo: Car = Car("red", 200)  # This is Object of a Class, volvo is name of object
print(volvo.color)
print(volvo.horsepower)

bmw: Car = Car("blue", 240)
print(bmw.color , bmw.horsepower)

print("==================================== Methods =========================================")

# Methods
class Car:
    def __init__(self, brand: str , hp: int):
        self.brand = brand
        self.hp = hp

    def drive(self) -> None:
        print(f'{self.brand} is driving!')

    def get_info(self, var: int) -> None:
        print(f'{self.brand} with {self.hp} hp')

audi: Car = Car('audi', 200)
audi.drive()  # audi is driving!
audi.get_info(10)  # audi with 200 hp

# We can create multiple instances of Car class
ford: Car = Car('ford', 145)
ford.drive()
ford.get_info(10)




