class Tasks:
    def __init__(self):
        self.tasks = []
        self.history = []

    def add_task(self, task):
    # Add a task to the front of the list
        if task in self.tasks:
            return False
        # Add that task to the history
        self.history.append(('add', task))
        # If the task is not in the stack, add the task
        self.tasks.append(('add', task))
        return True

    def remove_current_task(self):
    # Remove the current task when finished or not needed
        if len(self.tasks) <= 0:
            return
        # if there is a task in the stack, pop off the current task
        taskToDelete = self.tasks.pop()
        # add that task to the history
        self.history.append(('remove', taskToDelete[1]))
        return

    def next_task(self):
    # See what is next to do, in order of priority
        print(self.tasks[-1][1])
        return

    #####################
    ##    Problem #1   ##
    #####################
    # reverse method allows you to reverse the task list to view all the tasks from oldest to newest
    def reverse(self):
        # Create an empty list to help style the output
        valuesToPrint = []
        for tuple in self.tasks:
            # Append each value of the tuple to the list
            valuesToPrint.append(tuple[1])
        print(valuesToPrint)

    #####################
    ##    Problem #2   ##
    #####################
    # see_all_tasks method allows you to look at what is todo within the whole stack
    def see_all_tasks(self):
        # Create an empty list to help style the output
        valuesToPrint = []
        for tuple in self.tasks[::-1]:
            # Append each value of the tuple to the list
            valuesToPrint.append(tuple[1])
        print(valuesToPrint)

    #####################
    ##    Problem #3   ##
    #####################
    # is_empty method allows you to see if the stack is empty or not
    def is_empty(self):
        if len(self.tasks) != 0:
            print(False)
            return False
        print(True)
        return True

print('\n##########################################\n')

task = Tasks()
task.add_task('Hello')
task.add_task('How are you')
task.add_task('I am so hungry')
task.next_task()  # Output: I am so hungry
task.remove_current_task()

print('\n##################### Problem #1 #####################\n')
task.reverse()  # Output: ['Hello', 'How are you']
task.add_task('Slice a Pizza')
task.add_task('Go to the cinema')
task.add_task('Play football')

print('\n##################### Problem #2 #####################\n')
task.see_all_tasks() # Output: ['Play football', 'Go to the cinema', 'Slice a Pizza', 'need clothes', 'yo yo']
task.remove_current_task()
task.remove_current_task()

print('\n##################### Problem #3 #####################\n')
task.is_empty()  # Output: False
task.next_task()  # Output: Slice a Pizza
task.add_task('World cup')