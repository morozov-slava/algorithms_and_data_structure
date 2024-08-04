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
            return i
        return None

    def get(self, value: str):
        i = self.hash_func(value)
        return not self.power_set.get(i) is None

    def remove(self, value: str):
        i = self.hash_func(value)
        if self.power_set.get(i) is None:
            return False
        self.power_set.pop(i)
        return True

    def intersection(self, set2):
        intersected_set = []
        for value in set2:
            if self.get(value):
                intersected_set.append(value)
        return set(intersected_set)

    def union(self, set2):
        union_set = []
        for value in set2:
            if not self.get(value):
                union_set.append(value)
        return set(union_set + list(self.power_set.values()))

    def difference(self, set2):
        difference_set = []
        for value in self.power_set.values():
            if not value in set2:
                difference_set.append(value)
        return set(difference_set)

    def issubset(self, set2):
        for value in set2:
            if not self.get(value):
                return False
        return True




