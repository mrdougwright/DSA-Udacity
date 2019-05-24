class Stack:
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, arg):
        if self.next_index == len(self.arr):
            print("Stack Overflow Warning! Increasing stack size...")
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = arg
        self.next_index += 1
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]

    def top(self):
        return self.arr[self.next_index - 1]

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def _handle_stack_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]
        for i, el in enumerate(old_arr):
            self.arr[i] = el

stack = Stack()
stack.push(1)
stack.size()
stack.is_empty()
stack.top()
stack.pop()
