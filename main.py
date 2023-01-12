
# Python  r prefix before RegEx.

# A Regular Expression (RegEx) is a sequence of characters that defines a search pattern.
# Python has a module named "re" to work with RegEx.
# When r or R prefix is used before a regular expression, it means raw string. For example, '\n' is a new
# line whereas r'\n' means two characters: a backslash \ followed by n.



#------Python  r prefix before RegEx--------------------


import re    # importing the re module

string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string) # escaping the \n and \r using r prefix
print(result)

# Output: ['\n', '\r']



