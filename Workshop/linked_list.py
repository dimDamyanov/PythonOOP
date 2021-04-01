class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.values_count = 0

    def append(self, value):
        node = LinkedListNode(value)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node

        self.values_count += 1

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
