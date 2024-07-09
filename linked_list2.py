class Node:
    
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2: 
    
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            else:
                node = node.next
        return None

    def find_all(self, val):
        nodes = []
        node = self.head
        while node is not None:
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
                else:
                    # for other cases
                    prev_node.next = next_node
                    next_node.prev = prev_node
                if not all:
                    break
            
    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        lenght = 0
        while node is not None:
            lenght += 1
            node = node.next
        return lenght

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)
        else:
            prev_node = afterNode.prev
            next_node = afterNode.next
            if (prev_node is None) and (next_node is None):
                # for single node in linked list2
                self.add_in_tail(newNode)
            elif (prev_node is not None) and (next_node is None):
                # for tail node
                newNode.next = None
                newNode.prev = afterNode
                afterNode.next = newNode
                self.tail = newNode
            else:
                next_node.prev = newNode
                newNode.next = next_node
                afterNode.next = newNode
                newNode.prev = afterNode
                   
    def add_in_head(self, newNode):
        initial_head = self.head
        if initial_head is None:
            # for empty linked list 2
            self.add_in_tail(newNode)
        else:
            newNode.next = initial_head
            initial_head.prev = newNode
            self.head = newNode

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next


