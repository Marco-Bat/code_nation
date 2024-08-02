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
