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
        # 2 empty sets
        set2 = PowerSet()
        self.assertEqual(list(self.ps.intersection(set2).power_set.values()), [])
        # core set is empty
        set2 = PowerSet()
        set2.put("b")
        set2.put("c")
        self.assertEqual(list(self.ps.intersection(set2).power_set.values()), [])
        # default intersection
        self.ps.put("a")
        self.ps.put("b")
        set2 = PowerSet()
        set2.put("b")
        set2.put("c")
        self.assertEqual(list(self.ps.intersection(set2).power_set.values()), ["b"])
        # test
        set2 = PowerSet()
        set2.put("c")
        set2.put("d")
        self.assertEqual(list(self.ps.intersection(set2).power_set.values()), [])
        # test 
        set2 = PowerSet()
        set2.put("a")
        set2.put("b")
        self.assertEqual(list(self.ps.intersection(set2).power_set.values()), ["a", "b"])
        # test with integers (1-100, 50-150)
        self.ps.remove("a")
        self.ps.remove("b")
        for i in range(1, 101):
            self.ps.put(i)
        set2 = PowerSet()
        for i in range(50, 151):
            set2.put(i)
        self.assertEqual(list(self.ps.intersection(set2).power_set.values()), [i for i in range(50, 101)])

    def test_union(self):
        self.ps.put("a")
        self.ps.put("b")
        set2 = PowerSet()
        set2.put("b")
        set2.put("c")
        self.assertEqual(list(self.ps.union(set2).power_set.values()), ["a", "b", "c"])
        set2 = PowerSet()
        set2.put("d")
        set2.put("e")
        self.assertEqual(list(self.ps.union(set2).power_set.values()), ["a", "b", "d", "e"])

    def test_difference(self):
        self.ps.put("a")
        self.ps.put("b")
        set2 = PowerSet()
        set2.put("b")
        set2.put("c")
        self.assertEqual(list(self.ps.difference(set2).power_set.values()), ["a"])
        set2 = PowerSet()
        set2.put("a")
        set2.put("b")
        self.assertEqual(list(self.ps.difference(set2).power_set.values()), [])

    def test_issubset(self):
        self.ps.put("a")
        self.ps.put("b")
        set2 = PowerSet()
        set2.put("b")
        self.assertTrue(self.ps.issubset(set2))
        set2 = PowerSet()
        set2.put("c")
        set2.put("a")
        self.assertFalse(self.ps.issubset(set2))
        set2 = PowerSet()
        self.assertTrue(self.ps.issubset(set2))


# if __name__ == '__main__':
#     unittest.main()


