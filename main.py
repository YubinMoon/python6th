fruits = ["apple", "banana", "cherry", "orange"]
print(fruits)

fruits.append("grape")
print(fruits)

fruits.insert(2, "kiwi")
print(fruits)

print(fruits.pop())
print(fruits)

print(fruits.pop(1))
print(fruits)

fruits.append("cherry")
print(fruits)
fruits.remove("cherry")
print(fruits)

print(fruits.index("cherry"))
print(fruits.remove("cherry"))
print(fruits)

# fruits.remove("cherry") # Error

print(fruits)
fruits.reverse()
print(fruits)
