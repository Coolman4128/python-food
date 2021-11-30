import subprocess
import os
import socketworks

def runTerminal(command):
    output = subprocess.check_output(command, shell=True)
    return output

def checkCommand(command):
    match command[0]:
        case rTerm:
            output =  runTerminal(command[1])
            return output



