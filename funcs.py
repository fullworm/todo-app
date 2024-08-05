import re as re

def ReadFile(path):
    x = []
    with open(path, "r") as tasks:
        x = tasks.readlines() 
        tasks.close()
    return x

def WriteList(tasks, path):
    with open(path, "w") as content:
        for task in tasks:
            content.writelines(task + "\n")
        content.close()
    return

def ClearList(path):
    open(path, "w").close()
    return

def ReplaceNumber(tasks: list) -> list:
    new_tasks = []
    for task in tasks:
        new_task = re.sub(r'\d+', f"{len(new_tasks)+1}", task)
        new_tasks.append(new_task)
    return new_tasks

