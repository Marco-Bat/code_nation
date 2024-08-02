# # loops

# fav_drinks=[
#     "juice",
#     "tea",
#     "water"
# ]

# for i in fav_drinks:
#     print(i)

# fav_songs = [
#     "Bohemian Rhapsody",
#     "Halleluja",
#     "Time",
#     "Devil in Desguise",
#     "Perth",
#     "Dimmi che ci sei",
#     "Ancora",
#     "Don't stop me now",
#     "Bellissima",
#     "Cambiare"

# ]
# for i in fav_songs:
#     print(f"I love this song - {i} ")

# print(f"However, my favourite song among them is, {fav_songs[0]}." )

# -----------------------------------------------------------------------------------------------
# |                                 Challenge 1
# -----------------------------------------------------------------------------------------------
# Write a program that uses a for loop to print all the numbers from 1 to 10.

# num = [1,2,3,4,5,6,7,8,9,10]

# for i in num:
#     print(i)

# -----------------------------------------------------------------------------------------------
# |                                 Challenge 2
# -----------------------------------------------------------------------------------------------
# Create a program that prints all the even numbers between 1 and 20 using a for loop.

# num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# for number in num:
#     # using if and modulo == 0 it will print even numbers and giving us 
#     # the reminder 0 meanng is completely divided by 2
#     if number % 2 == 0:
#         print(number)

# -----------------------------------------------------------------------------------------------
# |                                 Challenge 3
# -----------------------------------------------------------------------------------------------
# # Write a program that calculates the sum of all the numbers from 1 to 100 using a for loop.

# # this variable will store the sum
# total = 0

# # use a for loop to iterate to the integers from 1 to 100 and the add them to the total
# # the range() function generates an immutable sequence of numbers.

# for i in range(1, 101):
# # the += operator is a shorthand for total = total + i
#   total += i

# print("The sum of numbers from 1 to 100 is:", total)

# 
# -----------------------------------------------------------------------------------------------
# |                                 Challenge 4
# -----------------------------------------------------------------------------------------------

# Create a program that takes a string input from the user and counts the number of vowels 
# (a, e, i, o, u) in the string using a for loop.

# vowels = "aeiou"

# user_input = input("Enter a string: ")  # Get input from the user

# vowel_count = 0
# for char in user_input.lower():  # Iterate over each character in lowercase
#     if char in vowels:
#         vowel_count += 1


# print("The number of vowels in the string is:", vowel_count)

# -----------------------------------------------------------------------------------------------
# |                                 Challenge 5
# |
# Write a program that prints the multiplication table of a number entered by the user 
# using a for loop.
# -----------------------------------------------------------------------------------------------

# total = 0 

# user_input = int (input("enter two numbers: ")) 

# # for 

# for i in range(2,12,2):
#     print(i)


# -----------------------------------------------------------------------------------------------
# |                                 Challenge 1 -  Range - 
# |
# Printing numbers from 1 to 10:
# Write a program that uses a range loop to print all the numbers from 1 to 10.
# -----------------------------------------------------------------------------------------------

# for i in range (1, 11):
#     print(i)

# -----------------------------------------------------------------------------------------------
# |                                 Challenge 2 -  Range - 
# |
# Create a program that prints all the even numbers between 1 and 20 using a range loop.
# -----------------------------------------------------------------------------------------------



# for number in range (1,21):
#     # using if and modulo == 0 it will print even numbers and giving us 
#     # the reminder 0 meanng is completely divided by 2
#     if number % 2 == 0:
#         print(number)


# -----------------------------------------------------------------------------------------------
# |                                 Challenge 3 -  Range - 
# |
# Write a program that prints all the numbers from 10 to 1 in reverse order using a range loop.
# -----------------------------------------------------------------------------------------------

# for number in range(10,0,-1): # start 10, stop: 0, step -1 is going backward 
#     print(number)


# -----------------------------------------------------------------------------------------------
# |                                 Challenge 4 -  Range - 
# |
# Create a program that calculates the sum of all the even numbers between 1 and 50 using a range loop.
# ----------------------------------------------------------------------------------------------


# sum = 0

# for num in range (0,51,2):
#     # using if and modulo == 0 it will print even numbers and giving us 
#     # the reminder 0 meanng is completely divided by 2
#     # if num % 2 == 0:
#         sum += num
    
# print("the sum the all even numbers from 1 to 50 is " , sum)


# answer = input("who oerdered a cortado?" ).lower().capitalize()

# if answer != "Alex":
#     print("Incorrect")

# else:
#     print("Correct")


# answer = input("who oerdered a cortado?" ).lower().capitalize()

# while answer != "Alex":
#     print("Incorrect")
#     answer = input("who oerdered a cortado?" ).lower().capitalize()

# else:
#     print("Correct")



# count = 0

# while count <10:
#     print(f"count is {count}")
#     count += 1



# -----------------------------------------------------------------------------------------------
# |                                 Activity 1 -  Hello World
# |
# Create a for loop that prints “hello world” 13 times.
# Now, convert this into a while loop that does the same job.
# ----------------------------------------------------------------------------------------------

# for i in range(1,14):
#     print("hello world")
# 
# count = 0   
# 
# while count < 13:
#     print ("hello World")
#     count+=1

# -----------------------------------------------------------------------------------------------
# |                                 Activity 2 -  Sum the list 
# |
# 
# Use a nested for loop to write a program which prints out the multiplication tables from 1 to 12.
# Include a line-break between each multiplication table to make it easier to read.
# ----------------------------------------------------------------------------------------------

# # Outer loop iterates through numbers 1 to 12 (multiplication table)
# for num in range(1, 13):
#   # Print the multiplication table header
#   print(f"Multiplication Table of {num}")

#   # Inner loop iterates through numbers 1 to 10 (multiplicands)
#   for i in range(1, 11):
#     # Calculate the product
#     product = num * i
#     # Print the multiplication in a formatted way
#     print(f"{num} x {i} = {product}")

#   # Print a line break after each table
#   print("------------------------------------------------")


# -----------------------------------------------------------------------------------------------
# |                                 Activity 3 -  10 seconds 
# |
# it’s t-minus 10 seconds to blast off, but there is no way to let anyone know!
# Write a blast off sequence using a while loop.
# Count down from 10 and after 1 print “blast off”.
# Before the countdown begins print “Countdown initiated, prepare for blast off”.
# 
# ----------------------------------------------------------------------------------------------

# for i in range (10,0,-1):
   
#    print(i)
#    if i == 1:
#       print("Blastoff")

# current_time=10

# while current_time > 0:
#     print(current_time)
    
#     current_time -= 1
#     if current_time == 0:
#         print("Blastoff")


# Countdown initiation message
print("Countdown initiated, prepare for blast off!")

# Set the starting point for the countdown
current_time = 10

# While loop for the countdown
while current_time > 0:
  # Print the current countdown time
  print(current_time)

  # Decrement the current time by 1
  current_time -= 1

# Blast off message after the countdown finishes
print("Blast off!")

# -----------------------------------------------------------------------------------------------
# |                                 Activity 4 -  Dog Imposters 
# |
# -----------------------------------------------------------------------------------------------

# animals = ["cat", "dog" , "dog", "bird", "elephent", "Jim", "dog" ]

# new lists
# dogs = []
# wild_animals = []

# for animal in animals:
#    if animal.lower() == "dog":
#         dogs.append(animal)
# if animal.lower() != ["dog ", "cat", "Jim"]:
#         wild_animals.append(animal)

# print(f"The number of {len(dogs)} dogs at our shelter are ")
# print(f"The number of {len(wild_animals)} wild animal at our shelter are ")

# -----------------------------------------------------------------------------------------------
# |                                 Activity 5 -  Going Shopping 
# |

# We are going shopping, and we need to check if what is on our list in at the supermarket.
# Create two lists, shopping_list and at_the_shops with the following elements:
# • shopping_list:cheese,beans,crisps,milk,apples
# • at_the_shops:pears,jam,cheese,apples,bread,tuna,crisps
# Use a nested for loop to check your list against the things at the shops.
# If something is at the shop, print “Yay, they’ve got it!”.
# If something is not at the shop, print “Oh no, they’ve not got it!”.
# 
# 
# -----------------------------------------------------------------------------------------------

# lists

# # Shopping list
# shopping_list = ["cheese", "beans", "crisps", "milk", "apples"]

# # Items available at the shop
# at_the_shops = ["pears", "jam", "cheese", "apples", "bread", "tuna", "crisps"]

# # Loop through each item on the shopping list
# for item in shopping_list:
#   # Found flag to track if the item is found
#   found = False
#   # Inner loop to check against items at the shop
#   for shop_item in at_the_shops:
  
#     if item == shop_item:
#       found = True
#       break  # Exit inner loop once found

 
#   if found:
#     print(f"Yay, they've got {item}!")
#   else:
#     print(f"Oh no, they've not got {item}!")

# -----------------------------------------------------------------------------------------------
# |                                 Activity 6 -  for vs while 
# |

#  Print the numbers from 1 to 10 in the console.
#  Do this twice; first with a for loop and then with a while loop.
#  Then answer the following questions:
# 
# • Which solution has the most lines of code? • Did either require variables; if so, why?
# • Which solution is more useful and why?
# 
# 
# -----------------------------------------------------------------------------------------------

# FOR loop
# ---------------
# for i in range (1,11):
#     print(i)
# --------------------
# While loop 
# ---------------------
# yes we do need to assign a variable

# i = 1
# while i <= 10:
#     print (i)
#     i += 1 

# In loops and other iterations, i += 1 is commonly 
# used to increment a counter variable, keeping track of the number of iterations or the current index.
    

# Ask a user to input any number of integers. They can enter as many numbers as they like. When they type "quit" the programme should end, 
# and the output should display a list of the numbers entered, the average of those numbers, and the sum total of the numbers.
# Given a list of numbers 3,45,23,32,67,87,56,43,1,86, find the maximum and output it to the terminal
# Given a list of numbers 12,45,23,75,3,22,11,66,78,43, find the number '3' and output "Found the number '3' on loop number <loop_num>"

# 
