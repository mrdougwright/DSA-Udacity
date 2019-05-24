class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items and self.items.pop()

    def top(self):
        if self.items:
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0
