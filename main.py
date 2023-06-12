try:
    number = int("Not a number")
    number = 5 + "abc"
except ValueError:
    print("Error: Invalid value.")
except TypeError:
    print("Error: Invalid type.")
