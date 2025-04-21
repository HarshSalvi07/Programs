class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,data):
        self.queue.append(data)
        return True

    def dequeue(self):
        self.queue.pop(-1)
        return True

    def isEmpty(self):
        return len(self.queue) == 0

    def length(self):
        return len(self.queue)

    def print(self):
        print(self.queue)

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

queue.print()

queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.print()

print(queue.isEmpty())
print(queue.length())
