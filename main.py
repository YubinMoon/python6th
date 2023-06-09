with open("example.txt", "r") as file_object:
    lines = file_object.readlines()
    print(lines)
    for line in lines:
        print(line.strip())
