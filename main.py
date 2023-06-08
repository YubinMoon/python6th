fruits = ["apple", "banana", "cherry", "orange"]
vegetables = ["carrot", "cucumber"]

grocery = fruits + vegetables
print(grocery)

numbers = [10, 5, 8, 1, 7]
numbers.sort()
print(numbers)

slice_numbers = numbers[1:4]
print(slice_numbers)

alias_numbers = numbers
print(alias_numbers)

numbers_copy = numbers.copy()
print(numbers_copy)

numbers_clone = numbers[:]
print(numbers_clone)

print(id(numbers))
print(id(alias_numbers))
print(id(numbers_copy))
print(id(numbers_clone))
print(alias_numbers is numbers)
print(numbers_copy is numbers)
print(numbers_clone is numbers)
