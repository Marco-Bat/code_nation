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



