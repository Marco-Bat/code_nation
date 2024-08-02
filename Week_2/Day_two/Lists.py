#---------------------------------------
#           activity 1 
# --------------------------------------

#  Create a list of your three favourite websites and then add another two using a method.
# Then, remove the last website using a method.

fav_web = [
    "www.imdb.com",
    "www.apple.co.uk",
    "www.tuttonapoli.com"
]
# .extend()
add_web = ["www.instagram.com", "www.asos.com"]
fav_web.extend(add_web)
# or 
# fav_web.extend([instagram, udemy])
# fav_web.append("www.instagram.com")
# fav_web.append("www.asos.com")
print(fav_web)

fav_web.pop(-1)

print(fav_web)

#---------------------------------------
#           activity 2 
# --------------------------------------

# Copy the list.
# Use a method to display the number of the following items:


shopping_list = [
    "apple",
    "carrot",
    "pizza",
    "carrot",
    "dog food", 
    "orange juice",
    "egg",
    "kale",
    "carrot",
    "kale",
    "orange juice",
    "kale",
    "toilet roll",
    "stamps",
    "noodles",
    "pasta sauce",
    "egg",
    "pasta sauce"
]

count_egg = shopping_list.count("egg")
count_kale = shopping_list.count("kale")
count_stamps = shopping_list.count("stamps")
count_carrot = shopping_list.count("carrot")
count_orange = shopping_list.count("orange juice")

print(f"egg:{count_egg}")
print(f"kale: {count_kale}")
print(f"stamps {count_stamps}")
print(f"carrot {count_carrot}")
print(f"orange juice:{count_orange}")


#---------------------------------------
#           activity 3 
# --------------------------------------

# .remove method program

# desk_items = [
#     "speakers",
#     "Iphone",
#     "mixer",
#     "toilet roll",
#     "stamps",
#     "noodles" 
# ]

# desk_items.remove("toilet roll")
# print(desk_items)

# .reverse() method

# backpack = [
#     "laptop",
#     "headphones",
#     "charger",
#     "snack"
# ]

# backpack.reverse()
# print(backpack)

# .sort()

# players = [
#     "Kvicha",
#     "Simeone",
#     "Buongiorno",
#     "Marin",
#     "Chiesa"
# ]

# players.sort()
# print(players)

# count()
# players = [
#     "Kvicha",
#     "Simeone",
#     "Buongiorno",
#     "Marin",
#     "Chiesa",
#     "Chiesa",
#     "Marin"
# ]
# count_kvicha = players.count("Kvicha")
# count_marin = players.count("Marin")
# count_chiesa = players.count("Chiesa")

# print(f"Kvicha:{count_kvicha}")
# print(f"Marin:{count_marin}")
# print(f"Chiesa:{count_chiesa}")

# players.remove("Chiesa")
# players.remove("Marin")
# print(players)

# .extend()

backpack = [
    "laptop",
    "mouse",
    "keybord",
    "charger"
]

small_bag = ["charger", "headphones"]
backpack.extend(small_bag)
backpack.remove("charger")
backpack.sort()
print(backpack)