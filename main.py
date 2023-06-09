with open("example.txt", "w") as file_object:
    content = """this is a test file
this is a test file
this is a test file
this is a test file
"""
    print(content)
    file_object.write(content)
