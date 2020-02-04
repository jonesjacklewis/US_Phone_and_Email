#! python3
# This project will extract US style phone numbers and email address from the clipboard
import re  # Used to use Regular Expressions [a regex]

import pyperclip  # Used to manipulate the clipboard

# Create a regex for phone number
phoneRegex = re.compile(r'''
#415-555-0000, 555-0000, (415) 555-0000, 55-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?    #area code optional
(\s|-)    #first separator
\d\d\d    #first 3 digits
-   #seperators
\d\d\d\d    #last 4 digits
(((ext(\.)?\s)|x)    #extension word-part (optional)
(/d{2,5}))? #extension number-part (optional)
)''', re.VERBOSE)

# Create a regex for an email
emailRegex = re.compile(r'''
#some.+_thing@something.com

[a-zA-z0-9_.+-]+    #name part
@                    #@ symbol
[a-zA-z0-9_.+-]+     #domain name part
''', re.VERBOSE)

# Get text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

all_phone_Numbers = []
for phoneNumber in extractedPhone:
    all_phone_Numbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard
results = "\n".join(all_phone_Numbers) + "\n" + "\n".join(extractedEmail)
pyperclip.copy(results)

# Output Done
print("Done")

