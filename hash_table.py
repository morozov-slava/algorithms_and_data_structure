class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def _is_zero_size(self):
        return self.size == 0

    def _find_empty_slot(self, i: int):
        visited_indices = set()
        while True:
            if i in visited_indices:
                break
            if self.slots[i] is None:
                return i
            visited_indices.add(i)
            i = (i + self.step) % self.size
            
    def _find_value(self, i: int, value: str):
        visited_indices = set()
        while True:
            if i in visited_indices:
                break
            if self.slots[i] == value:
                return i
            visited_indices.add(i)
            i = (i + self.step) % self.size

    def hash_fun(self, value: str):
        index = sum([(i + ord(x)) for i, x in enumerate(value)]) % self.size
        return index
        
    def seek_slot(self, value: str): 
        if self._is_zero_size():
            return None
        i = self.hash_fun(value)
        if self.slots[i] is None:
            return i
        # Check other indices for collision case
        return self._find_empty_slot(i)
                 
    def put(self, value: str):
        if self._is_zero_size():
            return None
        i = self.hash_fun(value)
        empty_i = self._find_empty_slot(i)
        if not empty_i is None:
            self.slots[empty_i] = value
            return empty_i
             
    def find(self, value: str):
        if self._is_zero_size():
            return None
        i = self.hash_fun(value)
        if self.slots[i] == value:
            return i
        # Check other indices for collision case
        return self._find_value(i, value)




