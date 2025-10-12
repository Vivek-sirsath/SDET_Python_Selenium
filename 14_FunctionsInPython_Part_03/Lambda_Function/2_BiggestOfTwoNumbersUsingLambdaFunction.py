# Find biggest of 2 numbers using Lambda Function

"""
NOTE: Since lambda functions are nameless anonymous functions, we store them in a variable
      that will act as a function name.

      Instead of 'def' we will use 'lambda' keyword.
"""

# Normal Function

def findBiggest(a,b):
    if a>b:
        print(a)
    else:
        print(b)


findBiggest(45,20)
findBiggest(20,50)


# Lambda Function

# SYNTAX :-
#        lambda arguments_list: expression

s = lambda a,b: a if a>b else b  # Ternary Operator
print(s(300,20))
print(s(60,120))




























