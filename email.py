# # Email Validation
# 

import re

#compiling regex
check = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

print("Enter your Email")
#user input
email = input()

#searching regex
a = check.search(email)

#validation condition
if a:
  print("Yes, the email is valid!")
else:
  print("Not valid")
