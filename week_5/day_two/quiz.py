import random
from colorama import Fore, Style

def get_username():
    return input("Please enter your user name here: ")

def initialize_high_scores(filename):
    try:
        with open(filename, 'x') as f:
            f.write('Username: , Score: 0\n')
    except FileExistsError:
        pass

def ask_question(question, choices):
    print(f"{question}")
    for choice in choices:
        print(choice)

    while True:
        my_input = input("Please enter your answer (1, 2, 3, 4): ")
        if my_input not in ["1", "2", "3", "4"]:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 4.")
            print(Style.RESET_ALL)
        else:
            return int(my_input)

def update_score(answer, correct_answer):
    if answer == correct_answer:
        print(f"{Fore.GREEN} Correct answer: {correct_answer}\n")
        print(Style.RESET_ALL)
        return 5
    else:
        print(f"{Fore.RED}Incorrect. The correct answer is: {correct_answer}\n")
        print(Style.RESET_ALL)
        return -2

def save_score(filename, username, score):
    with open(filename, 'a') as f:
        f.write('Username: {0}, Score: {1}\n'.format(username, score))

def display_high_scores(filename):
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(', ')
            username = parts[0].split(': ')[1]
            score = int(parts[1].split(': ')[1])
            print(f"{Fore.GREEN}{username} {Fore.YELLOW}{score}")

def quiz_game():
    user_score = 0
    quiz_questions = {
        "Question_1": {
            "Question_Type": "Who scored the most goals in a World Cup?",
            "Choice": ["1.Miroslav Klose", "2.Cristiano Ronaldo", "3.Leo Messi", "4.Eric Cantona"],
            "Answer": 1
        },
        "Question_2": {
            "Question_Type": "What's the hottest place in the world?",
            "Choice": ["Sitka, ALASKA,", "Palermo, ITALY", "Death Valley, USA", "Brighton, UK"],
            "Answer": 3
        },
        "Question_3": {
            "Question_Type": "Who is the fastest man in the world?",
            "Choice": ["Tyson GAY,", "Usain St. Leo Bolt OJ", "Asafa POWELL, USA", "Trayvon BROMELL"],
            "Answer": 2
        },
        "Question_4": {
            "Question_Type": "What is the 3rd highest mountain in the world?",
            "Choice": ["Everest,", "K2", "Fujiama", "Kangchenjunga"],
            "Answer": 4
        },
        "Question_5": {
            "Question_Type": "What is the fastest airplane in the world?",
            "Choice": ["Lockheed SR-71 Blackbird", "NASA X-43A", "Lockheed YF-12", "Mikoyan-Gurevich MiG-25 Foxbat"],
            "Answer": 2
        }
    }

    question_keys = list(quiz_questions.keys())
    random.shuffle(question_keys)

    username = get_username()
    initialize_high_scores('high-scores.txt')

    for key in question_keys:
        value = quiz_questions[key]
        ask_question(value['Question_Type'], value['Choice'])
        answer = ask_question(value['Question_Type'], value['Choice'])
        user_score += update_score(answer, value['Answer'])

    save_score('high-scores.txt', username, user_score)
    print(f"User score is {user_score}")
    display_high_scores('high-scores.txt')

if __name__ == "__main__":
    quiz_game()


