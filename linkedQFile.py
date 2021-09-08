class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQ:
    def __init__(self):
        self._first: Node() = None
        self._last = None
        self._size = 0

    def enqueue(self, newNodeValue):
        if self._first is None:
            self._first = Node(newNodeValue)
            self._last = self._first
        else:
            p = self._first
            while p.next is not None:
                p = p.next
            p.next = Node(newNodeValue)
            self._last = p.next
        self._size += 1

    def dequeue(self):
        p = self._first
        self._first = p.next
        self._size -= 1
        return p.value

    def __str__(self):
        temp = "The Linked List is: ["
        p = self._first

        while p.next is not None:
            temp += str(p.value) + ", "
            p = p.next

        temp = temp + str(p.value) + "]"
        return temp

    def size(self):
        return self._size

    def isEmpty(self):
        if self._first is None:
            return True
        else:
            return False


