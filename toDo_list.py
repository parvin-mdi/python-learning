import csv

class Task:
    def __init__(self, name, priority, description):
        self.name = name
        self.priority = priority
        self.description = description

    def task_defining(self):
        return f"🟣{self.name} is a task with {self.priority} priority level.\n🟣This task is about: {self.description}."


class ToDoList:
    def __init__(self, name):
        self.name = name
        self.board = []

    def board_introducing(self):
        print(f"\n------{self.name}------")

    def add_task(self, task):
        self.board.append(task)
        print("📥 You add a new task in the board.")

    def show_task(self):
        for task in self.board:
            print(f"\n-----{task.name}-----")
            print(task.task_defining())

    def delete_task(self, task):
        self.board.remove(task)
        print("📤 You delete this taask from the board.")

    def save_task(self, export_file_name):
        with open(export_file_name, 'w', newline='') as csvfile:
            for task in self.board:
                spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(['name'] + ['priority'] + ['description'])
                spamwriter.writerow([task.name] + [task.priority] + [task.description])


print("\n🔅🔆This is a board that you can add task to it, see👀, save💾 and delete🪦 them.🔆🔅")
print("\n💡 Here are some points that you need.")
print(" 1️⃣ In every steps, answer the question in a format that writes in the parantes.")
print(" 2️⃣ Please notice that if you want to save, show or delete a file, at first you should add it to the board.")
print(" 3️⃣ If you add a task to the board, you can't edit it. you should delete it and add a new task to the board.")
print(" 4️⃣ All steps are clear enough.")
print("\nNow you can start. \n😊enjoy it.")

board_name = input("\n⌨️ At first, enter a name for the board: ")
board = ToDoList(board_name)
board.board_introducing()

add_new_task = True

while(add_new_task):
    print("\n---ADD TASK---")
    answer_add_task = input("💻 Do you want to add a new task to the board? (Yes or No)").lower()
    if (answer_add_task == "y" or answer_add_task ==  "yes"):
        action = True

        add_file = True
        while(add_file):
            print("\n---IMPORT TASK---")
            answer_add_task_with_file = input("💾 Do you want to add a task with file? (Yes or No)").lower()
            if (answer_add_task_with_file == "y" or answer_add_task_with_file == "yes"):
                import_file_name = input("\n⌨️ Please enter the name of your file. (Ex: task.csv)")
                with open(import_file_name, newline='') as csvfile:
                    spamreader = csv.reader(csvfile)
                    for row in spamreader:
                        task_name = row[0]
                        task_priority = row[1]
                        task_description = row[2]
                task = Task(task_name, task_priority, task_description)
                add_file = False

            elif (answer_add_task_with_file == "n" or answer_add_task_with_file == "no"):
                print("\n---WRITE TASK---")
                task_name = input("🟣 Enter a name for task: ")
                task_priority = input("🟣 Enter a priority for task:")
                task_description = input("🟣 Enter a description for task:")
                task = Task(task_name, task_priority, task_description)
                add_file = False

            else:
                print("\n🚫 Please enter Yes or No.")


        while(action):
            print("\n---ACTION ON TASK---")
            action_answer = input("🧐 What do you want to do with this task? (Add, Delete, Show, Save or Exit)").lower()

            if(action_answer == "add"):
                board.add_task(task)

            elif(action_answer == "show"):
                board.show_task()   

            elif(action_answer == "delete"):
                board.delete_task(task)

            elif(action_answer == "save"):
                print("\n---EXPORT TASK---")
                export_file_name = input("💾 Please enter a name for your file:")+".csv"
                board.save_task(export_file_name)

            elif(action_answer == "exit"):
                action = False

            else:
                print("\n🚫 Please enter Add, Show, Save or Delete.")

    elif (answer_add_task == "n" or answer_add_task == "no"):
        add_new_task = False
        print("\n---THE END---")
        print("🥺 I hope see you soon. 👋")

    else:
        print("\n🚫 Please enter Yes or No.")
    


