import stackFunc
import listFunc
import beautify
from dataManager import getValidInt

#function to display main menu options
def mainMenu(listStack):
    #clearing the screen and printing the options
    beautify.clear_screen()
    beautify.printHeading("TO-DO LIST")
    print("Hello Abhay,")
    print("1. Create a new list.")
    print(f"2. Work on existing list. ({len(listStack)} lists)")
    print("3. Delete a list")
    print("4. Exit the program")

    #getting the user choice
    beautify.printBorder(beautify.findColumn(0.5))
    choice = getValidInt("Enter your choice", "That's not a valid choice try again")

    #matching the user choice to desired cases
    match choice:

        #creating a new list
        case 1:
            #the loop should run until user decides to stop creating more lists
            while True:
                listStack = stackFunc.createList(listStack)
                choice = getValidInt("Do you want to create more lists?\n 1 for yes 0 for no", "That's not a valid answer, try again.")
                if choice != 1:
                    break
        
        #working on the existing list
        case 2:
                beautify.clear_screen()
                beautify.printHeading("Choose a list to work on")
                stackFunc.showListStack(listStack)
                beautify.printBorder(beautify.findColumn(0.5))
                # condition to check if there are atlease one list in the listStack to work on
                if len(listStack) != 0:
                    listIndex = getValidInt("Enter the index of list you want to choose", "That's not a valid answer, try again.")

                    #looping until user selects the correct index of the list
                    while not 1 <= listIndex <= len(listStack):
                        listIndex = getValidInt(f"That index doesnt exist\n Enter between 1-{len(listStack)}")

                    #calling the listMenu function with the index of the chosen list to display actions on that list
                    listMenu(listStack, listIndex-1) 
                else:
                    print("There are no lists to work on yet")
                    while True:
                        choice = getValidInt("Do you want to go back to main menu and create a new list?\n 1 for yes 0 for no.")
                        if choice == 1:
                            break

                
        #deleting a list from the listStack
        case 3:

            #looping until user decides to stop deleting lists
            while True:
                listStack = stackFunc.deleteList(listStack)
                beautify.printBorder(beautify.findColumn(0.5))
                choice = getValidInt("Do you want to delete more lists?\n 1 for yes 0 for no", "That's not a valid answer, try again.")
                if choice != 1:
                    break
        
        #exiting the function
        case 4:
            return -1
        
        #for any unknown value it'll rerun the function
        case _ :
            pass

#function to display the actions to be performed at a particular list
def listMenu(listStack, listIndex):
   #loop until the user wants to stay inside
   while True:
        chosenList = listStack[listIndex]
        beautify.clear_screen()
        beautify.printHeading(f"List: {chosenList.nameOfList}")
        #To check if there exist any tasks in the list
        if len(chosenList.mainTasks) == 0:
            print('There are no tasks in ths list, choose the option from below to add tasks')
        else:
            print("Tasks..")
            chosenList.showTask()
        #printing the options 
        beautify.printBorder(beautify.findColumn(0.5))
        print("Choose from the options below")
        print("1. Add a new task to the list")
        print("2. Delete a task from the list")
        print("3. Go back to main menu")
        beautify.printBorder(beautify.findColumn(0.5))
        choice = getValidInt("Enter your choice")
        # matching the case with the desired choice.
        match choice:
            #case to add a new task to the list, and loop until user doesn't want to add any more tasks
            case 1:
                while True:
                    beautify.clear_screen()
                    beautify.printHeading(f"Add new task to {chosenList.nameOfList}")
                    listStack = listFunc.addTaskIntoList(listStack, listIndex)
                    beautify.printBorder(beautify.findColumn(0.5))
                    choice = getValidInt(inpPrompt="Do you want to add more tasks to the list?\n 1 for yes 0 for no")
                    if choice != 1:
                        break
            
            #case to delete a task from the list, and loop until user doesn't want to delete any more tasks
            case 2:
                while True:
                    beautify.clear_screen()
                    beautify.printHeading(f"Delete a task from {chosenList.nameOfList}")
                    listStack = listFunc.removeTaskFromList(listStack, listIndex)
                    beautify.printBorder(beautify.findColumn(0.5))
                    choice = getValidInt(inpPrompt="Do you want to delete more tasks from the list?\n 1 for yes 0 for no")
                    if choice != 1:
                        break
            
            #case to return back to the main menu function
            case 3:
                return
            
            #case to handle any unknown value and rerun the function
            case _ :
                pass