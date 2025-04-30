import threading
import time
import random

class Buffer:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.in_pointer = 0
        self.out_pointer = 0
        self.mutex = threading.Lock()
        self.empty_slots = threading.Semaphore(size)
        self.full_slots = threading.Semaphore(0)

class Producer(threading.Thread):
    def __init__(self, buffer, id):
        super().__init__()
        self.buffer = buffer
        self.id = id

    def produce(self, item):
        self.buffer.empty_slots.acquire()
        self.buffer.mutex.acquire()

        self.buffer.items[self.buffer.in_pointer] = item
        print(f"Produced: {item} at position {self.buffer.in_pointer}")
        self.buffer.in_pointer = (self.buffer.in_pointer + 1) % self.buffer.size

        self.buffer.mutex.release()
        self.buffer.full_slots.release()

    def run(self):
        for _ in range(10):
            item = random.randint(1, 100)
            print(f"Producer {self.id} producing {item}...")
            self.produce(item)
            time.sleep(random.uniform(0.1, 0.5))

class Consumer(threading.Thread):
    def __init__(self, buffer, id):
        super().__init__()
        self.buffer = buffer
        self.id = id

    def consume(self):
        self.buffer.full_slots.acquire()
        self.buffer.mutex.acquire()

        item = self.buffer.items[self.buffer.out_pointer]
        self.buffer.items[self.buffer.out_pointer] = None  # Clear the slot
        print(f"Consumed: {item} from position {self.buffer.out_pointer}")
        self.buffer.out_pointer = (self.buffer.out_pointer + 1) % self.buffer.size

        self.buffer.mutex.release()
        self.buffer.empty_slots.release()
        return item

    def run(self):
        for _ in range(10):
            item = self.consume()
            print(f"Consumer {self.id} consumed {item}...")
            time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    buffer = Buffer(5)
    producers = [Producer(buffer, i) for i in range(2)]
    consumers = [Consumer(buffer, i) for i in range(2)]

    for p in producers:
        p.start()
    for c in consumers:
        c.start()

    for p in producers:
        p.join()
    for c in consumers:
        c.join()

    print("All producers and consumers have finished.")