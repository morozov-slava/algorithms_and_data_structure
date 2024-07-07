class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
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
        prev_node = None
        node = self.head
        while node is not None:
            if node.value == val:
                next_node = node.next
                # delete node
                if (prev_node is None) and (next_node is None):
                    self.head = None
                elif (prev_node is None) and (next_node is not None):
                    self.head = next_node
                else:
                    prev_node.next = next_node
                if not all:
                    break    
            else:
                prev_node = node
            node = node.next
                
    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        lenght = 0
        while node != None:
            lenght += 1
            node = node.next
        return lenght

    def insert(self, afterNode, newNode):
        if afterNode is None:
            initial_head_node = self.head
            self.head = newNode
            self.head.next = initial_head_node
        else:
            current_next_node = afterNode.next
            afterNode.next = newNode
            newNode.next = current_next_node

    def get_node_by_index(self, i):
        node = self.head
        searched_node = None 
        counter = 0
        while node != None:
            if counter == i:
                searched_node = node
                break
            else:
                node = node.next
                counter += 1
        return searched_node


def sum_two_linked_lists_vectors(LL1, LL2):
    result = []
    if LL1.len() == LL2.len():
        for i in range(LL1.len()):
            node1 = LL1.get_node_by_index(i)
            node2 = LL2.get_node_by_index(i)
            result.append(node1.value + node2.value)
        return result
