from linkedQFile import LinkedQ


class Trollkarl:

    def __init__(self):
        self.card_numbers = LinkedQ()

    def input_numbers(self):
        datarad = input("Vilken ordning ligger korten i? ")
        uppdelad = datarad.split(" ")
        for item in uppdelad:
            num = float(item)
            self.card_numbers.enqueue(int(round(num)))

    def korttrick(self):
        self.input_numbers()
        outarray = []
        while not self.card_numbers.isEmpty():
            x = self.card_numbers.dequeue()
            self.card_numbers.enqueue(x)
            outarray.append(self.card_numbers.dequeue())

        print(outarray.__str__())


def main():
    t = Trollkarl()
    t.korttrick()


main()
