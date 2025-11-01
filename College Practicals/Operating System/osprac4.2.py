import threading

lock = threading.Lock()
sharedSum = 0

def addFibonacciSum(n):
    global sharedSum
    a,b = 0,1
    for i in range(n):
        with lock:
            sharedSum +=a
            a,b = b,a+b
threads = []

for i in range(3):
    t =threading.Thread(target=addFibonacciSum,args=(5,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Total no of Fibonacci nos (shared): ", sharedSum)