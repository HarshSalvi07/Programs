#Node class for singly linked-list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Linked list class to manage tasks
class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self,task):
        new_node = Node(task)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def remove_task(self,task):
        if not self.head: #Remove the first occuurrence of the task without uing prev
            return False  #List is empty
        
        if self.head.data == task:
            self.head = self.head.next #Remove head node
            return True
        
        curr = self.head
        while curr.next:
            if curr.next.data == task:
                curr.next = curr.next.next #Bypass the node
                return True
            curr = curr.next
        return False #Task not found
            
    def display_tasks(self):
        if not self.head:
            print("Task list is empty")
            return
        
        print("Task list: ")
        curr = self.head
        while curr:
            print(" -", curr.data)
            curr = curr.next

    def search_task(self,keyword):
        curr = self.head
        found = False
        keyword = keyword.lower()
        while curr:
            if keyword in curr.data.lower():
                print(f"Found: {curr.data}")
                found = True 
            curr = curr.next
        if not found:
            print("No matching task found")

#Creating an instance of the object
todo = TaskList()

#Adding tasks in the list
todo.add_task("Wish Cristiano Happy Birthday")
todo.add_task("Call Leo Messi about Cristiano party")
todo.add_task("Invite Neymar for samba")
todo.add_task("Play fifa with them after the party")
todo.add_task("Go for a swim with them")

#Displaying tasks
todo.display_tasks()

#Removing a tasks
print("\n Removing 'Go for a swim with them'")
todo.remove_task("Go for a swim with them")

#Displaying tasks
todo.display_tasks()

#Searching tasks
print("\n Searching for 'cristiano:'")
todo.search_task("cristiano")

todo.display_tasks()