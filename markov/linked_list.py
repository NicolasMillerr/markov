"""
Linked list implementation
"""


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value
        else:
            return self.value == other


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_head(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.length += 1

    def __getitem__(self, index: int) -> Node:
        current = self.head

        for i in range(index):
            current = current.next_node
        return current

    def __str__(self):
        current = self.head
        acc = []
        while current:
            acc.append(str(current.value))
            current = current.next_node
        return "->".join(acc)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self.length

    def insert_at_key(self, key, value):
        prev = self.__getitem__(key - 1)
        curr = self.__getitem__(key)
        new = Node(value, curr)
        prev.next_node = new
        self.length += 1

    def __setitem__(self, key, value):
        if key >= self.length:
            raise IndexError("Cant assign to value out of range")
        prev = self.__getitem__(key - 1)
        new_next = self.__getitem__(key).next_node
        new = Node(value, new_next)
        prev.next_node = new

    @classmethod
    def linked_list_from_list(cls, list_input: list):
        ll = LinkedList()
        for i in reversed(list_input):
            ll.insert_at_head(i)

        return ll
