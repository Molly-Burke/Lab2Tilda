class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQ:
    def __init__(self):
        self._first: Node() = None
        self._last : Node() = None
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
        return self._size

    def isEmpty(self):
        if self._first is None:
            return True
        else:
            return False

    #söka efter x och ta bort den från linked lista
    def remove(self, x):
        p = self._first
        # här kollar man om first node är den node som man söka efter
        if x == p.value:
            self._first = p.next
            self._size -= 1
        else:
            # här kollar vi om det är sista noden som vi letar efter
            if x == self._last.value:
                while not p.next == self._last:
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
        temp = "The Linked List is: ["
        p = self._first

        while p.next is not None:
            temp += str(p.value) + ", "
            p = p.next
        temp = temp + str(p.value) + "]"
        return temp

def main():
    q = LinkedQ()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(1)
    q.remove(2)
    print(q)

main()