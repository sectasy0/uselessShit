import subprocess

import psutil
import os

processName = "AutoHotkey.exe"
ahkPath = "C:\Program Files\AutoHotkey\AutoHotkey.exe"

filename = "test"
filesToRun = []
fileId = 0

def isRunning(process_name: str):
    return True if process_name in [process.name() for process in psutil.process_iter()] else False
 
for file in os.listdir():
    if file.endswith("ahk", 3):
        if file[len(file)-5].isdigit():
            fileId += 1

        filesToRun.append(file)

if isRunning(processName):
    output = []
    with open(f"{filename}.ahk", "r") as file:
        for line in file.readlines():
            line = line.replace("\n", "").split()
            
            if line[0] == "Global":
                tokenId = line[1][len(line[1])-1]
                line[1] = line[1][:-1] + str(int(fileId) + 1)
                filename = filename + str(int(fileId) + 1) 

            output.append(line)

    with open(f"{filename}.ahk", 'w') as file:
        for line in output:
            file.write(f"{' '.join(line)} \n")

    for file in filesToRun:
        subprocess.call([ahkPath, f"{file}"])
else: subprocess.call([ahkPath, f"{filename}.ahk"])