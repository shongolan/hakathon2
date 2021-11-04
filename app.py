import json

f = open('data.json', )
data = json.load(f)
# assigning the data  list to the variable
task = data['task']
f.close()

while True:
    print("To-Do App\n")
    print("Choose Action")
    print("a) Create a Task\nb) Delete a Task\nc) Update the task\nd) Show all task\ne) View selected task\n0) Exit")
    choice = input("--> ")
    if choice == 'a' or choice == 'A':
        # add a new data
        title = input("Task Title: ")
        content = input("Task Content: ")
        task.append({title: content})
        data = {"task": task}
        f = open("data.json", "w")
        json.dump(data, f)
        f.close()

    elif choice == 'b' or choice == 'B':
        f = open('data.json', )
        data = json.load(f)
        task = data['task']
        f.close()

        if len(task) > 0:
            print("# - Title\n")
            for i in range(len(task)):
                for key, value in task[i].items():
                    print(f"{i} - {key}")
            s = input("select the # of title you want to delete: ")

            # delete the data
            f = open('data.json', )
            data = json.load(f)
            task = data['task']
            del task[int(s)]
            f.close()

            # save to .json file
            data = {"task": task}
            f = open("data.json", "w")
            json.dump(data, f)
            f.close()
            print(f"Task #{s} is successfully deleted.\n")
        else:
            print("The To-Do list is empty...\n")

    elif choice == 'c' or choice == 'C':
        f = open('data.json', )
        data = json.load(f)
        task = data['task']
        f.close()
        if len(task) > 0:
            print("# - Title\n")
            for i in range(len(task)):
                for key, value in task[i].items():
                    print(f"{i} - {key}")
            s = input("select the # of title you want to update: ")

            # update the data
            f = open('data.json', )
            data = json.load(f)
            task = data['task']
            del task[int(s)]
            f.close()
            newTitle = input("New Task Title: ")
            newContent = input("New Task Content: ")
            task.insert(int(s), {newTitle: newContent})

            # save to .json file
            data = {"task": task}
            f = open("data.json", "w")
            json.dump(data, f)
            f.close()
            print(f"Task #{s} is successfully deleted.\n")
        else:
            print("The To-Do list is empty...\n")

    elif choice == 'd' or choice == 'D':
        f = open('data.json', )
        data = json.load(f)
        task = data['task']
        f.close()
        if len(task) > 0:
            print("All your task")
            print("# - Title\n")
            for i in range(len(task)):
                for key, value in task[i].items():
                    print(f"{i} - {key}")
        else:
            print("The To-Do list is empty...\n")

    elif choice == 'e' or choice == 'E':
        f = open('data.json', )
        data = json.load(f)
        task = data['task']
        f.close()
        if len(task) > 0:
            print("All your task")
            print("# - Title\n")
            for i in range(len(task)):
                for key, value in task[i].items():
                    print(f"{i} - {key}")

            select = input("select the # of title you want to view: ")

            # display the selected task
            print("\n")
            for key, value in task[int(select)].items():
                print(f"Title: {key}")
                print(f"Content: {value}")
            print("\n")

        else:
            print("The To-Do list is empty...\n")

    elif choice == '0':
        print("Goodbye!")
        quit()
