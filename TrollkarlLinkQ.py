from linkedQFile import LinkedQ


class Trollkarl:

    def __init__(self):
        self.card_numbers = LinkedQ()

    def input_numbers(self):
        datarad = input("Vilken ordning ligger korten i? ")
        uppdelad = datarad.split(" ")
        for item in uppdelad:
            self.card_numbers.enqueue(item)

    def korttrick(self):
        self.input_numbers()
        print_cards = LinkedQ()

        while not self.card_numbers.isEmpty():
            x = self.card_numbers.dequeue()
            self.card_numbers.enqueue(x)
            print_cards.enqueue(self.card_numbers.dequeue())

        print(print_cards.__str__())


def main():
    t = Trollkarl()
    t.korttrick()


main()
