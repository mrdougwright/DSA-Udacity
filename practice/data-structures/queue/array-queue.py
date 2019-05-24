class Queue:
    """Queue implementation with array"""

    def __init__(self, init_size):
        self.queue_size = 0
        self.head = 0
        self.tail = 0
        self.pointer = 0
        self.arr = [None for _ in range(init_size)]

    def enqueue(self, value):
        self._handle_full_capacity()
        self.arr[self.tail] = value
        self.queue_size += 1
        self.tail += 1
        pass

    def dequeue(self):
        value = self.front()
        self.head += 1
        self.queue_size -= 1
        return value

    def front(self):
        return self.arr[self.head]

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size == 0

    def _handle_full_capacity(self):
        if self.tail >= len(self.arr):
            self.queue_size += 50
            self.arr += [None for _ in range(50)]

# Setup
q = Queue(10)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")
