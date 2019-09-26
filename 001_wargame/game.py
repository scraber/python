from cards import Deck


class CardGame:
    main_deck = Deck()
    deck_p1 = []
    deck_p2 = []

    def prepare(self):
        self.main_deck.reshuffle()
        self.main_deck.deal(self.deck_p1, self.deck_p2)

    def p1_play_card(self):
        return self.deck_p1.pop(0)

    def p2_play_card(self):
        return self.deck_p2.pop(0)

    def figure_value(self, card):
        return self.main_deck.figures[card.split()[0]]