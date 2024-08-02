print("What is the capital of England?") 
# it was not a string 
answer= input("Type your answer here >> ")
# to return London or london I have use or  
if answer == "London" or answer == "london":
# print(f) gives back a more accurate answer
    print(f"Correct!The answer is {answer}") 
else:
    print(f"Incorrect, the answer is'London',not {answer}")