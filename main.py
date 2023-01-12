
# Python RegEx re.subn() method.

# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
# Python has a module named "re" to work with RegEx.
# The re.subn() is similar to re.sub() except it returns a tuple of 2 items containing the new string and the number of substitutions made.

# Syntax : re.subn(pattern, replace, string)

#------Python RegEx re.subn()--------------------


import re    # importing the re module

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.subn(pattern, replace, string)
print(new_string)

# Output: ('abc12de23f456', 4)



