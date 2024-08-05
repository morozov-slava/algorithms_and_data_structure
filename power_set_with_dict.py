class PowerSet:
    def __init__(self):
        self.power_set = {}

    def hash_func(self, value: str):
        return hash(value)

    def size(self):
        return len(self.power_set)

    def put(self, value: str):
        i = self.hash_func(value)
        if self.power_set.get(i) is None:
            self.power_set[i] = value
        return None

    def get(self, value: str):
        i = self.hash_func(value)
        return self.power_set.get(i) is not None

    def remove(self, value: str):
        i = self.hash_func(value)
        if self.power_set.get(i) is None:
            return False
        self.power_set.pop(i)
        return True

    def intersection(self, set2):
        intersected_ps = PowerSet()
        for value in set2.power_set.values():
            if self.get(value):
                intersected_ps.put(value)
        return intersected_ps

    def union(self, set2):
        union_ps = PowerSet()
        for value in self.power_set.values():
            union_ps.put(value)
        for value in set2.power_set.values():
            if not union_ps.get(value):
                union_ps.put(value)
        return union_ps
        
    def difference(self, set2):
        difference_ps = PowerSet()
        for value in self.power_set.values():
            if not set2.get(value):
                difference_ps.put(value)
        return difference_ps

    def issubset(self, set2):
        for value in set2.power_set.values():
            if not self.get(value):
                return False
        return True




