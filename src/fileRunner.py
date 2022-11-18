# CODE RUNNER FOR THE CPU
# CURRENTLY SUPPORTS ONLY .fo

import os

print("")

PATH = "D:\\CPU\\"

BIN_PATH = "D:\\CPU\\usr_bin\\"
CODE_PATH = "D:\\CPU\\usr_scripts"

def getText(fileName):
    with open(fileName) as f:
        lines = f.readlines()
        return lines

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

def getContent(Name, Dir, Ext):
    if (checkForFile(name=Name, dir=Dir, extension=Ext)):
        return getText(Dir+Name)

def replaceNewLines(string):
    return string.replace("\n", " ")

# Main Event Loop

while True:
    
    command = loop()
    ARRcontent: str = None
    content: str = ""

    # Command Detector

    if command.startswith("/@"):
        file = command.split("@")[1]
        if file.endswith(".fo"):
            ARRcontent = getContent(file, "D:\\CPU\\Examples\\", ".fo")#BIN_PATH)
        elif file.endswith(".flo"):
            ARRcontent = getContent(file, BIN_PATH, ".fo")
        elif file.endswith(".fsm"):
            ARRcontent = getContent(file, CODE_PATH, ".fo")
        elif file.endswith(".fl"):
            ARRcontent = getContent(file, CODE_PATH, ".fo")
    else:
        print("Command not found.\n")
        continue
    
    if ARRcontent == None:
        print("Please input a valid file.")
        continue

    # Combine

    content = ARRcontent[0]

    for str in ARRcontent:
        if str[0] == str:
            continue;
        else:
            content = content + str

    for child in content:
        print(content)
        for char in child:
            print(content)
            replaceNewLines(child)

    #print(content)

# /@CompiledAssemblyExample.fo to run the file
    