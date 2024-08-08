class BloomFilter:
    def __init__(self, f_len):
        self.filter_len = f_len
        self.bit_array = bytearray(self.filter_len // 8)

    def _set_bit(self, i):
        byte_index = i // 8
        bit_index = i % 8
        self.bit_array[byte_index] |= (1 << bit_index)

    def _get_bit(self, i):
        byte_index = i // 8
        bit_index = i % 8
        return (self.bit_array[byte_index] >> bit_index) & 1
            
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
        if self._get_bit(i1) == 0:
            self._set_bit(i1)
        if self._get_bit(i2) == 0:
            self._set_bit(i2)
        return None

    def is_value(self, str1: str):
        i1 = self.hash1(str1)
        i2 = self.hash2(str1)
        if (self._get_bit(i1) == 1) and (self._get_bit(i2) == 1):
            return True
        return False




