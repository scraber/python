from random import shuffle


class Deck:
    figures = {"ace": 14, "king": 13, "queen": 12, "jack": 11, "ten": 10, "nine": 9}

    def __init__(self, suits=("spades", "hearts", "diamonds", "clubs")):
        self.deck = []
        for i in self.figures:
            for j in suits:
                self.deck.append(i + " of " + j)

    def reshuffle(self):
        """Shuffles common deck"""
        shuffle(self.deck)

    def deal(self, deck1, deck2):
        """Deals the cards between two players"""
        for i in range(len(self.deck)):
            if i % 2 == 0:
                deck1.append(self.deck.pop())
            else:
                deck2.append(self.deck.pop())
