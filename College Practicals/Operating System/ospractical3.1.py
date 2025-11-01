import threading
import time

def task(name,delay):
    print(f"Task {name}")
    time.sleep(delay)
    print(f"Task {name} ended after {delay} seconds")

def singleThreaded():
    starTime = time.time()
    task("A",2)
    task("B",2)
    endTime = time.time()
    print(f"Single threaded task execution time {starTime - endTime} seconds")

def multipleThreaded():
    startTime = time.time()

    threadA = threading.Thread(target=task,args=("A",2))
    threadB = threading.Thread(target=task,args=("B",2))

    threadA.start()
    threadB.start()

    threadA.join()
    threadB.join()

    endTime = time.time()

    print(f"Multiple threading execution time {startTime - endTime} seconds")

if __name__ == "__main__":
    print("Running sigle-threaded version: ")
    singleThreaded()

    print("Running multiple-threaded version: ")
    multipleThreaded()