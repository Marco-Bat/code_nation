import random
from colorama import Fore, Style

# i had to rely on Ai to understands class, in order to utilise this again and again
class RPSLSGame:
    def __init__(self):
        self.gestures = {
            1: "rock",
            2: "paper",
            3: "scissors",
            4: "lizard",
            5: "spock"
        }
        self.gestures_art = {
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
            ''',
            "lizard": '''
                _______
            ---'   ____)____
                      ______)
                   __________)
                LIZARD
            ''',
            "spock": '''
               ⌠⌒|
             ⌠⌒⌉| |   ◜﹆◜﹆
            | ||⩧|  / // /
            |_|| | /-//=/
            | || |/ // /
            ( || | // /
            |         .______
            |         __⫫____)
            |       |
              SPOCK

            '''
        }
        
        self.rules = {
            "rock": ["scissors", "lizard"],
            "paper": ["rock", "spock"],
            "scissors": ["paper", "lizard"],
            "lizard": ["spock", "paper"],
            "spock": ["scissors", "rock"]
        }

    def play_game(self):
        user_score = 0
        computer_score = 0

        total_games = self.get_total_games()
        wins_needed = (total_games // 2) + 1

        while user_score < wins_needed and computer_score < wins_needed:
            user_action = self.get_user_action()
            computer_action = self.get_computer_action()

            print(f"\nYou chose:\n{self.gestures_art[user_action]}")
            print(f"Computer chose:\n{self.gestures_art[computer_action]}")

            if user_action == computer_action:
                print(Fore.CYAN + f"Both players selected {user_action}. It's a tie!")
                print(Style.RESET_ALL)
            elif computer_action in self.rules[user_action]:
                print(Fore.GREEN + f"{user_action.capitalize()} beats {computer_action}! You win!")
                print(Style.RESET_ALL)
                user_score += 1
            else:
                print(Fore.RED + f"{computer_action.capitalize()} beats {user_action}! You lose.")
                print(Style.RESET_ALL)
                computer_score += 1

            print(f"\nScore: You {user_score} - Computer {computer_score}\n")

        if user_score > computer_score:
            print(Fore.GREEN + "Congratulations! You won the series!")
        else:
            print(Fore.RED + "The computer won the series. Better luck next time!")
        print(Style.RESET_ALL)

    def get_total_games(self):
        while True:
            total_games = input("Enter the total number of games to play (best of 3, 5, or 7): ")
            if total_games in ["3", "5", "7"]:
                return int(total_games)
            else:
                print("Invalid choice. Please enter 3, 5, or 7.")

    def get_user_action(self):
        while True:
            print("\nChoose your gesture:")
            print("1: Rock")
            print("2: Paper")
            print("3: Scissors")
            print("4: Lizard")
            print("5: Spock")

            try:
                user_choice = int(input("Enter the number corresponding to your choice: "))
                if user_choice in self.gestures:
                    return self.gestures[user_choice]
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid choice. Please enter a number.")

    def get_computer_action(self):
        return self.gestures[random.randint(1, 5)]

    def start(self):
        while True:
            self.play_game()
            play_again = input("Do you want to play another series? (y/n): ").lower()
            if play_again != "y":
                print("Goodbye!")
                break

if __name__ == "__main__":
    game = RPSLSGame()
    game.start()
