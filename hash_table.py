class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def _is_zero_size(self):
        return self.size == 0
        
    def hash_fun(self, value):
        index = sum([(i + ord(x)) for i, x in enumerate(value)]) % self.size
        return index
        
    def seek_slot(self, value): 
        if self._is_zero_size():
            return None
        i = self.hash_fun(value)
        if (i >= self.size):
            return None
        if self.slots[i] is None:
            return i
                 
    def put(self, value):
        if self._is_zero_size():
            return None
        i = self.hash_fun(value)
        if i >= self.size:
            return None
        if self.slots[i] is None:
            self.slots[i] = value
            return i
             
    def find(self, value):
        if self._is_zero_size():
            return None
        i = self.hash_fun(value)
        if i >= self.size:
            return None
        if not self.slots[i] is None:
            return i




