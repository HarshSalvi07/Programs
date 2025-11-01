import threading

def fibonacci(name, n):
    a,b = 0,1
    print(f"{name} generating {n} Fibonacci numbers")
    for i in range(n):
        print(f"{name}: {a}")
        a,b = b,a+b

thread1 = threading.Thread(target= fibonacci,args=("Thread-1",5))
thread2 = threading.Thread(target= fibonacci,args=("Thread-2",10))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("All fibonacci threads finished")