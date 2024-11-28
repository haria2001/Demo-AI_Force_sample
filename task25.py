# Check if the password has at least 1 capital case letter, 1 number, 1 small case 
# letter and one special character

import re
password = input("Enter the password: ")
if (re.search(r'[A-Z]', password) and re.search(r'[0-9]', password) and re.search(r'[@#$%^&+=]', password)):  
   print("Password is valid.")
else:
   print("Password is invalid. It must contain:")
   print("At least one uppercase letter")
   print("At least one lowercase letter")
   print("At least one number")
   print("At least one special character (@#$%^&+=)")