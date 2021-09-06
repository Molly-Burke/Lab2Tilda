from array import array


class Trollkarl:

    def __init__(self):
        self.uppdelad = array('i', [])

    def input_numbers(self):
        datarad = input("Vilken ordning ligger korten i? ")
        uppdelad = datarad.split(" ")
        array_of_numbers = array('i', [])
        for item in uppdelad:
            num = float(item)
            array_of_numbers.append(int(round(num)))

        return array_of_numbers

    def korttrick(self):
        array = self.input_numbers()
        print(array.tolist())

        outarray = []
        while len(array) > 0:
            x = array.pop()
            array.append(x)
            outarray.append(array.pop())

        print(outarray.__str__())


def main():
    t = Trollkarl()
    t.korttrick()


main()
