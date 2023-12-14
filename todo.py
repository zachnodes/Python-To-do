
def main():
    tasks = []

    active = True

    while (active):
        print("----To-do's----")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        enterChoice = int(input("Enter your choice: "))

        if enterChoice == 1:
            numOfTasks = int(input("How many tasks would you like to add: "))
            for i in range(numOfTasks):
                todo = input("What needs to be done: ")
                tasks.append([todo, "Not Done"])

        if enterChoice == 2:
            for i in range(len(tasks)):
                print(tasks[i][0], '- ' + tasks[i][1])

        if enterChoice == 3:
            markDone = int(
                input("Enter the number of the task to mark done: "))
            markDone -= 1
            tasks[markDone][1] = 'Done'
            print("Marked as done!")

        if enterChoice == 4:
            break


main()
