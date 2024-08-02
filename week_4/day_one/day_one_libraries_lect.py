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

# import random

# # print(random.uniform(1,10))
# #generate a random float number betewwn the range sepcified in the unifom method

# print(random.randint(1,10))
# # generates a random int between the range specified in the randint method

# import random

# my_num = 13
# ran_num = random.randint(1,50)

# while my_num != ran_num:
#     print(f"The number {ran_num} doesn't match my number {my_num}")
#     ran_num = random.randint (1,50)

# print(f"The number {ran_num} matches my number {my_num}")

# from random import random, uniform, randint
# print(random())
# print(uniform(1,10))
# print(randint(1.10))


# from colorama import Back, Fore, Style

# print(Fore.RED + "Some red text")
# print(Back.GREEN + "Some text with a green background" )
# print(Style.BRIGHT + "and in bright text")
# print(Style. RESET_ALL)
# print("back to normal now")



# from datetime import datetime

# now = datetime.now()
# print(now)

# # variables
# birth_month =10
# birth_day = 22
# birth_year=1983

# # this is calcultaing the difference between now and my birthdate
# actual = datetime.now() - datetime(year=birth_year, month=birth_month, day=birth_day)
# total_seconds = actual.total_seconds()

# # get the total number of days
# total_days= actual.days

# # // floor division always rounds down to the nearest whole number
# age_in_years=total_days // 365

# total_seconds = actual.total_seconds()
# print(f"your age in seconds: {int(total_seconds)}")
# total_minutes = total_seconds / 60

# # print(f"Total time difference: {actual}")
   
# print(f"You have been alive for {actual}" )
# print(f"Your age in years is: {age_in_years}")
# print(f"Your approximate age in minutes is: {int(total_minutes)}")

import random

mylist = ["apple", "banana", "cherry"]

print(random.choice(mylist))



