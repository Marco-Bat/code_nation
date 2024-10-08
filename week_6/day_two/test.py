# fav_books = ["guerriero di pace", "the moon and sixpences", "the magician", "living dangerously"]
# wish_list = []

# while True:
#     user_fav = input("What's your favourite book? ").strip().lower()

#     if not user_fav:
#         print("Please add a book title.")
#         continue  # Prompt the user again
    
#     if user_fav.isdigit():
#         print("Please don't use numbers; type a book title.")
#         continue  # Prompt the user again
    
#     if user_fav in fav_books:
#         print(f"{user_fav} is one of my favorite books too.")
#         break  # Exit the loop since a valid book title was provided
    
#     else:
#         print("I have not read that book. I will add this to my wish list.") 
#         wish_list.append(user_fav)
#         print(f"Added to my wish list: {wish_list}")
#         break  # Optionally continue to prompt the user again instead of breaking the loop


# my_list = [1,2,3]
# my_list[1] = 99

# print (my_list)
# 11, 2, 31

# nums = [-1, 2, -3, 4, -5]
# positive_nums = [number for number in nums if number >= 0]
# print (positive_nums)

# score = 75
# if score < 50:
#         category = "Low"
# elif score <= 80:
#     category = "Medium"
# else:
#         category = "High"
# print(f"The score is {score} is categorized as {category}")

# count = 0
# while count < 3:
#     print("Hello, world!")
   
#     count+=1  # count = count +1

text_to_morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', 
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', 
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

user_text = input("Type a sentence or a word you'd like to translate: ").upper()

translated_text = ''

for char in user_text:
    if char in text_to_morse_code:
        translated_text += text_to_morse_code[char] + ' '
    elif char == ' ':
        translated_text += '  '  # To denote space between words

print(translated_text)