class DummyNode():
    def __init__(self):
        self.prev = None
        self.next = None


class Node(DummyNode):
    def __init__(self, v):
        super().__init__()
        self.value = v
        

class LinkedList2Dummy:

    def __init__(self):
        self.head = DummyNode()
        self.tail = DummyNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add_in_tail(self, item):
        if self.head.next is None:
            self.head.next = item
            self.tail.prev = item
            item.prev = self.head
            item.next = self.tail
        else:
            prev_node = self.tail.prev
            prev_node.next = item
            item.prev = prev_node
            item.next = self.tail
            self.tail.prev = item

    def find(self, val):
        node = self.head.next
        while node is not self.tail:
            if node.value == val:
                return node
            else:
                node = node.next
        return None

    def find_all(self, val):
        nodes = []
        node = self.head.next
        while node is not self.tail:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def delete(self, val, all=False):
        while True:
            node = self.find(val)
            if node is None:
                break
            else:
                prev_node = node.prev
                next_node = node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                if not all:
                    break
            
    def clean(self):
        self.head.next = None
        self.tail.prev = None

    def len(self):
        node = self.head.next
        lenght = 0
        while node is not self.tail:
            lenght += 1
            node = node.next
        return lenght

    def insert(self, afterNode, newNode):
        if (afterNode is None) or (self.find(afterNode) is None):
            self.add_in_tail(newNode)
        else:
            prev_node = afterNode.prev
            next_node = afterNode.next
            next_node.prev = newNode
            newNode.next = next_node
            afterNode.next = newNode
            newNode.prev = afterNode
                   
    def add_in_head(self, newNode):
        initial_head = self.head.next
        if initial_head is None:
            # for empty linked list 2
            self.add_in_tail(newNode)
        else:
            newNode.next = initial_head
            initial_head.prev = newNode
            self.head.next = newNode

    def print_all_nodes(self):
        node = self.head.next
        while node is not self.tail:
            print(node.value)
            node = node.next



