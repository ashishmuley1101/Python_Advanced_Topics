
# Python RegEx re.match()

# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
# Python has a module named "re" to work with RegEx.

#------Python RegEx re.match()--------------------


import re    # importing the re module

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:   # if pattern match to test_string return true or flase
  print("Search successful.")
else:
  print("Search unsuccessful.")

