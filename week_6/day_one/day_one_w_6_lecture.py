# music = "classical" #this is a truthy 
# new_music = "" #aa empty string is falsy that's how python has been designed
# print(music == "classical")
# print(new_music==True)
# the rieason why we want tyo to do that it makes more understandlbe our reading, and it more easy to evaluate 

# music = "classical"
# shopping_list = []
# num = 0
# name = ""
# my_name = "Dave"

# print(bool(music))
# print(bool(shopping_list))
# print(bool(num))
# print(bool(name))
# print(bool(my_name))

# print( "What is your name?")
# name = input(" > " )
# if name:
#     print(f"Hello {name}, how are you?")
# else:
#     print( "You did not give me your name!")

# list = ["carrot","yogurt","milk","apple"]    
# new_item =  input("Please add an item to the list: ").lower()

# if new_item not in list:
#     list.append(new_item)
#     print(list)
    
# else:
#     print("the item is already in the list")

# capital_cities = {
# "England": "London",
# "Northern Ireland": "Belfast",
# "Ireland": "Dublin",
# "Scotland": "Edinburgh",
# "Wales": "Cardiff",
# "england": "Liverpool"
# }
# print(capital_cities ["England" ])
# print(capital_cities ["England"]. lower ())

# animals = {
#     "Lion" : "Cub",
#     "Pigeon" : "Squab",
#     "Gecko" : "Hatchling",
#     "Hedgehog" : "Hoglet",

# print(animals.items())# items are the pair stored in the dictionary such as lion : cub
# # methods are 
# new_input= input("Insert a key to retrieve a value:").capitalize

# if new_input not in animals:
#     print("not a valid key")
    
# else:

# print(animals)

# more_cities = {
#     "Russia": "Moscow",
#     "Lithuania": "Vilneus"
# }
# print(capital_cities.update(more_cities))
# print(capital_cities)

# dinosaurs = [
# "Triceratops",
# "Velociraptor",
# "Anklyosaurus",
# "Archaeopteryx",
# "Tyrannosaurus Rex",
# "Stegosaurus",
# "Iguanodon"
# ]

# # saurus_dinosaurs = []

# # for dino in dinosaurs:
# #     if "saurus"in dino:
# #       saurus_dinosaurs.append(dino)
                
# # print(saurus_dinosaurs)

# # a list comprehention look in to it. 
# saurus_dinosaurs = [dino for dino if "saurus" in dinosaurs]:
# print(saurus_dinosaurs)



# if "saurus" in dino
# new_item = "saurus"
# new_list.append(dinosaurs)
# new_list.append(new_item)

# print(new_list)

# print("Type in two numbers to multiply them")
# while True:
#     try:
#         num1 = int(input(">>"))
#         num2 = int(input (">>"))
#         break 
#     except:
#         print("Please try again using numbers only!")
# print(num1*num2)

# num1 = int(input(">>"))
# num2 = int(input (">>"))

