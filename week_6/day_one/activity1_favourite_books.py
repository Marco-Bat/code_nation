# Write a list of your favourite books.
# Create a program which allows a user to type in their favourite book.
# If their favourite book matches one of your favourite books print
# “<bookname> is one of my favourite books too.” Else, print “I haven’t read that book.”
# Ensure the user gives you information - a blank string should not be accepted!

fav_books = ["guerriero di pace", "the moon and sixpences", "the magician", "living dangerously"]
wish_list = []

while True:
    user_fav = input("What's your favourite book? ").strip().lower()

    if not user_fav:
        print("Please add a book title.")
        continue  # Prompt the user again
    
    if user_fav.isdigit():
        print("Please don't use numbers; type a book title.")
        continue  # Prompt the user again
    
    if user_fav in fav_books:
        print(f"{user_fav} is one of my favorite books too.")
        break  # Exit the loop since a valid book title was provided
    
    else:
        print("I have not read that book; I will add this to my wish list.") 
        wish_list.append(user_fav)
        print(f"Added to my wish list:{wish_list}")
         

# while True:
#     if user_fav in fav_books:
#         print(f"{user_fav} is my favouite books too.")
#     else:
#         print("i have not read that book")
#         break
# # saurus_dinosaurs = []

