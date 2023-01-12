
# Python @ Symbol With Decorator Function.

# Instead of assigning the function call to a variable, Python provides a much more
# elegant way to achieve this functionality using the @ symbol.

#------@ Symbol With Decorator Function.--------------------

def make_pretty(func):
    # define the inner function
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()

    # return the inner function
    return inner


# define ordinary function
# decorate the ordinary function
@make_pretty  # Calling the make_pretty using @ symbol and passing ordinary() as argument.
def ordinary():
    print("I am ordinary")

ordinary()

# Output:
# I got decorated
# I am ordinary
