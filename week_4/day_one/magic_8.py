import random
from colorama import Fore, Style # fore defines text colour and style could reset colour once we have the answer


# I have created 2 answer lists, good and bad
 
good_fortunes = ["It is certain.",
    "Yes.",
    "The outlook is good.",
    "Most likely.",
    "Count on it.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Concentrate and ask again.",
    "My sources are unclear.",
    "Outlook good."]

bad_fortunes = ["You may rely on it.",
    "Without a doubt.",
    "Yes definitely.",
    "You betcha!",
    "Forget about it.",
    "There is no chance.",
    "Don't bank on it.",
    "Looks bleak.",
    "Very doubtful." ]

#main cilcle loop (infite loop until the exit condition has met)
while True:
    question = input("Ask the Magic 8 Ball a question (type 'quit' to exit): ")

    if question.lower() == 'quit': #.lower formats user answer and will quit the program
        print("Exiting the Magic 8 Ball program.")
        break

    random_number = random.randint(1, 100) #generates a radnom number between 1 and 100

    if random_number % 2 == 0: # checks if a number has a reminder 0
        fortune = random.choice(good_fortunes)  #random choice is selcting randomly from a good_fortunes list 
        print(Fore.GREEN + fortune + Style.RESET_ALL) #I had to use Style reset all to get back to the normal text 
    else:
        fortune = random.choice(bad_fortunes) #random choice is selcting randomly from a bad fortunes list 
        print(Fore.RED + fortune + Style.RESET_ALL) #I had to use Style reset all to get back to the normal tex