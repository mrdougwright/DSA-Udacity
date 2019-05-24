class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:

    def __init__(self, initial_size = 10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)
        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key is already present in the map, and update it's value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in the chain --> create a new entry and place it at the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1

    def delete(self, key):
        previous = None
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]

        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next
        pass

    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def get_bucket_index(self, key):
        return self.get_hash_code(key)

    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        hash_code = 0
        current_coefficient = 1
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                     # compress hash_code
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets # compress coefficient
        return hash_code % num_buckets                              # one last compression before returning

    def size(self):
        return self.num_entries


hash_map = HashMap()

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)

print("size: {}".format(hash_map.size()))


print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("size: {}".format(hash_map.size()))

# Notes
# On average, the distribution of entries is such that if we have n entries and b buckets,
# then each bucket does not have more than n/b key-value pair entries.
#
# Therefore, because of our choice of hash functions, we can assume that the time complexity is 𝑂(𝑛𝑏)
# . This number which determines the load on our bucket array n/b is known as load factor.
