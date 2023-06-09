class Mobile:
    fp = "yes"


realme = Mobile()
redme = Mobile()
geek = Mobile()

print(Mobile.fp)
print(realme.fp)
print(redme.fp)
print(geek.fp)

Mobile.fp = "no"
print(Mobile.fp)
print(realme.fp)
print(redme.fp)
print(geek.fp)
print("-------------")
realme.fp = "Not Working"
print(Mobile.fp)
print(realme.fp)
print(redme.fp)
print(geek.fp)
