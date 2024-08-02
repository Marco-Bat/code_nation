# Create a dictionary of five favourite songs
# (the key is the artist).
# Using any method, add two new items to your dictionary.
# -----------------------------------------------------------------------------------------------
# |                                 Challenge 1
# -----------------------------------------------------------------------------------------------

# fav_song = {
#     "Queen" : "Bohemian Rapsody",
#     "Jeff Buclkey" :"Halleluja",
#     "Hans Zimmer" : " Time",
#     "Elvis" : "Devil in Desguise",
#     "Bon Iver" : "Perth"
# }
# print(fav_song)
# fav_song.setdefault("Micheal Jackson","Thriller")
# fav_song.setdefault("Fiffo","Zuzzo")

# print( fav_song)

# Research into printing your favourite song dictionary using a for loop.
# -----------------------------------------------------------------------------------------------
# |                                 Challenge 1: Stretch
# -----------------------------------------------------------------------------------------------

# fav_song = {
#     "Queen" : "Bohemian Rapsody",
#     "Jeff Buclkey" :"Halleluja",
#     "Hans Zimmer" : "Time",
#     "Elvis" : "Devil in Desguise",
#     "Bon Iver" : "Perth"
# }
# You can also use the .values() function to return values of a dictionary:
# for i in fav_song.values():
#     print(i)
# Print all values in the dictionary, one by one
# for x in fav_song:
#     print(fav_song[x])\

# Loop through both keys and values, by using the items() function:
# for x, y in fav_song.items():
#     print(x, y)

# Using the two lists, create a dictionary where country is the key, and language is the value.
# -----------------------------------------------------------------------------------------------
# |                                 Challenge 2
# -----------------------------------------------------------------------------------------------
# language = {
#     "England" : "English",
#     "Spain" : "Spanish",
#     "Ethiopia" : "Amharic",
#     "Iran" : "Farsi"
# }
# print(language ["Spain"])

# Using your dictionary of animals, create a program which allows a user to search for an animal to see the corresponding young name.
# If the animal does not exit in the dictionary, return a suitable message.

# -----------------------------------------------------------------------------------------------
# |                                 Challenge 3
# -----------------------------------------------------------------------------------------------

animals = {
    "Lion" : "Cub" ,
    "Pigeon" : "Squab",
    "Cat" : "Kitten",
    "Balena" : "Balenottera"

} 

print(animals["Balena"])
for k, v, in animals.items():
    print(k,v)
print(animals.get("Zebra"))



# Using your dictionary of animals, create a program which allows a user 
# to submit an animal name and baby name.
# If the animal already exists, return the existing baby name.
# If the animal does not exist, add it to the dictionary.
# -----------------------------------------------------------------------------------------------
# |                                 Challenge 4
# -----------------------------------------------------------------------------------------------

animals = {
    "Lion" : "Cub" ,
    "Pigeon" : "Squab",
    "Cat" : "Kitten",
    "Balena" : "Balenottera"

} 

animals.setdefault("Dinosauro", "Dinos")



for k, v, in animals.items():
    print(k,v)
print(animals.get("Zebra"))