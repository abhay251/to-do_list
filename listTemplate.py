class listTemplate:
    
    def __init__(self, nameOfList, mainTasks = None):
        self.nameOfList = nameOfList
        self.mainTasks = mainTasks if mainTasks is not None else []
    
    def addTask(self, task):
        self.mainTasks.append(task)

    def removeTask(self, index):
        del self.mainTasks[index]
    
    def showTask(self):
        for index,task in enumerate(self.mainTasks, start=1):
            print(f"{index}. {task}")