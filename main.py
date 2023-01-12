
# Iterating Through an Iterator and for loop.

# the next() function to return the next item in the sequence.

# define a list
my_list = [4, 7, 0]

# created an iterator from the list using the iter() method object.
iterator = iter(my_list)

# The next() function to retrieve the elements of the iterator in sequential order.
# get the first element of the iterator
print(next(iterator))  # O/P : 4

# get the second element of the iterator
print(next(iterator))  # O/P : 7

# get the third element of the iterator
print(next(iterator))  # O/P : 0

#-----------------Using for Loop--------------------------

# A more elegant way of automatically iterating is by using the for loop.

# define a list
my_list = [4, 7, 0]

for element in my_list:
    print(element)

# Output :
# 4
# 7
# 0
