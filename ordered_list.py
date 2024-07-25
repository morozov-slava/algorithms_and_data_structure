class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        return 0

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item
  
    def add(self, value):
        new_node = Node(value)
        node = self.head
        while node is not None:
            comp_result = self.compare(node.value, new_node.value)
            if ((comp_result == -1) and (self.__ascending is True)) or ((comp_result == 1) and (self.__ascending is False)):
                node = node.next
                continue
            # if add to head
            new_node.next = node
            if node.prev is None:
                new_node.prev = None
                self.head = new_node
            else:
                new_node.prev = node.prev
                node.prev.next = new_node
            node.prev = new_node
            return None
        # if we are on None, than add to head or tail
        self.add_in_tail(new_node)

    def find(self, val):
        node = self.head
        while node is not None:
            comp_result = self.compare(node.value, val)
            if ((comp_result == 1) and (self.__ascending is True)) or ((comp_result == -1) and (self.__ascending is False)):
                break
            if comp_result == 0:
                return node
            node = node.next 

    def delete(self, val):
        node = self.head
        while node is not None:
            if node.value != val:
                node = node.next
                continue
            prev_node = node.prev
            next_node = node.next
            if (prev_node is None) and (next_node is None):
                # for single node in linked list2
                self.head = None
                self.tail = None
            elif (prev_node is not None) and (next_node is None):
                # for tail node
                prev_node.next = None
                self.tail = prev_node
            elif (prev_node is None) and (next_node is not None):
                # for head node
                next_node.prev = None
                self.head = next_node
            elif (prev_node is not None) and (next_node is not None):
                # for other cases
                prev_node.next = next_node
                next_node.prev = prev_node
            break
            
    def clean(self, asc):
        current_list = self.get_all()
        self.head = None
        self.tail = None
        self.__ascending = asc
        for node in current_list:
            self.add(node.value)

    def len(self):
        node = self.head
        lenght = 0
        while node is not None:
            lenght += 1
            node = node.next
        return lenght

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next 

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1: str, v2: str):
        v1 = v1.lstrip().rstrip()
        v2 = v2.lstrip().rstrip()
        if v1 != v2:
            return 1
        return 0


