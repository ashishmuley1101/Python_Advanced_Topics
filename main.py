
# Python RegEx re.search() method.

# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
# Python has a module named "re" to work with RegEx.
# The re.search() method takes two arguments: a pattern and a string. The method looks for the first
# location where the RegEx pattern produces a match with the string. If the search is successful,
# re.search() returns a match object; if not, it returns None
# Syntax : match = re.search(pattern, str)

#------Python RegEx re.search()--------------------


import re    # importing the re module

string = "Welcome to BridgeLabz !"

# check if 'Welcome' is at the beginning or start with
match = re.search('\AWelcome', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")

# Output: pattern found inside the string



