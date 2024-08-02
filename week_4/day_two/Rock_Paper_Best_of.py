import random 
from colorama import Fore, Style

print("----------------------------------------")
print("Welcome to Rock - Paper - Scissors game ASCII ART!" )

# creating variables with all possible gestures 
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

# dictionary of 
gestures = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

# I had to use AI to overcaome the problem of not disaplying the score and definining a function play_game() i was able to get that
def play_game():
    user_score = 0
    computer_score = 0

    # Get the total number of games to play
    while True:
        total_games = input("Enter the total number of games to play (best of 3, 5, or 7): ")
        if total_games in ["3", "5", "7"]:
            total_games = int(total_games)
            break
        else:
            print("Invalid choice. Please enter 3, 5, or 7.")

    # Calculate the number of wins needed to win the series
    wins_needed = (total_games // 2) + 1 #by using total_games //(floor division operator)

    # Loop until one player wins the series
    while user_score < wins_needed and computer_score < wins_needed:
        user_action = input("Enter a choice (rock, paper, scissors): ").lower()
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions) #random.choice is picking from possible actions list

        if user_action not in possible_actions:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        print(f"\nYou chose:\n{gestures[user_action]}")
        print(f"Computer chose:\n{gestures[computer_action]}")

        # Check for tie
        if user_action == computer_action:
            print(Fore.CYAN + f"Both players selected {user_action}. It's a tie!")
            print(Style.RESET_ALL)
        # Check for user's choice and computer's response
        elif user_action == "rock":
            if computer_action == "scissors":
                print(Fore.GREEN + "Rock smashes scissors! You win!")
                print(Style.RESET_ALL)
                user_score += 1
            else:
                print(Fore.RED + "Paper covers rock! You lose.")
                print(Style.RESET_ALL)
                computer_score += 1
        elif user_action == "paper":
            if computer_action == "rock":
                print(Fore.GREEN + "Paper covers rock! You win!")
                print(Style.RESET_ALL)
                user_score += 1
            else:
                print(Fore.RED + "Scissors cuts paper! You lose.")
                print(Style.RESET_ALL)
                computer_score += 1
        elif user_action == "scissors":
            if computer_action == "paper":
                print(Fore.GREEN + "Scissors cuts paper! You win!")
                print(Style.RESET_ALL)
                user_score += 1
            else:
                print(Fore.RED + "Rock smashes scissors! You lose.")
                print(Style.RESET_ALL)
                computer_score += 1

        print(f"\nScore: You {user_score} - Computer {computer_score}\n")

    # Declare the overall winner
    if user_score > computer_score:
        print(Fore.GREEN + "Congratulations! You won the series!")
    else:
        print(Fore.RED + "The computer won the series. Better luck next time!")
    print(Style.RESET_ALL)

# Main loop to play multiple series
while True:
    play_game()
    play_again = input("Do you want to play another series? (y/n): ").lower()
    if play_again != "y":
        print("Goodbye!")
        break
