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
        return self.Q.pop()

    # kolla om kön är tom
    def isEmpty(self):
        if self.dequeue() == -1:
            return True
        else:
            return False

    # returnerar antalet element i kön
    def size(self):
        return len(self.Q)
