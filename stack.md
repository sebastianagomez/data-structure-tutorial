### [<- Home](welcome.md)

# Stack

## Introduction

A Stack in a type of Data Structure that follows a particular order in how operations are performed. It stores items using the Last In, First Out (LIFO) method. Add to the back, but pull from the back as well.

An example of a stack, in a real-world scenario, think of a stack of plates. When you put plates away, you put them on top of the other clean plates that were already there, but when you need a plate to use, you pull from the top.

![Stack](stack.jpeg)

## Uses of Stacks

- A Stack can be used for evaluating expressions consisting of operands and operators.
- Stacks can be used for Backtracking, i.e., to check parenthesis matching in an expression.
- It can also be used to convert one form of expression to another form.
- It can be used for systematic Memory Management.

## Implementing Stacks

Operation | Description | Time Complexity
-------- | -------- | --------
.isEmpty() | The stack.isEmpty() method returns True if the stack is empty. Else, returns False | O(1)
.length() | The stack.length() method returns the length of the stack. | O(1)
.top() | The stack.top() method returns a pointer/reference to the top element in the stack. | O(1)
push(x) | The stack.push() method inserts the element, x to the top of the stack. | O(1)
.pop() | The stack.pop() method removes the top element of the stack and returns it. | O(1)

## Example of Stack

``` python

class Tasks:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
    # Add a task to the front of the list
        if task in self.tasks:
            return False
        self.tasks.append(task)
        return True

    def remove_current_task(self):
    # Remove the current task when finished or not needed
        if len(self.tasks) <= 0:
            return
        # if there is a task in the stack, pop off the current task
        return self.tasks.pop()

    def next_task(self):
    # See what is next to do, in order of priority
        print(self.tasks[-1])
        return


task = Tasks()
task.add_task('Hello')
task.add_task('How are you')
task.next_task()  # Output: How are you
task.add_task('I am so hungry')
task.next_task()  # Output: I am so hungry
task.remove_current_task()
task.add_task('Slice of pizza')
task.remove_current_task()
task.remove_current_task()
task.next_task()  # Output: Hello

```

## Problem to Solve

Now here is a problem where you can sort a binary tree:

[Stack](stack.py)

Solution:

[Stack Solution](stack_solution.py)