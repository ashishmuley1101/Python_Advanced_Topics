
# Python RegEx re.findall() method.

# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
# Python has a module named "re" to work with RegEx.
# The re.findall() method returns a list of strings containing all matches.

#------Python RegEx re.findall()--------------------



import re    # importing the re module


string = 'hello 12 hi 891. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string)
print(result)

# Output: ['12', '891', '34']

