from cards import Deck


class CardGame:

    def __init__(self):
        self.main_deck = Deck()
        self.deck_p1 = []
        self.deck_p2 = []

    def prepare(self):
        self.main_deck.reshuffle()
        self.main_deck.deal(self.deck_p1, self.deck_p2)

    def p1_play_card(self):
        """Get card from top of player 1 deck"""
        return self.deck_p1.pop(0)

    def p2_play_card(self):
        """Get card from top of player 2 deck"""
        return self.deck_p2.pop(0)

    def figure_value(self, card):
        """Get value of card's figure"""
        return self.main_deck.figures[card.split()[0]]
