import time
def sum(n):
    startTime =time.perf_counter()
    sum = (n*(n-1)/2)
    endTime = time.perf_counter()
    timeRequired = endTime - startTime
    print("The sum of natural number",n,"is: ",sum)
    print("The time required is: ",timeRequired)
