import heapq
q = []
heapq.heappush(q,(2,"Eat,Workout"))
heapq.heappush(q,(1,"Walk"))
heapq.heappush(q,(3,"Sleep"))

while q:
    next_item = heapq.heappop(q)
    print(next_item)
                
