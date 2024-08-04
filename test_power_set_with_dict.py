import unittest


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
        return self.power_set.get(i) is not None

    def remove(self, value: str):
        i = self.hash_func(value)
        if self.power_set.get(i) is None:
            return False
        self.power_set.pop(i)
        return True

    def intersection(self, set2: set):
        intersected_set = []
        for value in set2:
            if self.get(value):
                intersected_set.append(value)
        return set(intersected_set)

    def union(self, set2: set):
        union_set = []
        for value in set2:
            if not self.get(value):
                union_set.append(value)
        return set(union_set + list(self.power_set.values()))

    def difference(self, set2: set):
        difference_set = []
        for value in self.power_set.values():
            if value not in set2:
                difference_set.append(value)
        return set(difference_set)

    def issubset(self, set2: set):
        for value in set2:
            if not self.get(value):
                return False
        return True


class TestPowerSet(unittest.TestCase):
    def setUp(self):
        self.ps = PowerSet()

    def test_put_and_size(self):
        self.assertEqual(self.ps.size(), 0)
        self.ps.put("a")
        self.assertEqual(self.ps.size(), 1)
        self.ps.put("b")
        self.assertEqual(self.ps.size(), 2)
        self.ps.put("a")  # add duplicated value
        self.assertEqual(self.ps.size(), 2)

    def test_get(self):
        self.ps.put("a")
        self.assertTrue(self.ps.get("a"))
        self.assertFalse(self.ps.get("b"))

    def test_remove(self):
        self.ps.put("a")
        self.assertTrue(self.ps.remove("a"))
        self.assertFalse(self.ps.get("a"))
        self.assertFalse(self.ps.remove("b"))  # remove non-existent element

    def test_intersection(self):
        # empty power set
        set2 = {"b", "c"}
        self.assertEqual(self.ps.intersection(set2), set())
        self.ps.put("a")
        self.ps.put("b")
        set2 = {"b", "c"}
        self.assertEqual(self.ps.intersection(set2), {"b"})
        set2 = {"c", "d"}
        self.assertEqual(self.ps.intersection(set2), set())

    def test_union(self):
        self.ps.put("a")
        self.ps.put("b")
        set2 = {"b", "c"}
        self.assertEqual(self.ps.union(set2), {"a", "b", "c"})
        set2 = {"d", "e"}
        self.assertEqual(self.ps.union(set2), {"a", "b", "d", "e"})

    def test_difference(self):
        self.ps.put("a")
        self.ps.put("b")
        set2 = {"b", "c"}
        self.assertEqual(self.ps.difference(set2), {"a"})
        set2 = {"a", "b"}
        self.assertEqual(self.ps.difference(set2), set())

    def test_issubset(self):
        self.ps.put("a")
        self.ps.put("b")
        self.assertTrue(self.ps.issubset({"a"}))
        self.assertFalse(self.ps.issubset({"a", "b", "c"}))
        self.assertFalse(self.ps.issubset({"c", "d"}))


if __name__ == '__main__':
    unittest.main()
