# Create a variable called num.
# If num is divisible by 3 print “fizz”, 
# if it’s divisible by 7 print “buzz”, if it’s divisible by both 3 and 7 print “fizzbuzz”.
# Otherwise print num.

# num = 217

# if num % 3 == 0:
#     print("fizz")
# elif num % 7 ==0:
#     print("buzz")
# elif num % 3 == 0 and num % 7 == 0:
#     print("fizzbuzz")
# else:
#     print(num)

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