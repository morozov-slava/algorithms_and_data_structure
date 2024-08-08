import unittest


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


class TestBloomFilter(unittest.TestCase):
    def setUp(self):
        self.bf = BloomFilter(32)

    def test_add(self):
        test_set = ["0123456789", "2345678901", "3456789012", "4567890123", "5678901234",
                    "6789012345", "7890123456", "8901234567", "9012345678"
                   ]
        self.bf.add(test_set[0])
        self.assertEqual(self.bf.hash1(test_set[0]), 13)
        self.assertEqual(self.bf.hash2(test_set[0]), 5)

    def test_is_value(self):
        test_set = ["0123456789", "2345678901", "3456789012", "4567890123", "5678901234",
                    "6789012345", "7890123456", "8901234567", "9012345678"
                   ]
        self.bf.add(test_set[0])
        self.assertTrue(self.bf.is_value(test_set[0]))
        self.assertFalse(self.bf.is_value("abc"))
        self.assertTrue(self.bf.is_value(test_set[1]))
        self.assertFalse(self.bf.is_value(test_set[2]))
        self.bf.add(test_set[2])
        self.assertTrue(self.bf.is_value(test_set[2]))


# if __name__ == '__main__':
#     unittest.main()




