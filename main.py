
# Python Property Getter.

# In Python, a getter is a method that is used to retrieve the value of an attribute.
# It is defined using the @property decorator, which allows the method to be accessed like an attribute.
# the @property decorator is a built-in function that allows us to define methods that can be accessed like an attribute.

#------Python Property Getter--------------------

class Student:
    def __init__(self, first_name):
        self.first_name = first_name

    # define getter method
    @property    #  @property decorator to access get_name() like an attribute.
    def get_name(self):
        return self.first_name

# create a new Student object
student = Student("Bridgelabz")

# access the first name using data property
print("Student first_name : ", student.first_name)

# access the first name using getter property
print("Student first_name : ", student.get_name)

# Output :
# Student first_name :  Bridgelabz
# Student first_name :  Bridgelabz