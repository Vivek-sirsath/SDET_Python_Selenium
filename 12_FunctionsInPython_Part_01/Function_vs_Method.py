
# FUNCTION vs METHOD :-
# -------------------

"""
# Function :-
-----------
A function is a block of reusable code defined with def (or lambda) keywords.
It does not belong to any object/class (though it can be inside a module).
It is called independently.
Example:

def greet(name):
    return f"Hello, {name}!"

print(greet("Vivek"))   # Calling a function

Here, greet is a function, not tied to any class or object.
==================================================================================
# Method :-
---------
A method is also a function — but it is defined inside a class.
It operates on instances (objects) of that class.
By convention, its first parameter is self (the object itself).
Example:

class Person:
    def greet(self, name):
        return f"Hello, {name}! I am {self}."

p = Person()
print(p.greet("Vivek"))   # Calling a method

Here, greet is a method of the Person class.
When we call p.greet("Vivek"), Python automatically passes self (the object p).
==============================================================================

But… in Python, they’re related :
-------------------------------

Technically, a method is just a function that belongs to a class.
Methods are stored as functions in the class, but when accessed via an object,
they become bound methods (with self automatically attached).

print(Person.greet)  # <function Person.greet at 0x...>
print(p.greet)       # <bound method Person.greet of <__main__.Person object>>

Summary:
--------
All methods are functions, but not all functions are methods.
A function stands alone, while a method lives inside a class and usually acts on an object (self).

"""

# FUNCTION IN PYTHON:-

def greet(name):
    print(f"Hello, {name}!")

greet("Vivek")   # Hello, Vivek!

print("==================================================")

# METHOD IN PYTHON :-

class Person:

    def greet(self,name):
        # return f"Hello, {name}! I am {self}."   # Hello, Ishita! I am <__main__.Person object at 0x000001737FC670E0>.
        return f"Hello, {name}"

p = Person()
print(p.greet("Ishita"))    # Hello, Ishita
print(p.greet("John"))   # Hello, John




