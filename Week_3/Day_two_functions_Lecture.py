# str = "hello"

# print(len(str))

# def add_nums(a,b):
#     pass

# def say_hello(greeting):
#     print(greeting)

# say_hello("Goodbye!")

# def fullname(name, surname):
   
#     print(f"Welcome, {name} {surname}!")

# fullname("Marco", "Battimelli")

# def say_goobye():
#     print("Goobye")

# say_goobye()


# def say_something(something):
#     print(f"{something}")

# say_something("Hello there!")
# say_something("How are you?")
# say_something("Goodbye")

# def coffe_order(name,size,type,food):
#     print(f"{name} you have ordered {size} a {type} and a {food}, enjoy!")

# coffe_order("Marco","Small", "Flat White","Hazelnut Cake")
# coffe_order("Sara", "large"," none"," none")

# def withdrawal(amt , accnum):
#     print(f"withdrawing {amt} from account {accnum}" )

# withdrawal( 100, 556677)

#-----------------------------------------------------------------------------------------------
# |                                 Activity 1 -  MultiplyingNumbers 
# |
#-----------------------------------------------------------------------------------------------
# MultiplyingNumbers 
# Write a function called multiply_numbers(a, b) that takes two numbers 
# as input, multiplies them together, and prints the result.

# def mutliply_number(n1, n2):
#     print(f"the product of {n1} and {n2} is: {n1 * n2}")

# mutliply_number(5,5)

#-----------------------------------------------------------------------------------------------
# |                                 Activity 2 -  even or odd
# |
#-----------------------------------------------------------------------------------------------

# Checking Even or Odd
# Define a function named check_even_odd(num) 
# that takes a number as input and prints whether it's even or odd.

# def check_even_odd(num):
#       if num%2 == 0:
#         print(f"{num} is even.")
#       else:
#         print(f"{num} is odd")
# # check_even_odd(int
# check_even_odd(11)
# check_even_odd(10)

#-----------------------------------------------------------------------------------------------
# |                                 Activity 3 -  printing a list
# |
#-----------------------------------------------------------------------------------------------

# Create a function called print_list(my_list) that takes a 
# list as input and prints each element of the list on a separate line.

# def print_list(my_list):

#     for i in my_list:
#         print(i)

# backpack = ["Camera","Lenses","Batteries","Laptop"]     

# print_list(backpack)

#------------------------------------------------------------------------------------
# |                                 Activity 4 -  counting vowels
# |
#-------------------------------------------------------------------------------------

# print()
# print("Activity 4 - count vowels")
# print("-------------------------")

# vowels = "aeiouAEIOU" 

# def count_vowels(word):

#     count = 0

#     for char in word:
#         if char in vowels:
#             count +=1
#     print(f" There are {count} vowels in {word}")

# count_vowels(input("Check vowel count in "))   


# def add_up(n1,n2):
#     print(n1 + n2)
# add_up(56,88)


# integer_list = [1,2,3,4,5]
# def add_up_append(n1,n2):
#     integer_list.append(n1 + n2)
#     print(integer_list)
# add_up_append(4,7)

# def add_up(n1,n2):
#     return n1 + n2

# print(add_up(56,88))

# integer_list = [1,2,3,4,5]
# def add_up(n1,n2):
#     return n1 + n2
# integer_list.append(add_up(7,22))

# print(add_up)
# print(integer_list)

#      # Expected input: 
# order_pizza("cheese", "ham", "Medium")
 
# -> "Thanks for ordering a Medium cheese and ham pizza. Enjoy!"

# def order_pizza (size,topping1,topping2):
#      print(f"Thanks for odering a {size} pizza with {topping1} and {topping2}, enjoy!")

# order_pizza("medium","Cheese","Ham")


# A user enters their PIN number. If the PIN is valid they are then 
# prompted to enter the amount they would like. If the amount is less than their balance, 
# the cash is dispensed. If it is more than their balance they receive a message "Sorry, insufficient funds."
 
# The programme will likely have a number of functions:
 
# withdrawal() -> calls the main part of the programme to get the user's PIN
# check_balance() -> checks for sufficient funds in the account and dispense() is called.
# dispense() -> dispenses cash requested or a message to say "insufficient funds"

# Valid account numbers are "1234" and "5678". 
# Account 1234 has £1000 balance, 5678 has £500 balance.

# def pin():
    
#     pin=input("Enter your pin")
#     if pin (1234):
#         return pin
#     else:
#         print("invalid PIN, try again")
      
# pin()

# def check_balance(pin, account):
#     if pin in account:
#     balance =  



# Ipod 

# import time

# playlist = ["Last Night - Fuffo",
#             "Brian McKnight - One Last Cry",
#             "Ennio Morricone - C'era una volta in paradiso",
#             "Hanz Zimmer - Time",
#             "Queen - Don't Stop me know"
# ]

# def play(playlist):
#     for song in playlist:
#         print(f"Playing {song}")
#         time.sleep(2)

# play(playlist)


# print ("Activity 5 - Pizza order")


# def take_order(top1, top2, size=9):
#      if top2 == "": # If just one topping
#           print(f"Your Order: \n - {size} inch pizza with {top1}")
#      else: # If two toppings
#           print(f"Your Order:\n - {size} inch pizza with {top1} and {top2}")

# take_order ("cheese", "",) 
# take_order ("cheese","", 12) 
# take_order ("cheese", "ham",)
# take_order (9, "ham", 9)

# to do list in python
# todo_list = []

# def add_task(task):
#   todo_list.append(task)
#   print(f"Task '{task}' added to the list.")

# def view_tasks():
#   if not todo_list:
#     print("Your to-do list is empty.")
#   else:
#     print("To-Do List:")
#     for index, task in enumerate(todo_list):
#       print(f"{index+1}. {task}")

# def mark_as_complete(task_index):
#   if 0 <= task_index < len(todo_list):
#     completed_task = todo_list.pop(task_index)
#     print(f"Task '{completed_task}' marked as complete.")
#   else:
#     print("Invalid task index.")

# def delete_task(task_index):
#   if 0 <= task_index < len(todo_list):
#     deleted_task = todo_list.pop(task_index)
#     print(f"Task '{deleted_task}' deleted.")
#   else:
#     print("Invalid task index.")

# while True:
#   print("\nTo-Do List App")
#   print("1. Add task")
#   print("2. View tasks")
#   print("3. Mark task as complete")
#   print("4. Delete task")
#   print("5. Quit")

#   choice = input("Enter your choice: ")

#   if choice == '1':
#     task = input("Enter task: ")
#     add_task(task)
#   elif choice == '2':
#     view_tasks()
#   elif choice == '3':
#     task_index = int(input("Enter task index to mark as complete: ")) - 1
#     mark_as_complete(task_index)
#   elif choice == '4':
#     task_index = int(input("Enter task index to delete: ")) - 1
#     delete_task(task_index)
#   elif choice == '5':
#     break
#   else:
#     print("Invalid choice. Please try again.")



# count = 0 
# while count < 5:
#     print(count)
#     count += 1 



# print("Ready for launch!")

# import time
# count = 10
# while count > 0:
#      print(count)
#      count -=1
#      time.sleep(1) 
#      if count == 0: 
#           print("Blast Off!")


# import random

# Let's create a simple game where the computer generates a random number between 1 and 10, and the user has to guess it.

# num = random.randint(1,10)

# guess = 0

# while guess != num:
#     guess = int(input("Guess a number between 1 and 10: " ))
#     if guess < num:
#         print("too low!")
#     elif guess > num:
#         print("too high!")
# print("You guessed it!")





# def check_even_odd(num):
#      if num %2 == 0:
#         print(f"{num} is even.")
#      else:
#         print(f"{num} is odd")

# number = int(input("give me a number: "))        


# check_even_odd(number)


def check_even_odd(num):
  if num % 2 == 0:
    return "even"
  else:
    return "odd"

while True:
  user_input = input("Enter a number (or 'quit' to exit): ")
  if user_input.lower() == 'quit':
    break
  try:
    number = int(user_input)
    result = check_even_odd(number)
    print(f"{number} is {result}.")
  except ValueError:
    print("Invalid input. Please enter a number or 'quit'.")