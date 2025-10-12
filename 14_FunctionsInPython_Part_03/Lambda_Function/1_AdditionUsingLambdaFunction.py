# ADDITION USING LAMBDA FUNCTION :-

"""
NOTE: Since lambda functions are nameless anonymous functions, we store them in a variable
      that will act as a function name.

      Instead of 'def' we will use 'lambda' keyword.
"""

# Normal Function
def add(a,b):
    print(a+b)

add(30,20)  # 50

# Lambda Function

# SYNTAX :-
#        lambda arguments_list: expression

s = lambda a,b:a+b

print(s(15,10))  # 25



