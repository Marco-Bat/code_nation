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