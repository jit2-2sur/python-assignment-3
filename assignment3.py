class Task:
    # constructor
    def __init__(self, title, description="", status="incomplete"):
        self.title = title
        self.description = description
        self.status = status

    def mark_as_complete(self):
        '''
        this method is to changee status of a task from incomplete to complete
        '''
        self.status = "complete"

    def display_details(self):
        '''
        this method is to display details about a task
        '''
        return f"Task: {self.title} - Status: {self.status}"


class TaskList:
    # constructor
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description="", status="incomplete"):
        '''
        this method is to add tasks
        '''
        task = Task(title, description, status)
        self.tasks.append(task)

    def remove_task(self, title):
        '''
        this method is to remove tasks by their title
        '''
        for i in range(len(self.tasks)):
            if self.tasks[i].title == title:
                del(self.tasks[i])
                break

    def list_tasks(self):
        '''
        this method is to get list of all tasks and display them
        '''
        print("\nTasks: \n")
        for task in self.tasks:
            print(task.display_details(), "\n")

    def find_task(self, title):
        '''
        this method is to find tasks by their title
        '''
        for task in self.tasks:
            if task.title == title:
                return task.display_details()
        return "Task not found!"

    def mark_task_complete(self, title):
        '''
        this method is to mark tasks as complete
        '''
        for task in self.tasks:
            if task.title == title:
                task.mark_as_complete()

    def add_priority_task(self, title, description="", priority="low", status="incomplete"):
        '''
        this method is to add priority tasks
        '''
        priority_task = PriorityTask(title, description, priority, status)
        self.tasks.append(priority_task)

    def find_priority_task(self, title):
        '''
        this method is to find priority tasks by their title
        '''
        for task in self.tasks:
            if isinstance(task, PriorityTask) and task.title == title:
                return task.display_details()
        return "Priority task not found!"


class PriorityTask(Task):
    '''
    PriorityTask is a derived class/ child class which inherits properties from parent class Task
    '''
    # constructor
    def __init__(self, title, description="", priority="low", status="incomplete"):
        super().__init__(title, description, status)
        self.priority = priority

    # overriding the method display_details
    def display_details(self):
        return f"Priority Task: {self.title} - Status: {self.status} - Priority: {self.priority}"


# Sample usage
task_list = TaskList()

# adding tasks and example of method overloading
task_list.add_task("Do homework")
task_list.add_task("Go to the gym", "Cardio workout")

# adding priority tasks
task_list.add_priority_task("Buy groceries", "Milk and eggs", "high")

# getting list of all the tasks
task_list.list_tasks()

# marking a task as complete
print("checking task before changing status: ", task_list.find_task("Go to the gym"))
task_list.mark_task_complete("Go to the gym")
print("checking task after changing status: ", task_list.find_task("Go to the gym"), "\n")

# finding tasks by their title
print(task_list.find_task("Do homework"))
print(task_list.find_task("Do not homework"))  # exception case: if task not found
print(task_list.find_task("Go to the gym"), "\n")

# finding priority tasks by their title
print(task_list.find_priority_task("Buy groceries"))
print(task_list.find_priority_task("Do homework"), "\n")

# remove task example
print("\nbefore deleting:")
task_list.list_tasks()

print("\nafter deleting:")
task_list.remove_task("Do homework")
task_list.list_tasks()