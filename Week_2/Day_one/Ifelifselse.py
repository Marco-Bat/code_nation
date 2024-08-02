#Create a variable called password.
# Check how many letters are in the password, if there are fewer than 8 print that the password is too short.
# Otherwise print the password.

password = input("enter your password->>>")

if len(password) >= 8:
    print("Password accepted")
else:
    print("The password is too short")

#---------------------------------------
#           activity 2 
# --------------------------------------

# Create a variable called num.
# Check if the variable is divisible by 3 or 5.
# If it is print “This number is divisible by 3 or 5” to the terminal.
# Otherwise print “This number is not divisible by 3 or 5”.

num = int (input("please enter any number "))

if num % 3 == 0 or num % 5 == 0:
    print(f"{num} is divisible by 3 or 5")
else:
    print(f"{num} is not divisible by 3 or 5")

#---------------------------------------
#           activity 3 
# --------------------------------------

num = 21

# we to verify the both condition we neeed to if / and in order to get back a number dividible by 3 and 7 
if num % 3 == 0 and num % 7 == 0:
    print("fizzbuzz")
elif num % 3 == 0:
    print("fizz")
elif num % 7 ==0:
    print("buzz")

else:
    print(num)

#---------------------------------------
#           activity 4 
# --------------------------------------

print("What is the capital of England?") 
# it was not a string 
answer= input("Type your answer here >> ")
# to return London or london I have use or  
if answer == "London" or answer == "london":
# print(f) gives back a more accurate answer
    print(f"Correct!The answer is {answer}") 
else:
    print(f"Incorrect, the answer is'London',not {answer}")

#---------------------------------------
#           activity 5 
# --------------------------------------

# Create a variable called word that takes a string.
# Create an if statement that checks if the last letter is the same as the first.
# If it is return true, otherwise return false.

word = input("Type any word and check 1st and the last character are the same >>> ").lower().strip()

#if I use a space in the terminal the program is recognising the first 
# letter as a space and not as an actual letter
if word [0] == word [-1]:
    print("True")
else:
    print("False")

#---------------------------------------
#           activity 5 stretch
# --------------------------------------   

# Create a variable called word that takes a string.
# Create an if statement that checks if the whole string is a palindrome 
# (reads the same forwards as it does backwards e.g. abba)

# word = "radar"
# if word == word [::-1]:
# #::-1 read the word from right to left
#     print(f"{word} Is a palindrome")
# else:
#     print(f"{word} is not a palindrome")

word = input("check if the entered word is a palindrome>>>> ").lower().strip()
# [::-1] reads backward
if word == word [::-1]:
    print(f"{word} is a palindrome")

else:
    print(f"{word} is not a palindrome")