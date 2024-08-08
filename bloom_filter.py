class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_array = [0] * self.filter_len
        
    def hash1(self, str1: str):
        # 17
        i = 0
        for c in str1:
            i = ord(c) + i * 17
        i = i % self.filter_len
        return i

    def hash2(self, str1: str):
        # 223
        i = 0
        for c in str1:
            i = ord(c) + i * 223
        i = i % self.filter_len
        return i

    def add(self, str1: str):
        i1 = self.hash1(str1)
        i2 = self.hash2(str1)
        if self.bit_array[i1] == 0:
            self.bit_array[i1] = 1
        if self.bit_array[i2] == 0:
            self.bit_array[i2] = 1
        return None

    def is_value(self, str1: str):
        i1 = self.hash1(str1)
        i2 = self.hash2(str1)
        if (self.bit_array[i1] == 1) and (self.bit_array[i2] == 1):
            return True
        return False




