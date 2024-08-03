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
        return 
            
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
        return None
             
    def find(self, value: str):
        if self._is_zero_size():
            return None
        i = self.hash_fun(value)
        if self.slots[i] == value:
            return i
        # Check other indices for collision case
        return self._find_value(i, value)


class PowerSet(HashTable):
    def __init__(self, sz, stp):
        super().__init__(sz, stp)
        self.power_set = [None] * sz
        self.set_values = []

    def size(self):
        return len(self.set_values)

    def _find_empty_slot(self, i: int, value: str):
        visited_indices = set()
        while True:
            if (i in visited_indices) or (self.power_set[i] == value):
                break
            if self.power_set[i] is None:
                return i
            visited_indices.add(i)
            i = (i + self.step) % self.size
        return None

    def _find_value(self, i: int, value: str):
        visited_indices = set()
        while True:
            if i in visited_indices:
                break
            if self.power_set[i] == value:
                return i
            visited_indices.add(i)
            i = (i + self.step) % self.size
        return None

    def put(self, value: str):
        if self._is_zero_size():
            return None
        i = self.hash_fun(value)
        empty_i = self._find_empty_slot(i, value)
        if not empty_i is None:
            self.power_set[empty_i] = value
            self.set_values.append(value)
            return empty_i
        return None

    def get(self, value: str):
        if self._is_zero_size():
            return False
        i = self.hash_fun(value)
        if not self._find_value(i, value) is None:
            return True
        return False

    def remove(self, value: str):
        if self._is_zero_size():
            return False
        i = self.hash_fun(value)
        searching_index = self._find_value(i, value)
        if not searching_index is None:
            self.power_set[searching_index] = None
            self.set_values.remove(value)
            return True
        return False

    def intersection(self, set2: set):
        intersected_set = []
        for v in set2:
            if self.get(v):
                intersected_set.append(v)
        return intersected_set 

    def union(self, set2: set):
        union_set = []
        for v in set2:
            if not self.get(v):
                union_set.append(v)
        return self.set_values + union_set 

    def difference(self, set2: set):
        diff_set = []
        for v in self.set_values:
            if not v in set2:
                diff_set.append(v)
        return diff_set

    def issubset(self, set2: set):
        for v in set2:
            if not self.get(v):
                return False
        return True




