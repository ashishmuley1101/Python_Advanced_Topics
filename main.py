
# Python Decorating Functions with Parameters.

# Instead of assigning the function call to a variable, Python provides a much more
# elegant way to achieve this functionality using the @ symbol.

#------Decorating Functions with Parameters--------------------

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide by 0")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2, 5)

divide(2, 0)

# Output:
# I am going to divide 2 and 5
# 0.4
# I am going to divide 2 and 0
# Whoops! cannot divide by 0
