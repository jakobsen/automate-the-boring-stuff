import pyperclip
import re


# Define the regular expressions
phoneNumberRegex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # optional seperator
    (\d{3})                         # First 3 digits
    (\s|-|\.)                       # seperator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2, 5}))? # extension
)""", re.VERBOSE)
emailRegex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    \.
    [a-zA-Z]{2,4}
)""", re.VERBOSE)

# Get the text from the clipboard and search it
textToSearch = str(pyperclip.paste())
matches = []
for groups in phoneNumberRegex.findall(textToSearch):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(textToSearch):
    print(groups)
    matches.append(groups)

# Print the results and copy the to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print("No phone numbers or emails found") 
