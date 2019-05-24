class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

class Queue:
    # Code here
    def __init__(self):
        self.in_store = Stack()
        self.out_store = Stack()

    def size(self):
        return self.in_store.size() + self.out_store.size()

    def enqueue(self, item):
        self.in_store.push(item)

    def dequeue(self):
        if not self.out_store.items:
            while self.in_store.items:
                self.out_store.push(self.in_store.pop())
        return self.out_store.pop()

# Setup
q = Queue()
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
