import threading
import time

def task(name,delay):
    print(f"[{time.strftime('%H:%M:%S')}] Task {name} started")
    time.sleep(delay)
    print(f"[{time.strftime('%H:%M:%S')}] Task {name} finished")

def sequential():
    print("------Sequential Execution--------")
    startTime = time.time()

    task("A",1)
    task("B",2)
    task("C",3)

    endTime = time.time()
    print(f"Total time taken for sequentail execution is {endTime - startTime:2f} seconds")

def multiThreaded():
    print("--------Multi-Threaded Execution----------")
    startTime = time.time()

    threads = [
        threading.Thread(target=task, args=("A", 1)),
        threading.Thread(target=task, args=("B", 2)),
        threading.Thread(target=task, args=("C", 3))
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    endTime = time.time()
    print(f"Total time taken for multi-threaded execution is {endTime - startTime:2f} seconds")

sequential()
multiThreaded()