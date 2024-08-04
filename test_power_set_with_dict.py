class TestPowerSet:

    @staticmethod
    def test_size():
        ps = PowerSet()
        assert ps.size() == 0
        ps.put("abc")
        ps.put("hwd")
        assert ps.size() == 2

    @staticmethod
    def test_put():
        ps = PowerSet()
        assert ps.put("abc") == 5131920428635776490
        assert ps.put("abc") is None
        assert ps.put("qwe") == 821241285682361358
        assert ps.put("cab") == 983071625819620223
        assert ps.put("cab") is None

    @staticmethod
    def test_get():
        ps = PowerSet()
        ps.put("abc")
        ps.put("qwe")
        ps.put("cab")
        assert ps.get("qwe") is True
        assert ps.get("abc") is True
        assert ps.get("cab") is True
        assert ps.get("bac") is False
        assert ps.get("jkj") is False
        
    @staticmethod
    def test_remove():
        ps = PowerSet()
        ps.put("abc")
        ps.put("qwe")
        ps.put("cab")
        assert ps.remove("cab") is True
        assert ps.remove("cab") is False
        assert ps.remove("mwqef") is False
        assert ps.remove("qwe") is True
        assert ps.remove("abc") is True

    @staticmethod
    def test_intersection():
        ps = PowerSet()
        ps.put("abc")
        ps.put("qwe")
        ps.put("cab")
        assert ps.intersection({"sn", "qwe", "abc", "ppp"}) == {'abc', 'qwe'}
        assert ps.intersection({}) == set()
        assert ps.intersection({"sw", "qqq", "aaa"}) == set()

    @staticmethod
    def test_union():
        ps = PowerSet()
        ps.put("abc")
        ps.put("qwe")
        ps.put("cab")
        assert ps.union({"ppp", "qwe", "abc", "kke"}) == {'abc', 'cab', 'kke', 'ppp', 'qwe'}
        assert ps.union({}) == {'abc', 'cab', 'qwe'}

    @staticmethod
    def test_difference():
        ps = PowerSet()
        ps.put("abc")
        ps.put("qwe")
        ps.put("cab")
        assert ps.difference({"ppp", "qwe", "fb"}) == {'abc', 'cab'}
        assert ps.difference({}) == {'abc', 'cab', 'qwe'}
        assert ps.difference({"cab", "abc", "qwe"}) == set()

    @staticmethod
    def test_issubset():
        ps = PowerSet()
        ps.put("abc")
        ps.put("qwe")
        ps.put("cab")
        assert ps.issubset({}) is True
        assert ps.issubset({"pd", "qwe"}) is False
        assert ps.issubset({"cab", "abc", "qwe", "kkk"}) is False
        assert ps.issubset({"cab", "abc", "qwe"}) is True
        assert ps.issubset({"abc", "cab"}) is True


def test_PowerSet():
    TestPowerSet.test_size()
    TestPowerSet.test_put()
    TestPowerSet.test_get()
    TestPowerSet.test_remove()
    TestPowerSet.test_intersection()
    TestPowerSet.test_union()
    TestPowerSet.test_difference()
    TestPowerSet.test_issubset()
    return True




