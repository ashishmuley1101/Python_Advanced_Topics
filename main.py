
# Python decorator function

# the decorators are used to modify the behaviour of function or class. In Decorators,
# functions are taken as the argument into another function and then called inside the wrapper function.

#------The decorator function.--------------------

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
def ordinary():
    print("I am ordinary")


# decorate the ordinary function
decorated_func = make_pretty(ordinary)   # Syntax : decorated_func = calling_fun(arg_fun)

# call the decorated function
decorated_func()

# Output:
# I got decorated
# I am ordinary
