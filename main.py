
# Python Generators.

# A generator is a function that returns an iterator that produces a sequence of values when iterated over.
# Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.
# In Python, similar to defining a normal function, we can define a generator function using the
# def keyword, but instead of the return statement we use the yield statement.

# Syntax : def generator_name(arg):
#                   statements
#                   yield something --> the yield keyword is used to produce a value from the generator.

def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1

# iterate over the generator object produced by my_generator using next() method
generator = my_generator(3)
print(next(generator))  # O/P: 0
print(next(generator))  # O/P: 1
print(next(generator))  # O/P: 2


# iterate over the generator object produced by my_generator
for value in my_generator(3):

    # print each value produced by generator
    print(value)

# Output :
# 0
# 1
# 2
