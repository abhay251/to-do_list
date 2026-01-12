import json
from listTemplate import listTemplate as template
import os

# fucntion to take the listStack as an argument and put it as a json format text in the listStack.json file
def encrypt(listStack):
    with open("listStack.json", "w") as file:
        serializableStack = [obj.__dict__ for obj in listStack]
        json.dump(serializableStack,file, indent=4)

#function to access the listStack.json file and convert the json back to the list of listTemplate objects and return them
def decrypt():
    try:
        with open("listStack.json", "r") as file:

            #returning an empty list if the listStack file doesn't contain anything
            if os.stat("listStack.json").st_size == 0:
                return[]
            
            #acutal logic of loading the data from the listStack
            serializableStack = json.load(file)
            listStack = [template(**obj) for obj in serializableStack]
            return listStack
    except(FileNotFoundError, json.JSONDecodeError):
        #returns an empty list if the file doesn't exist or json decode error occurs
        return[]
    
#funtion to get a guranteed integer input. However it doesn't gurantee that the integer is in the desired range
def getValidInt(inpPrompt, errorMsg="That's not a valid answer, try again."):
    while True:
        try:
            return int(input(inpPrompt+"\n"))
        except:
            print(errorMsg)
