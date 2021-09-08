from array import array

class ArrayQ:


    def __init__(self):
        self._newq = array('i',[])

    # stoppa in ett värde sist i kön
    def enqueue(self, array_int):
        self._newq.append(array_int)

    # plocka ut värdet som står först i kön
    def dequeue(self):
        x = self._newq.pop(0)
        return x

    # kolla om kön är tom
    def isEmpty(self):
        if len(self._newq) == 0:
            return True
        else:
            return False

    # returnerar antalet element i kön
    def size(self):
        return len(self._newq)

    # ta bort x från array
    def remove(self,x):
        self._newq.remove(x)
