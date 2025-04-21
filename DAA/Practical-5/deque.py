from collections import deque
d = deque()
d.append(0)
d.append(2)
d.append(4)
d.append(6)
d.append(8)
d.append(10)

print("Before POP: ",d)
a = d.popleft()
print("After POP: ",d)
print("Value popped: ",a)
