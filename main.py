
# Python RegEx re.split() method.

# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
# Python has a module named "re" to work with RegEx.
# The re.split method splits the string where there is a match
# and returns a list of strings where the splits have occurred.
# If the pattern is not found, re.split() returns a list containing the original string.

#------Python RegEx re.split()--------------------


import re    # importing the re module


string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string)
print(result)

# Output: ['Twelve:', ' Eighty nine:', '.']



