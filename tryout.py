import os

output = os.listdir(".")
print("os.listdir():",output)

for path in output:
    if os.path.isdir(path):
        print("folder:", path)
    else:
        print("File:", path)

def read_folder(path):
    output = os.listdir(".")
    for item in output:
        if os.path.isdir(path):
            read_folder(path+"/"+item)
        else:
            print("file:", item) 

read_folder(".")
