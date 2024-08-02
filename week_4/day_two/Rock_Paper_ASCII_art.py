import random 
from colorama import Fore, Style

print("----------------------------------------")
print("Welcome to Rock - Paper - Scissors game ASCII ART!" )

# creating viarables for each gestures 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ROCK
'''

paper = '''
    ________
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    PAPER
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    SCISSORS
'''

gestures = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

# while infinite loop to keep playing until user quits
while True:
    user_action = input("Enter a choice (rock, paper, scissors): ").lower()
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions) #random.choice is picking from possible actions list

    if user_action not in possible_actions:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    print(f"You chose:\n{gestures[user_action]}") #this is printing user action from gestures to pick the ASCII gesture 
    print(f"Computer chose:\n{gestures[computer_action]}") # this is printing computer action from gestures to pick the ASCII gesture 

    # Check for tie
    if user_action == computer_action:
        print(Fore.CYAN + f"Both players selected {user_action}. It's a tie!")
        print(Style.RESET_ALL)
    # Check for user's choice and computer's response
    elif user_action == "rock":
        if computer_action == "scissors":
            print(Fore.GREEN + "Rock smashes scissors! You win!")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + "Paper covers rock! You lose.")
            print(Style.RESET_ALL)
    elif user_action == "paper":
        if computer_action == "rock":
            print(Fore.GREEN + "Paper covers rock! You win!")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + "Scissors cuts paper! You lose.")
            print(Style.RESET_ALL)
    elif user_action == "scissors":
        if computer_action == "paper":
            print(Fore.GREEN + "Scissors cuts paper! You win!")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + "Rock smashes scissors! You lose.")
            print(Style.RESET_ALL)

    # Ask user to play again
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("Goodbye!")
        break
