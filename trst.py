# name = input("What's your name? ")
# print ("Hello " + name)

# birth_year = int(input("Enter your birth year: "))
# age = 2024 - birth_year
# print(age)

# sum
# first = float(input("Please enter a number: "))
# second = float(input("Please enter an other number: "))
# print(f"the sum is {first + second}")

# Stings and methods 
# course = "Python for beginners"

# print(course.upper())
# print(course.find("y"))
# print(course.find("Python"))
# print(course.replace("for", "4"))

# print("Python" in course)

# x=10
# x +=3 #augumented assigned operator
# print(x)

# x = (10 + 3) * 2
# print(x) 

# x = 3>2
# print(x)

# price = 5
# print (not price > 10)

# temp = 70

# if temp > 30:
#     print("it's a hot day! ")
#     print("Drink plenty of water ")
# elif temp > 20: # if this condition is true we are going to se the message in print
#     print("It's a nice day")
# elif temp > 10:
#     print("it's chill!")
# else: #this will be print if any of the above condition is true!
#     print("It's cold")


# weight exercise
# weight = float(input("Enter your weight: "))

# unit = input("(K)g or (L)bs: ")

# if unit.upper == "K":
#     converted = weight / 0.45
#     print(f"Weight in Lbs: {converted} ")
    
# else:
#     converted = weight * 0.45
#     print(f"Weight in Lbs: {converted} ")

# i = 1

# while i <= 20:
#     print(i * "/")
#     print(i * "*")
#     i += 1
    
# names = ["John", "Bob", "Mosh", "Sam", "Mary"]

# names[0] = "Jon"
# print(names[0:3]) #the end index is exlcuded 

# numbers = [1,2,3,4,5,]
# print(len(numbers))

# numbers = [1,2,3,4,5,]

# for item in numbers:#we can iterate all the itme in this list
#     print(item)

# # this while loop is doing the same but it's less intuitive
# i = 0 
# while i < len(numbers):
#     print(numbers[i])
#     i +=1

# the range function

# numbers = range(5)#the range function in this case will include number from 0 to 4, 5 is not included
# numbers = range(5,10) #  in this case the first value is the starting value 5 and the the 2nd value is 10 but 
# but actually it will print 9
# if we use (5,10, 2) 2 is the step is gonna jump by two 
# numbers = range(5,10,2)
# for num in numbers:
#     print(num)
    
# in reality we don't really need to store any numbers so we could use range in the for loop

# for num in range(5):
#     print(num)


# tuples

num = (1,2,3)
