import copy

from .linked_list_dummy_node import Node, DummyNode, LinkedList2Dummy


# Empty Linked List
empty_linked_list = LinkedList2Dummy()

# Single node Linked List
n1 = Node(8)
single_node_linked_list = LinkedList2Dummy()
single_node_linked_list.add_in_tail(n1)

# Default linked list
n1 = Node(10)
n2 = Node(11)
n3 = Node(10)
n1.next = n2
n2.next = n3
n2.prev = n1
n3.prev = n2
linked_list_default = LinkedList2Dummy()
linked_list_default.add_in_tail(n1)
linked_list_default.add_in_tail(n2)
linked_list_default.add_in_tail(n3)



class TestLinkedListDummy2:

    @staticmethod
    def test_add_in_head():
        n11 = Node(10)
        n12 = Node(11)
        n13 = Node(10)
        linked_list_add_in_head = LinkedList2Dummy()
        
        linked_list_add_in_head.add_in_head(n11)
        assert linked_list_add_in_head.head.next == n11
        assert linked_list_add_in_head.tail.prev == n11

        linked_list_add_in_head.add_in_head(n12)
        assert linked_list_add_in_head.head.next == n12
        assert linked_list_add_in_head.tail.prev == n11
        assert linked_list_add_in_head.head.next.next == n11
        assert linked_list_add_in_head.tail.prev.prev == n12

        linked_list_add_in_head.add_in_head(n13)
        assert linked_list_add_in_head.head.next == n13
        assert linked_list_add_in_head.tail.prev == n11
        assert linked_list_add_in_head.tail.prev.prev == n12
        assert linked_list_add_in_head.head.next.next == n12
        assert linked_list_add_in_head.head.next.next.value == 11
        assert linked_list_add_in_head.head.next.next.next == n11
        
    @staticmethod
    def test_clean():
        linked_list_default_copy = copy.deepcopy(linked_list_default)
        linked_list_default_copy.clean()
        assert linked_list_default_copy.head.next is None
        assert linked_list_default_copy.tail.prev is None 

    @staticmethod
    def test_delete():
        # TEST-2
        linked_list_default_copy = copy.deepcopy(linked_list_default)
        linked_list_default_copy.delete(10, all=True)
        assert linked_list_default_copy.head.next.value == 11
        assert linked_list_default_copy.tail.prev.value == 11
        # TEST-3
        linked_list_default_copy = copy.deepcopy(linked_list_default)
        linked_list_default_copy.delete(10, all=False)
        assert linked_list_default_copy.head.next.value == 11
        assert linked_list_default_copy.tail.prev.value == 10

    @staticmethod
    def test_find():
        assert linked_list_default.find(10).value == 10 
        assert linked_list_default.find(100) is None

    @staticmethod
    def test_find_all():
        assert len(linked_list_default.find_all(10)) == 2
        assert len(single_node_linked_list.find_all(8)) == 1
        assert empty_linked_list.find_all(100) == [] 

    @staticmethod
    def test_insert():
        # TEST-1
        n111 = Node(10)
        n112 = Node(11)
        linked_list_insert = LinkedList2Dummy()
        
        linked_list_insert.insert(afterNode=None, newNode=n111)
        assert linked_list_insert.head.next == n111
        assert linked_list_insert.tail.prev == n111

        linked_list_insert.insert(afterNode=n111, newNode=n112)
        assert linked_list_insert.head.next == n111
        assert linked_list_insert.head.next.next == n112
        assert linked_list_insert.tail.prev == n112
        assert linked_list_insert.tail.prev.prev == n111
        assert linked_list_insert.tail.prev.prev.value == 10
        
        # TEST-2
        n1111 = Node(100)
        n1112 = Node(111)
        n1113 = Node(122)
        linked_list_insert_1 = LinkedList2Dummy()

        linked_list_insert_1.insert(afterNode=n1112, newNode=n1111)
        assert linked_list_insert_1.head.next == n1111
        assert linked_list_insert_1.tail.prev == n1111

        linked_list_insert_1.insert(afterNode=None, newNode=n1112)
        assert linked_list_insert_1.head.next == n1111
        assert linked_list_insert_1.head.next.next == n1112
        assert linked_list_insert_1.tail.prev == n1112
        assert linked_list_insert_1.tail.prev.prev == n1111

        linked_list_insert_1.insert(afterNode=n1112, newNode=n1113)
        assert linked_list_insert_1.head.next == n1111
        assert linked_list_insert_1.head.next.next == n1112
        assert linked_list_insert_1.tail.prev == n1113
        assert linked_list_insert_1.tail.prev.prev == n1112
        assert linked_list_insert_1.head.next.next.next == n1113
        assert linked_list_insert_1.head.next.next.prev == n1111

    @staticmethod
    def test_len():
        # TEST-1
        linked_list_default_copy = copy.deepcopy(linked_list_default)
        assert linked_list_default_copy.len() == 3
        # TEST-2
        empty_linked_list_copy = copy.deepcopy(empty_linked_list)
        assert empty_linked_list_copy.len() == 0 


def run_tests_TestLinkedListDummy2():
    TestLinkedListDummy2.test_add_in_head()
    TestLinkedListDummy2.test_clean()
    TestLinkedListDummy2.test_delete()
    TestLinkedListDummy2.test_find()
    TestLinkedListDummy2.test_find_all()
    TestLinkedListDummy2.test_insert()
    TestLinkedListDummy2.test_len()
