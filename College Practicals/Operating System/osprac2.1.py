import multiprocessing
import time
import random

def producer(queue,n_items):
    for i in range(n_items):
        item = random.randint(1,100)
        queue.put(item)
        print(f"Produced: {item}")
        time.sleep(random.uniform(0.5,1.0))

def consumer(queue,n_items):
    for i in range(n_items):
        item = queue.get()
        print(f"Consumed: {item}")
        time.sleep(random.uniform(0.5,1.2))

if __name__ == "__main__":
    N_ITEMS = 10
    queue = multiprocessing.Queue(maxsize=5)

    p = multiprocessing.Process(target=producer,args=(queue,N_ITEMS))
    c = multiprocessing.Process(target=consumer,args=(queue,N_ITEMS))

    p.start()
    c.start()
    p.join()
    c.join()