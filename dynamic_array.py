import ctypes


class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i > self.count:
            raise IndexError('Index is out of bounds')
        if i == self.count:
            self.append(itm)
            return None
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        new_array = self.make_array(self.capacity)
        if i == 0:
            new_array[i] = itm
            for j in range(self.count):
                new_array[j+1] = self.array[j]
        else:
            for j in range(i):
                new_array[j] = self.array[j]
            new_array[i] = itm
            for j in range(i, self.count):
                new_array[j+1] = self.array[j]
        self.array = new_array
        self.count += 1

    def delete(self, i):
        if i >= self.count:
            raise IndexError('Index is out of bounds')
        # Check capacity (and resize if necessary)
        if ((self.count - 1) / self.capacity) < 0.50:
            new_capacity = int(self.capacity / 1.5)
        else:
            new_capacity = self.capacity
        if new_capacity > 16:
            self.capacity = new_capacity
        else:
            self.capacity = 16
        # Create new array (without deleted element)
        new_array = self.make_array(self.capacity)
        if i == self.count - 1:
            # to delete last element
            for j in range(i):
                new_array[j] = self.array[j]
        else:
            for j in range(i):
                new_array[j] = self.array[j]
            for j in range(i+1, self.count):
                new_array[j-1] = self.array[j]
        self.array = new_array
        self.count -= 1

    def print_array_elements(self):
        for i in range(self.count):
            print(self.array[i])



