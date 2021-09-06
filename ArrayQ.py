from array import array


class ArrayQ:

    # "konstruktor" som skapar en tom int-array
    def __init__(self):
        self.Q = array('i', [])

    # stoppa in ett värde sist i kön
    def enqueue(self, array_int):
        self.Q.append(array_int)

    # plocka ut värdet som står först i kön
    def dequeue(self):
        x = self.Q.pop(0)
        return x

    # kolla om kön är tom
    def isEmpty(self):
        if self.dequeue() == -1:
            return True
        else:
            return False

    # returnerar antalet element i kön
    def size(self):
        return len(self.Q)

    def Q(self):
        arraycopy = array('i', [])
        for value in self.Q:
            arraycopy.append(value)
        return arraycopy

    __arrayQ = Q()
