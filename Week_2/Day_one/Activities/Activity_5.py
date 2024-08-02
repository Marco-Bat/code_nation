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

