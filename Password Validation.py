
# ## Conditions for a valid password are:
# 
# #### Should have at least one number.
# #### Should have at least one uppercase and one lowercase character.
# #### Should have at least one special symbol.
# #### Should be between 6 to 20 characters long.


# ?= poistive look head 
import re
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
      
# compiling regex 
pat = re.compile(reg) 

print("Enter a password ")
#input
passwd = input()

# searching regex                  
mat = re.search(pat, passwd) 
      
# validating conditions 
if mat: 
   print("Password is valid.") 
else: 
   print("Password invalid !!") 
  



