from .ordered_list import Node, OrderedList


class TestOrderedList:

    @staticmethod
    def test_compare():
        ol = OrderedList(asc=True)
        assert ol.compare(5, 3) == 1
        assert ol.compare(7, -2) == 1
        assert ol.compare(3, 5) == -1
        assert ol.compare(-8, -15) == 1
        assert ol.compare(2, 2) == 0
        assert ol.compare(0, 0) == 0

    @staticmethod
    def test_add():
        ol_asc = OrderedList(asc=True)
        ol_asc.add(2)
        assert ol_asc.head.value == 2
        assert ol_asc.tail.value == 2
        ol_asc.add(7)
        assert ol_asc.head.value == 2
        assert ol_asc.tail.value == 7
        ol_asc.add(50)
        assert ol_asc.head.value == 2
        assert ol_asc.tail.value == 50
        ol_asc.add(1)
        assert ol_asc.head.value == 1
        assert ol_asc.tail.value == 50
        # Descending
        ol_desc = OrderedList(asc=False)
        ol_desc.add(2)
        assert ol_desc.head.value == 2
        assert ol_desc.tail.value == 2
        ol_desc.add(7)
        assert ol_desc.head.value == 7
        assert ol_desc.tail.value == 2
        ol_desc.add(50)
        assert ol_desc.head.value == 50
        assert ol_desc.tail.value == 2
        ol_desc.add(1)
        assert ol_desc.head.value == 50
        assert ol_desc.tail.value == 1
    
    @staticmethod
    def test_find():
        ol_asc = OrderedList(asc=True)
        ol_asc.add(2)
        ol_asc.add(7)
        ol_asc.add(4)
        ol_asc.add(50)
        ol_asc.add(1)
        assert ol_asc.find(2).value == 2
        assert ol_asc.find(5) is None
        assert ol_asc.find(50).value == 50
        assert ol_asc.find(1).value == 1
        assert ol_asc.find(150) is None
        assert ol_asc.find(-3) is None
        # Descending
        ol_desc = OrderedList(asc=False)
        ol_desc.add(2)
        ol_desc.add(7)
        ol_desc.add(4)
        ol_desc.add(50)
        ol_desc.add(1)
        assert ol_desc.find(2).value == 2
        assert ol_desc.find(5) is None
        assert ol_desc.find(50).value == 50
        assert ol_desc.find(1).value == 1
        assert ol_desc.find(150) is None
        assert ol_desc.find(-3) is None

    @staticmethod
    def test_len():
        ol_asc = OrderedList(asc=True)
        assert ol_asc.len() == 0
        ol_asc.add(2)
        assert ol_asc.len() == 1
        ol_asc.add(7)
        assert ol_asc.len() == 2
        ol_asc.add(7)
        assert ol_asc.len() == 3
        ol_asc.add(7)
        assert ol_asc.len() == 4
        ol_asc.add(2)
        assert ol_asc.len() == 5

        ol_desc = OrderedList(asc=False)
        assert ol_desc.len() == 0
        ol_desc.add(2)
        assert ol_desc.len() == 1
        ol_desc.add(7)
        assert ol_desc.len() == 2
        ol_desc.add(7)
        assert ol_desc.len() == 3
        ol_desc.add(7)
        assert ol_desc.len() == 4
        ol_desc.add(2)
        assert ol_desc.len() == 5

    @staticmethod
    def test_delete():
        ol_asc = OrderedList(asc=True)
        ol_asc.add(2)
        ol_asc.add(15)
        ol_asc.add(2)
        ol_asc.add(7)
        ol_asc.add(1)

        ol_asc.delete(15)
        assert ol_asc.len() == 4
        assert ol_asc.tail.value == 7
        assert ol_asc.tail.next is None

        ol_asc.delete(1)
        assert ol_asc.len() == 3
        assert ol_asc.head.value == 2
        assert ol_asc.head.prev is None

        ol_asc.delete(2)
        assert ol_asc.len() == 2
        assert ol_asc.head.value == 2
        assert ol_asc.head.prev is None

        ol_asc.delete(7)
        assert ol_asc.len() == 1
        assert ol_asc.head.value == 2
        assert ol_asc.tail.value == 2

        ol_asc.delete(2)
        assert ol_asc.len() == 0
        assert ol_asc.head is None
        assert ol_asc.tail is None


def test_ordered_list():
    TestOrderedList.test_compare()
    TestOrderedList.test_find()
    TestOrderedList.test_add()
    TestOrderedList.test_delete()
    TestOrderedList.test_len()
    return True


