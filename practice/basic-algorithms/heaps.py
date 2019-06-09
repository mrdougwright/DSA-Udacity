# read and search: O(n)
# insert/remove: O(log n)
class Heap:
    def __init__(self, initial_size):
        self.cbt = [None for _ in range(initial_size)]  # initialize arrays
        self.next_index = 0                             # denotes next index where new element should go

    def size(self):
        return self.next_index

    def _up_heapify(self):
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element > child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element

                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        parent_index = 0

        while parent_index <= self.next_index:
            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            min_element = parent

            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                min_element = min(parent, left_child)

            if right_child is not None:
                min_element = min(right_child, min_element)

            # check if parent is rightly placed
            if min_element == parent:
                return

            if min_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = min_element
                parent_index = left_child_index

            elif min_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = min_element
                parent_index = right_child_index


    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index
        self.next_index += 1

        # double array if next_index out of array
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def remove(self):
        # Remove and return the element at the top of the heap
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # will be overwritten on next insert. why?
        self.cbt[self.next_index] = None
        self._down_heapify()

        return to_remove

# child nodes of parent index:
# formulas: (2 * p) + 1 and (2 * p) + 2
# ex: index 2 => children: 5 & 6

# parent node for child:
# formula: ((c + 1) // 2) - 1
# ex: child 7 => parent: 3

  # Min Heap: each child must be bigger than parent
  #     2
  #    / \
  #   3   7
  #  /\   /\
  # 10 8 17 9
