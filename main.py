filename = "example.txt"

print("파일이 존재하는지 확인하기")

import os

if os.path.isfile(filename):
    print(f"{filename}이 존재합니다.")
else:
    print(f"{filename}이 존재하지 않습니다.")

file_object = open("list_example.txt", "w")

content_list = ["Python", "Java", "C++", "Javascript"]

for item in content_list:
    file_object.write(item + "\n")

file_object.close()
