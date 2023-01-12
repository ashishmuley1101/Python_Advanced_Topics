
# Python decorator(Pass Function as Argument).

# In Python, a decorator is a design pattern that allows you to modify the functionality
# of a function by wrapping it in another function.
# The outer function is called the decorator, which takes the original function as an
# argument and returns a modified version of it.

#------Pass Function as Argument---------------------

# Syntax : def fun1(arg):
#                statements

#          def fun2(arg):
#                 statements

#          variable = fun2(fun1(arg))

#          print(variable)

def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)   # calling the add()

result = calculate(add, 4, 6) # calling the calculate(add()) passing the add() as argument
print(result)     # O/P : 10

