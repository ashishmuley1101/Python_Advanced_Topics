
# Python Property Setter

# In Python, a setter is a method that is used to set the value of an attribute.
# It is defined using the @<property_name>.setter decorator,
# <property_name> name of the property that the setter is for.

#------Python Property Setter--------------------


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Define a "name" getter
    @property
    def name(self):    # getting the name variable
        return self._name

    # Define a "name"  as setter
    @name.setter       # setting the name variable with value
    def name(self, value):
        self._name = value

# Create a new Person object
person = Person("Jack", 30)

# Access and set the "name" attribute using the getter and setter
print("Old name :", person.name)           # calling the getter method
person.name = "Bridgelabz"   # calling the setter method passing the value
print("New name :", person.name)           # calling the getter method

# Output :
# Old name : Jack
# New name : Bridgelabz