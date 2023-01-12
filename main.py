
# Python RegEx re.sub() method.

# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
# Python has a module named "re" to work with RegEx.
# The method returns a string where matched occurrences are replaced with the content of replace variable
# Syntax : re.sub(pattern, replace, string)

#------Python RegEx re.sub()--------------------


import re    # importing the re module

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.sub(pattern, replace, string)
print(new_string)

# Output: abc12de23f456



