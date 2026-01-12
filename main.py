from dataManager import decrypt
import beautify
import displayOptions


def main():
    #importing the data from the listStack.json before starting the program
    listStack = decrypt()
    #looping until the user doesn't want to exit the program
    while True:
        listStack = decrypt() #this line could be removed but I want to be safe for any future changes so I'm keeping it here

        choice = displayOptions.mainMenu(listStack)
        if choice == -1:
            break
    
    beautify.clear_screen() #clearing the screen before program ends


main()