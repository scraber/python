from game import CardGame


class Wargame(CardGame):
    def __init__(self):
        self.cards_on_table = []
        CardGame.__init__(self)
        self.prepare()

    def players_have_cards(self):
        """Check if both players still have cards"""
        if 0 != len(self.deck_p1) and 0 != len(self.deck_p2):
            return True
        else:
            return False

    def trophy_on_table(self):
        """Check if there is trophy from previous draw"""
        if 0 != len(self.cards_on_table):
            return True
        else:
            return False

    def higher_card_wins(self, card1, card2):
        if self.figure_value(card1) > self.figure_value(card2):
            self.deck_p1.extend((card1, card2))
            if self.trophy_on_table():
                self.deck_p1 += self.cards_on_table
                self.cards_on_table.clear()
        else:
            self.deck_p2.extend((card1, card2))
            if self.trophy_on_table():
                self.deck_p2 += self.cards_on_table
                self.cards_on_table.clear()

    def draw(self, card1, card2):
        """Draw scenario, add both cards to stack on table"""
        self.cards_on_table.append(card1)
        self.cards_on_table.append(card2)

    def next(self):
        """Get card from both players and execute action depending on figure's value"""
        p1_card = self.p1_play_card()
        p2_card = self.p2_play_card()

        if self.figure_value(p1_card) == self.figure_value(p2_card):
            self.draw(p1_card, p2_card)
        else:
            self.higher_card_wins(p1_card, p2_card)

    def play(self):
        """Play until one of the players run out of cards"""
        while self.players_have_cards():
            self.next()
        print("P1 won" if 0 == len(self.deck_p2) else "P2 won")
