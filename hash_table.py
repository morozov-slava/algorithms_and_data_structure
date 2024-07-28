class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        
    def hash_fun(self, value):
        index = sum([(i * ord(x))  for i, x in enumerate(value)]) % self.size
        return index
        
    def seek_slot(self, value): 
        i = self.hash_fun(value)
        if i < self.size:
            return None
        if not self.slots[i] is None:
            return i
                 
    def put(self, value):
        i = self.hash_fun(value)
        if i < self.size:
            return None
        if self.slots[i] is None):
            self.slots[i] = value
            return i
             
    def find(self, value):
        i = self.hash_fun(value)
        if i < self.size:
            return None
        return self.slots[i]
