import threading
import time
import random

mutex = threading.Semaphore(1)
db = threading.Semaphore(1)

shared_Data = 0
rc = 0 
running  = True

def reader(reader_id):
    global rc, shared_Data, running
    while running:
        # Entry section
        mutex.acquire()
        rc += 1
        if rc == 1:      # first reader locks db
            db.acquire()
        mutex.release()

        # Critical section
        print(f"[Reader] {reader_id} reads {shared_Data}")
        time.sleep(random.uniform(0.2, 0.5))

        # Exit section
        mutex.acquire()
        rc -= 1
        if rc == 0:      # last reader unlocks db
            db.release()
        mutex.release()

        # Pause before next read
        time.sleep(random.uniform(0.5, 1.0))


def writer(writer_id):
    global shared_Data, running
    while running:
        db.acquire()  # Exclusive access
        shared_Data += 1
        print(f"[Writer] {writer_id} writes {shared_Data}")
        time.sleep(random.uniform(0.3, 0.6))
        db.release()

        # Pause before next write
        time.sleep(random.uniform(0.8, 1.5))

if __name__ == "__main__":
    readers = [threading.Thread(target=reader, args=(i,)) for i in range(3)]
    writers = [threading.Thread(target=writer, args=(i,)) for i in range(2)]

    for t in readers + writers:
        t.start()

    time.sleep(10)   # Run simulation for 10 sec
    running = False  # Stop all threads

    for t in readers + writers:
        t.join()

    print("Simulation finished.")