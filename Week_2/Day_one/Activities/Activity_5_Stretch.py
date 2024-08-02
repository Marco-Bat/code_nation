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