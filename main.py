import os

current_directory = os.getcwd()
print(current_directory)

os.mkdir("example")  # 단일 폴더
os.makedirs("parent_dir/child_dir")  # 여러 폴더

# os.chdir("venv")
# current_directory2 = os.getcwd()
# print(current_directory2)

os.rename("example", "new_example")

os.rmdir("new_example")
os.removedirs("parent_dir/child_dir")  # 여러 폴더

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Current Path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)
    print()
