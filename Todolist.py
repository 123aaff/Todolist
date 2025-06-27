from datetime import datetime

todolist = []

def start():
    print(f"You have {len(todolist)} items in your to do list")
    print("""What would you like to do first?
             1: Add a tast to the list
             2: Update a task
             3: Remove a task from the list
             4: See your list
             5: Close the app""")
    select = int(input("select an option: "))
    if select == 1:
        add_task()
    elif select == 2:
         update_task()
    elif select == 3:
        remove_task()
    elif select == 4:
        list_task()
    elif select == 5:
        exit
    else:
        print("Wrong input please try again")
        start()




def add_task():
    add = input("What would you like to add to the list? \n")
    description = input("Could you give a short description of the task: \n")
    status = input("Have you already started work on this task (Y/N) \n").upper()
    createddate = datetime.now()
    if status == "Y":
        todolist.append({
            "id": 1,
            "Task name": add,
            "Description": description,
            "Status": "in progress",
            "Created at": createddate.date()
            })
    elif status == "N":
        todolist.append({
            "id": len(todolist) + 1,
            "Task name": add,
            "Description": description,
            "Status": "to do",
            "Created at": createddate.date()
            })
    else:
        print("Something went wrong")
    start()

def update_task():
     print("Before you update a task, you should see your list again")
     for task in todolist:
          print(task.get("Task name"))
     try:
        update = int(input("Which task do you want to update? (p.s The first item in the list is 0) "))
        print(todolist[update])
        change = input("What would you like to change? (T)ask name, (D)escription, or (S)tatus? ").upper()
        if change == "T":
            name = input('What would you like to call it? \n')
            todolist[update]["Task name"] = name
            updateddate = datetime.now()
            todolist[update]["Updated at"] = updateddate.date()
            print("Here is the updated version: ")
            print(todolist[update])
            start()
        elif change == "D":
            new_description = input("Could you give a short description of the task: \n")
            todolist[update]["Description"] = new_description
            updateddate = datetime.now()
            todolist[update]["Updated at"] = updateddate.date()
            print("Here is the updated version: ")
            print(todolist[update])
            start()
        elif change == "S":
            while True:
                new_status = input("What is the status? (I)n progress or (D)one ").upper()
                if new_status == "I":
                    todolist[update]["Status"] = "in progress"
                    updateddate = datetime.now()
                    todolist[update]["Updated at"] = updateddate.date()
                    print("Here is the updated version: ")
                    print(todolist[update])
                    start()
                elif new_status == "D":
                    todolist[update]["Status"] = "done"
                    updateddate = datetime.now()
                    todolist[update]["Updated at"] = updateddate.date()
                    print("Here is the updated version: ")
                    print(todolist[update])
                    start()
                else:
                    print("Invalid option, try again")
           
     except:
          ("Invalid option, try again")
          update_task()
    
def remove_task():
    print("Before you remove a task you should see your list again")
    for task in todolist:
        print(task.get("Task name"))
    try:
        remove = int(input("Which task do you want to remove? (p.s The first item in the list is 0) "))
        print(todolist[remove])
        verification = input('Are you sure you want to remove this from the list? (Y/N) ').upper()
        if verification == "Y":
            del todolist[remove]
            print("The task has been succesfully removed from your list")
            print(f"This is your current to do list {task.get("[Task name]")} ")
        else:
            start()

    except:
        ("Invalid option, try again")


def list_task():
    print("How would you like to list your tasks")
    method = input("Do you want to see your tasks that are (C)ompleted, (I)n progress, or (Y)et to be started: ").upper()
    if method == "C":
        for task in todolist:
            if task.get("Status") == "done":
                print(task.get("Task name"))
                start()
    elif method == "I":
        for task in todolist:
            if task.get("Status") == "in progress":
                print(task.get("Task name"))
                start()
    elif method == "Y":
        for task in todolist:
            if task.get("Status") == "to do":
                print(task.get("Task name"))
                start()






print("Welcome to your favourite to do list app")
start()
