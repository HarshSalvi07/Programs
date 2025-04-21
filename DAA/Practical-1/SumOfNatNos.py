import time
def sum(n):
    sum = 0
    startTime = time.perf_counter()
    for i in range(1,n+1):
        sum += i
        endTime = time.perf_counter()
        timeUsed = endTime - startTime
    print("The sum of natural nos from 1 to ",n,"is: " ,sum)
    print("The time required is: ",timeUsed)
