FILEPATH = '.\Exports\To-Do-List\\tasks.txt'


def getTasks():
    with open(
            FILEPATH, 'r') as file:
        localTasks = file.readlines()
    return localTasks


def writeTasks(Tasks):
    with open(
            FILEPATH, 'w') as file:
        localTasks = file.writelines(Tasks)
    return localTasks
