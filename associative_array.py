class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        
    def hash_fun(self, key: str):
        index = sum([(i + ord(x)) for i, x in enumerate(key)]) % self.size
        return index
        
    def is_key(self, key: str):
        return key in self.slots
             
    def put(self, key: str, value):
        i = self.hash_fun(key)
        self.slots[i] = key 
        self.values[i] = value
        
    def get(self, key: str):
        i = self.hash_fun(key)
        if self.slots[i] == key:
            return self.values[i]




