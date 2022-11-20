# CODE RUNNER FOR THE CPU
# CURRENTLY SUPPORTS ONLY .fo

import os

print("")

PATH = "D:\\CPU\\"

BIN_PATH = "D:\\CPU\\usr_bin\\"
CODE_PATH = "D:\\CPU\\usr_scripts"

MEMORY = "D:\\CPU\\Memory\\RAM.mem"
RAG = "D:\\CPU\\Memory\\RAG.mem"
RBG = "D:\\CPU\\Memory\\RBG.mem"
RCG = "D:\\CPU\\Memory\\RCG.mem"
RDG = "D:\\CPU\\Memory\\RDG.mem"
REG = "D:\\CPU\\Memory\\REG.mem"
RFG = "D:\\CPU\\Memory\\RFG.mem"
RGG = "D:\\CPU\\Memory\\RGG.mem"
RHG = "D:\\CPU\\Memory\\RHG.mem"

def getText(fileName: str):
    with open(fileName) as f:
        lines = f.readlines()
        return lines


def loop():

    print(PATH + " ~ ")

    cmd = input("$ ")

    print("")

    return cmd


def checkForFile(name: str, directory: str, extension: str):
    files = os.listdir(directory)

    for File in files:
        if (File == name) and (File.endswith(extension)):
            return True

    return False


def getContent(Name: str, Dir: str, Ext: str):
    if checkForFile(name=Name, directory=Dir, extension=Ext):
        return getText(Dir + Name)


def replaceNewLines(inpt: str):
    return inpt.replace("\n", " ")


with open(MEMORY, "w") as file:
    file.write("Hello, world!")
# Main Event Loop

while True:

    Tcommand = loop()
    ARRcontent: str or None = None
    content: str = ""

    # Command Detector

    # Run

    if Tcommand.startswith("os -r"):
        file = Tcommand.split("-r ")[1]
        if file.endswith(".fo"):
            print(Tcommand)
            print(file)
            ARRcontent = getContent(file, "D:\\CPU\\Examples\\", ".fo")  # BIN_PATH)
            print(ARRcontent)
        elif file.endswith(".flo"):
            ARRcontent = getContent(file, BIN_PATH, ".flo")

    # Compile

    elif Tcommand.startswith("os -c"):
        file = Tcommand.split("-c")[1]

        if file.endswith(".fsm"):
            ARRcontent = getContent(file, CODE_PATH, ".fsm")
        elif file.endswith(".fl"):
            ARRcontent = getContent(file, CODE_PATH, ".fl")
    # Help menu

    elif Tcommand.startswith("os -h"):
        print(
            """
            OS Commands help
            
                os -h: Brings up this menu
                os -r: Runs selected file
                os -c: Compiles selected file 
        
            """
              )
    else:
        print("Command not found.\n")
        continue

    if ARRcontent is None:
        print("Please input a valid file.")
        continue

    # Combine
    content = ARRcontent[0]

    for string in ARRcontent:
        content = content + string

    del ARRcontent
    del Tcommand

    commands = None
    continuousContent = None

    for cmds in content:
        continuousContent = continuousContent + content.replace('\n', ' ')

    print(continuousContent)

# os -r CompiledAssemblyExample.fo to run the file
