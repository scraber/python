from random import shuffle


class Deck:
    suits = ("spades", "hearts", "diamonds", "clubs")
    figures = {"ace": 14, "king": 13, "queen": 12, "jack": 11, "ten": 10, "nine": 9}

    deck = []

    def __init__(self):
        for i in self.figures:
            for j in self.suits:
                self.deck.append(i + " of " + j)

    def reshuffle(self):
        shuffle(self.deck)

    def deal(self, deck1, deck2):
        for i in range(len(self.deck)):
            if i % 2 == 0:
                deck1.append(self.deck.pop())
            else:
                deck2.append(self.deck.pop())
