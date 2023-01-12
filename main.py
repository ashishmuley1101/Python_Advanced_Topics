
# Python RegEx match.group() method.

# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
# Python has a module named "re" to work with RegEx.
# The group() method returns the part of the string where there is a match.
# Syntax : match = re.search(pattern, str)
#          print(match.group())

#------Python RegEx match.group()--------------------


import re    # importing the re module

string = '2102 1111,123 45'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string)

if match:
  print(match.group())    # return the matching group
else:
  print("pattern not found")

# Output: 102 11



