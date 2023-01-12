
# Python RegEx match.start(), match.end() and match.span() method.

# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
# Python has a module named "re" to work with RegEx.



#------Python RegEx match.start(), match.end() and match.span()--------------------


import re    # importing the re module

string = '2102 1111,123 45'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string)

if match:
  print(match.group())    # return the matching group
  print(match.start())  # return the starting index
  print(match.end())  # return the end index
  print(match.span())  # return the span() function returns a tuple containing start and end index of the matched part.
else:
  print("pattern not found")

# Output:
# 102 11
# 1
# 7
# (1, 7)



