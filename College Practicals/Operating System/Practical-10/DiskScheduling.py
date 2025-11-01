import random
class DiskScheduling:
    def __init__ (self,requests,head,disk_size=200):
        self.requests = requests[:]  #copy
        self.head = head
        self.disk_size = disk_size

    def fcfs(self):
        distance = 0
        head = self.head
        order = []
        for req in self.requests:
            distance += abs(head - req)
            order.append(req)
            head = req
            return order, distance
        
    def sstf(self):
        distance = 0
        head = self.head
        requests = self.requests[:]
        order = []
        while requests:
            closest = min(requests, key=lambda x: abs(x-head))
            distance += abs(head-closest)
            order.append(closest)
            head = closest
            requests.remove(closest)
        return order,distance
    
    def cscan(self):
        distance = -
        head = self.head
        requests = sorted(self,requests)
        order = []
        right = [r for r in requests if r >= head]
        left = [r for r in requests if r < head]
