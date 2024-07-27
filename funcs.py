def ReadFile(path):
    x = []
    with open(path, "r") as tasks:
        x = tasks.readlines() 
        tasks.close()
    return x

def WriteList(tasks, path):
    with open(path, "w") as content:
        content.writelines(tasks)
        content.close()
    return
   