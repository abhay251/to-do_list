from dataManager import encrypt
from dataManager import getValidInt

#function to input task and add it inside a particular list of the list stack and encrypt and return the list stack
def addTaskIntoList(listStack, listIndex):
    task = input("Enter the task\n")
    listStack[listIndex].addTask(task)
    encrypt(listStack) #saving the task to listStack.json file too
    print("Task added successfully")
    return listStack #returning the modified listStack back

#function to remove a task from a particular list of the listStack and encrypt the new listStack and return it
def removeTaskFromList(listStack, listIndex):
    #checking to run the delete function only if the number of tasks are 1 or more
    if len(listStack[listIndex].mainTasks)>0:
            listStack[listIndex].showTask()
            choice = getValidInt(inpPrompt="Enter the index of task you want to remove")
            while choice<=0 and choice>len(listStack[listIndex].mainTasks): #looping until we get an index value within the correct range
                choice = getValidInt("Enter the correct index.")
            listStack[listIndex].removeTask(choice-1)
            encrypt(listStack) #saving the task to listStack.json file too
            print("Task removed successfully!")
            return listStack #returning the new modified listStack back
    #checking if the listStack is empty then returning the listStack as it is because there's nothing to delete
    else:
        print("The list is empty.")
        return listStack