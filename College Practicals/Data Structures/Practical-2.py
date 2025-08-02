#Define the Node class to represent each element in the linked list
class Node:
    def __init__(self,data):
        self.data = data #Store the data value
        self.next = None #Store the reference to the next node/ Pointer to the next Node (initially none)

#Define the Linked List class
class LinkedList:
    def __init__(self,data):
        self.head = Node(data) #Head pointer to the next node of the list
        self.data = None

#Method to insert a node at the end of the list
    def insert(self,newNode):
        if self.head is None:  #If the list is empty
            self.head = newNode #Make the new node as the head of the list
        else:  #If the list is not empty
            lastNode = self.head  #Start at the head of the list
            while lastNode.next is not None:  #Traverse till the last Node
                lastNode = lastNode.next  #Move to the next Node
            lastNode.next = newNode  #Link the last Node to the new Node

#Method to delete a node by value
    def delete(self,value):
        current = self.head #Start at the head of the list
        previous = None #To keep track of the previous node

        #Case 1 : Node to delete the head Node
        if current is not None and current.data == value:
            self.head = current.next  #Move the head to the next node
            current = None  #Delete the current node
            return #Exit after deletion
    
        #Case 2 : Search for the value to delete
        while current is not None and current.data != value:
            previous = current  #Move the previous to current
            current = current.next #Move the current to next

            #If value is not found in the list
            if current is None:
                print("Value not found in the list")
                return
    
        #Case 3 : Unlink the node to delete it
        previous.next = current.next  #Skip the current node
        current = None  #Delete the current node

#Method to print(Traverse) the Linked list
    def printlist(self):
        currentNode = self.head    #Start from the head
        while currentNode is not None: #Loop till the end of the list
            print(currentNode.data) #Print the data of the current Node
            currentNode = currentNode.next #Move to the next Node

#Create individual node objects with values
fnode = Node(1)  #First Node with data 1
snode = Node(2)  #Second Node with data 2
tnode = Node(3)  #Third Node with data 3

#Create LinkedList object and insert nodes into it
LinkedList = LinkedList(None) #Create a Linked List
LinkedList.insert(fnode) #Insert the first node
LinkedList.insert(snode) #Insert the second node
LinkedList.insert(tnode) #Insert the third node

#Display the list before deletion
print("List before deletion:")
LinkedList.printlist()  #Print the list

#Delete the node with value 2
LinkedList.delete(2)

#Display the list after deletion
print("List afer deleting value 2:")
LinkedList.printlist()