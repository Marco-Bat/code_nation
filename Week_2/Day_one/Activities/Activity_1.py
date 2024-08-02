#Create a variable called password.
# Check how many letters are in the password, if there are fewer than 8 print that the password is too short.
# Otherwise print the password.

password = input("enter your password->>>")

if len(password) >= 8:
    print("Password accepted")
else:
    print("The password is too short")
    
