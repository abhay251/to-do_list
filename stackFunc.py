from listTemplate import listTemplate as template 
from dataManager import encrypt
from dataManager import getValidInt
import beautify

#function to create a new object of listTemplate class and append it to the listStack and then encrypt it to the listStack.json file and return the new listStack
def createList(listStack):
    beautify.clear_screen()
    beautify.printBorder(beautify.findColumn(0.5))
    print("Creating a new list")
    beautify.printBorder(beautify.findColumn(0.5))
    name = input("Enter the name of the new to-do list\n")
    newList = template(name)
    listStack.append(newList)
    encrypt(listStack)
    beautify.printBorder(beautify.findColumn(0.5))
    print(f"List {name} created")
    return listStack

#function to delete an object of the listTemplate class from the listStack and encrypt it and return the new listStack
def deleteList(listStack):
    beautify.clear_screen()
    beautify.printBorder(beautify.findColumn(0.5))
    print("Deleting a list")
    beautify.printBorder(beautify.findColumn(0.5))

    if len(listStack) == 0:
        print("There is no list to be deleted, create a new list first.")
        return listStack

    showListStack(listStack)
    beautify.printBorder(beautify.findColumn(0.5))
    choice = getValidInt(inpPrompt="Enter the index of list you want to delete or enter 0 to cancel")
    if choice == 0:
        return listStack
    else:
        removedList = listStack.pop(choice-1)
        encrypt(listStack)
        print(f"Deleted {removedList.nameOfList}")
        return listStack

#function to iterate and show the lists present inside the list stack
def showListStack(listStack):
    for index,item in enumerate(listStack, start=1):
        print(f"{index}. {item.nameOfList} ({len(item.mainTasks)} pending)")