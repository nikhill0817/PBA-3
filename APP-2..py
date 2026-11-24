import re

password = input("Enter password: ")

pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*!]).+$'

if re.match(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")