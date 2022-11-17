import os

print("")

PATH = "D:\\CPU\\"

def loop():
    
    print(PATH+" ~ ")
    content = input("$ ")
    print("")
    return content

def checkForFile(name, dir, extension):
    files = os.listdir(dir)

    for file in files:
        if (file == name) and (file.endswith(extension)):
            return True

    return False

def runFileASMBIN(name):

    files = os.listdir(PATH)

    for file in files:
        if file.endswith(".fo"):
            return True

    if name in files 
