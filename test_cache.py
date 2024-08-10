import unittest


class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def _remove(self, i: int):
        self.slots[i] = None
        self.values[i] = None
        self.hits[i] = 0

    def _hash_fun(self, key: str):
        return hash(key) % self.size

    def _find_key_index(self, key: str):
        try:
            return self.slots.index(key)
        except ValueError:
            return None

    def _find_empty_slot(self, i: int, key: str):
        visited_indices = set()
        while True:
            if i in visited_indices:
                break
            if self.slots[i] is None:
                return i
            visited_indices.add(i)
            i = (i + 1) % self.size
        return None

    def _find_least_used_index(self):
        min_i = 0
        min_hit = self.hits[0]
        for i in range(1, len(self.hits)):
            if self.hits[i] < min_hit:
                min_i = i 
                min_hit = self.hits[i]
        return min_i

    def put(self, key: str, value: str):
        key_i = self._find_key_index(key)
        if key_i is not None:
            self.hits[key_i] += 1
            return None
        i = self._hash_fun(key)
        empty_i = self._find_empty_slot(i, key)
        if empty_i is None:
            empty_i = self._find_least_used_index()
            self._remove(empty_i)
        self.slots[empty_i] = key
        self.values[empty_i] = value
        self.hits[empty_i] += 1
        return None

    def get(self, key: str):
        i = self._hash_fun(key)
        visited_indices = set()
        while True:
            if i in visited_indices:
                break
            if self.slots[i] == key:
                self.hits[i] += 1
                return self.values[i]
            visited_indices.add(i)
            i = (i + 1) % self.size
        return None


class TestNativeCache(unittest.TestCase):

    def setUp(self):
        self.cache = NativeCache(3)

    def test_put_and_get(self):
        self.cache.put('key1', 'value1')
        self.assertEqual(self.cache.get('key1'), 'value1')
        self.assertEqual(self.cache.get('nonexistent_key'), None)

    def test_default_cashe_overflow(self):
        self.cache.put('key1', 'value1')
        self.cache.put('key2', 'value2')
        self.cache.put('key3', 'value3')
        # Check cache overflow
        self.cache.put('key4', 'value4')
        self.assertIsNone(self.cache.get('key2'), None)  # Один из старых элементов должен быть удален
        self.assertEqual(self.cache.get('key1'), 'value1')
        self.assertEqual(self.cache.get('key3'), 'value3')
        self.assertEqual(self.cache.get('key4'), 'value4')

    def test_cache_overflow_for_least_used_key(self):
        self.cache.put('key1', 'value1')
        self.cache.put('key2', 'value2')
        self.cache.put('key3', 'value3')
        self.cache.get('key2')  # Увеличивает использование 'key2'
        self.cache.put('key4', 'value4')  # 'key2' или 'key3' должны быть удалены, так как они используются меньше
        self.assertEqual(self.cache.get('key4'), 'value4')  # 'key1' должен остаться
        self.assertIsNone(self.cache.get('key3'), None)  # 'key2' или 'key3' должен быть удален

    def test_hash_function(self):
        # Проверка корректности хеш-функции в контексте текущего размера кэша
        size = self.cache.size
        key = 'test_key'
        expected_index = hash(key) % size
        self.assertEqual(self.cache._hash_fun(key), expected_index)


# if __name__ == '__main__':
#     unittest.main()




