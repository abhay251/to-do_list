import os
import shutil

#clear screen function
def clear_screen():
    # Check if the operating system is Windows ('nt')
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux (posix)
    else:
        os.system('clear')

#funtion to print ---- till the window's width
def printBorder(column):
    print("-"*column)

#function to find the width of the window
def findColumn(length=1):
    size  = shutil.get_terminal_size()
    column =  size.columns
    return int(column*length)

#function to print the given text as heading using the above two functions
def printHeading(text):
    width = findColumn()
    padding = int((width-len(text))/2)
    printBorder(width)
    print(" "*padding+text)
    printBorder(width)
