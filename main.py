
# Python decorator Return a Function as a Value

# In Python, a decorator is a design pattern that allows you to modify the functionality
# of a function by wrapping it in another function.
# The outer function is called the decorator, which takes the original function as an
# argument and returns a modified version of it.

#------Return a Function as a Value---------------------

# Syntax : def fun1(arg):
#                statements

#          def fun2(arg):
#                 statement
#          return fun2

#          variable = fun1(arg)

#          print(variable())

def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello

greet = greeting("Bridgelabz")
print(greet())

# Output: Hello, Bridgelabz!
