
# Python Property Deleter

# A deleter in Python is a method that is used to delete a class attribute.
# It is defined using the @<property_name>.deleter decorator,
# <property_name> - name of the class attribute to delete.

#------Python Property Deleter--------------------


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # define a "name" getter
    @property
    def name(self):
        return self._name

    # define a "name" deleter
    @name.deleter   # Deleting the name attribute.
    def name(self):
        del self._name

# create a new Person object
person = Person("Bridgelabz", 30)

# access, set, and delete the "name" attribute
# using the getter, setter, and deleter
print(person.name)  # O/P : "Bridgelabz"

del person.name
print(person.name)  # Error -----> AttributeError: 'Person' object has no attribute '_name'

