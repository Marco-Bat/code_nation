# def swap_head_tail(lst):
#     # Determine the middle index
#     n = len(lst)
#     middle_index = n // 2
    
#     # Slice the list into head, middle, and tail
#     if n % 2 == 0:
#         head = lst[:middle_index]
#         tail = lst[middle_index:]
#         middle = []  # No middle element if the list length is even
#     else:
#         head = lst[:middle_index]
#         middle = [lst[middle_index]]
#         tail = lst[middle_index + 1:]
    
#     # Create the new list by swapping the head and tail
#     new_list = tail + middle + head
    
#     return new_list

# # Example usage
# lst = [1, 2, 3, 4, 5, 6]
# result = swap_head_tail(lst)
# print(result)  # Output: [4, 5, 6, 1, 2, 3]

# lst = [1, 2, 3, 4, 5]
# result = swap_head_tail(lst)
# print(result)  # Output: [4, 5, 1, 2, 3]


# dice

# import random

# def play_game():
#     score = 0
#     while True:
#         input("Press Enter to roll the dice...")
#         roll = random.randint(1, 6)
#         print(f"You rolled a {roll}!")
        
#         if roll == 1:
#             print("You rolled a 1! You lose your score.")
#             score = 0
#             break
#         else:
#             score += roll
#             print(f"Your current score is {score}.")
#             print("You win!")

# # Start the game
# play_game()


# extended dice game

# import random

# def play_game():
#     score = 0
#     winning_score = 20
#     while True:
#         input("Press Enter to roll the dice...")
#         roll = random.randint(1, 6)
#         print(f"You rolled a {roll}!")
        
#         if roll == 1:
#             print("You rolled a 1! You lose your score.")
#             score = 0
#             break
#         else:
#             score += roll
#             print(f"Your current score is {score}.")
            
#             if score >= winning_score:
#                 print("Congratulations! You've reached the winning score of 20!")
#                 break

# # Start the game
# play_game()


# refactoring my code

import random
from colorama import Fore, Style

def display_welcome_message():
    print("----------------------------------------")
    print("Welcome to Rock-Paper-Scissors game ASCII ART!")

# ASCII art for gestures
GESTURES = {
    "rock": '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
        ROCK
    ''',
    "paper": '''
        ________
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
        PAPER
    ''',
    "scissors": '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        SCISSORS
    '''
}

POSSIBLE_ACTIONS = ["rock", "paper", "scissors"]

def get_total_games():
    while True:
        total_games = input("Enter the total number of games to play (best of 3, 5, or 7): ")
        if total_games in ["3", "5", "7"]:
            return int(total_games)
        else:
            print("Invalid choice. Please enter 3, 5, or 7.")

def get_user_action():
    while True:
        user_action = input("Enter a choice (rock, paper, scissors): ").lower()
        if user_action in POSSIBLE_ACTIONS:
            return user_action
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def display_choices(user_action, computer_action):
    print(f"\nYou chose:\n{GESTURES[user_action]}")
    print(f"Computer chose:\n{GESTURES[computer_action]}")

def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(Fore.CYAN + f"Both players selected {user_action}. It's a tie!")
        print(Style.RESET_ALL)
        return None
    elif (user_action == "rock" and computer_action == "scissors") or \
         (user_action == "paper" and computer_action == "rock") or \
         (user_action == "scissors" and computer_action == "paper"):
        print(Fore.GREEN + f"{user_action.capitalize()} beats {computer_action}! You win!")
        print(Style.RESET_ALL)
        return "user"
    else:
        print(Fore.RED + f"{computer_action.capitalize()} beats {user_action}! You lose.")
        print(Style.RESET_ALL)
        return "computer"

def play_round(user_score, computer_score, wins_needed):
    user_action = get_user_action()
    computer_action = random.choice(POSSIBLE_ACTIONS)
    display_choices(user_action, computer_action)

    winner = determine_winner(user_action, computer_action)
    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1

    print(f"\nScore: You {user_score} - Computer {computer_score}\n")

    return user_score, computer_score

def play_game():
    user_score = 0
    computer_score = 0
    total_games = get_total_games()
    wins_needed = (total_games // 2) + 1

    while user_score < wins_needed and computer_score < wins_needed:
        user_score, computer_score = play_round(user_score, computer_score, wins_needed)

    if user_score > computer_score:
        print(Fore.GREEN + "Congratulations! You won the series!")
    else:
        print(Fore.RED + "The computer won the series. Better luck next time!")
    print(Style.RESET_ALL)

def main():
    display_welcome_message()
    while True:
        play_game()
        play_again = input("Do you want to play another series? (y/n): ").lower()
        if play_again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
