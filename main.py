
# Python closure.

# Python closure is a nested function that allows us to access variables of the outer function even
# after the outer function is closed.

# Syntax : def outer_fun(arg):
#                statements

#                def inner_fun(arg):
#                     statements

#          variable = outer_fun(arg)  # calling the outer function

#          print(variable())         # calling the inner function

def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

# call the outer function
odd = calculate()

# call the inner function
print(odd())
print(odd())
print(odd())

# call the outer function again
odd2 = calculate()
print(odd2())

# Output :
# 3
# 5
# 7
# 3
