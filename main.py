
# Python Chaining Decorators .

# Multiple decorators can be chained in Python.
# To chain decorators in Python, we can apply multiple decorators to a single function
# by placing them one after the other, with the most inner decorator being applied first.

#------Python Chaining Decorators--------------------

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("\tHello Bridgelabz...!")

# Output:
# ******************************
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 	Hello Bridgelabz...!
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ******************************
