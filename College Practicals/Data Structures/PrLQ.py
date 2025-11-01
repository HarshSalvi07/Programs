class Node:
    def __init__(self, data):
        self.data, self.prev, self.next = data, None, None

class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def push(self, data):  # insert at head
        n = Node(data)
        n.next, self.head = self.head, n
        if n.next: n.next.prev = n
        else: self.tail = n
        self.size += 1

    def put(self, data):  # insert at tail
        n = Node(data)
        n.prev, self.tail = self.tail, n
        if n.prev: n.prev.next = n
        else: self.head = n
        self.size += 1

    def insert(self, data, pos=0):  # insert at given position
        if pos <= 0: return self.push(data)       # case 1: at head
        if pos >= self.size: return self.put(data)  # case 2: at tail
        cur = self.head
        for _ in range(pos): cur = cur.next       # case 3: in middle
        n = Node(data)
        n.prev, n.next = cur.prev, cur
        cur.prev.next, cur.prev = n, n
        self.size += 1

    def delete(self, key):  # delete by value
        cur = self.head
        while cur and cur.data != key: cur = cur.next
        if not cur: return  # case 0: not found
        if cur.prev: cur.prev.next = cur.next
        else: self.head = cur.next               # case 1: deleting head
        if cur.next: cur.next.prev = cur.prev
        else: self.tail = cur.prev               # case 2: deleting tail
        self.size -= 1                           # case 3: deleting middle

    def show(self):
        cur = self.head
        while cur: print(cur.data, end=" <-> "); cur = cur.next
        print("None")

    def showRev(self):
        cur = self.tail
        while cur: print(cur.data, end=" <-> "); cur = cur.prev
        print("None")

dll = DoublyLinkedList()
dll.put(10)        # tail insert (empty list -> head=tail=10)
dll.push(20)       # head insert -> 20 <-> 10
dll.put(30)        # tail insert -> 20 <-> 10 <-> 30
dll.insert(25, 2)  # middle insert -> 20 <-> 10 <-> 25 <-> 30
dll.insert(5, 0)   # head insert -> 5 <-> 20 <-> 10 <-> 25 <-> 30
dll.insert(40, 10) # tail insert -> ... <-> 30 <-> 40
dll.show()
dll.showRev()

dll.delete(5)      # delete head
dll.delete(40)     # delete tail
dll.delete(25)     # delete middle
dll.show()
dll.showRev()
