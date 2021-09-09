class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQ:
    def __init__(self):
        self._first = None
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

    def size(self):
        if self._first is None:
            return 0
        else:
            p = self._first
            count = 1
            while p.next is not None:
                count += 1
                p = p.next
            return count

    def isEmpty(self):
        if self._first is None:
            return True
        else:
            return False

    # söka efter x och ta bort den från linked lista
    def remove(self, x):
        p = self._first
        # här kollar man om first node är den node som man söka efter
        if x == p.value:
            self._first = p.next
            self._size -= 1
        else:
            # här kollar vi om det är sista noden som vi letar efter
            if x is self._last.value:
                while p.next is not self._last:
                    p = p.next
                p.next = None
                self._last = p
                self._size -= 1
                # annars kollar man om x finns i andra noder
            else:
                while p.next is not None:
                    if x == p.next.value:
                        p.next = p.next.next
                        self._size -= 1
                    p = p.next

    def __str__(self):
        p = self._first

        while p.next is not None:
            temp += p.value + " "
            p = p.next
        temp = temp + p.value
        return temp