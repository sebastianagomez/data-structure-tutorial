class Node:
    def __init__(self, Value):
        self.Value = Value
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    # Code to print out the entire list
    def print_list(self):
        node = self.head
        # while the node is not nothing, print the value of the node, and move to the next one. 
        while node != None:
            print("\n - " + node.Value)
            node = node.next

    # function to add insert a new value at the head.
    def insert(self):
        new_node = Node(input("\nWhat item do you want to add? \n\n-> "))
        # point the next of the new node to the current head.
        new_node.next = self.head
        self.head = new_node

    def remove(self):
        if self.head != None:
            self.head = self.head.next

def main():
    todo_list = Linked_List()
    do = input("\nAdd to list (a)\n\nRemove from list (r) \n\nPrint list (p) \n\nExit (e) \n\n-> ")
    while True:
        # If exit was chosen, exit
        if do == "e" or do == "E":
            break
        # If add was chosen, insert a node at the head
        elif do == "a" or do == "A":
            todo_list.insert()
        # If remove was chosen, remove a node from the head
        elif do == "r" or do == "R":
            todo_list.remove()
        # If print was chosen, print the list
        elif do == "p" or do == "P":
            todo_list.print_list()
        do = input("\nAdd to list (a),\n\nRemove from list (r), \n\nPrint list (p), \n\nExit (e) \n\n-> ")

if __name__ == "__main__":
    main()