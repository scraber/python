from game import CardGame


class Wargame(CardGame):
    cards_on_table = []

    def __init__(self):
        CardGame.__init__(self)
        self.prepare()

    def players_have_cards(self):
        if 0 != len(self.deck_p1) and 0 != len(self.deck_p2):
            return True
        else:
            return False

    def trophy_on_table(self):
        if 0 != len(self.cards_on_table):
            return True
        else:
            return False

    def higher_card_wins(self, deck1, deck2, card1, card2):
        if self.figure_value(card1) > self.figure_value(card2):
            deck1.append(card1)
            deck1.append(card2)
            if self.trophy_on_table():
                deck1 += self.cards_on_table
                self.cards_on_table.clear()
        else:
            deck2.append(card1)
            deck2.append(card2)
            if self.trophy_on_table():
                deck2 += self.cards_on_table
                self.cards_on_table.clear()

    def draw(self, card1, card2):
        self.cards_on_table.append(card1)
        self.cards_on_table.append(card2)

    def play(self):
        while self.players_have_cards():
            p1_card = self.p1_play_card()
            p2_card = self.p2_play_card()

            if self.figure_value(p1_card) == self.figure_value(p2_card):
                self.draw(p1_card, p2_card)
            else:
                self.higher_card_wins(self.deck_p1, self.deck_p2, p1_card, p2_card)
        print("P1 won" if 0 == len(self.deck_p2) else "P2 won")


dupa = Wargame()
dupa.play()
