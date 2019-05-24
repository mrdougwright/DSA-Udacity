class HashTable:
    def __init__(self):
        self.table = [None]*1000

    def store(self, string):
        key = self.calculate_hash_value(string)
        if self.table[key] != None:
            self.table[key].append(string)
        else:
            self.table[key] = [string]

    def lookup(self, string):
        key = self.calculate_hash_value(string)
        if self.table[key] != None:
            if string in self.table[key]:
                return key
        return -1

    def calculate_hash_value(self, string):
        hash_code = (ord(string[0]) * 100) + ord(string[1])
        return hash_code % len(self.table)
