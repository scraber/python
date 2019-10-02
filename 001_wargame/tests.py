from cards import Deck
from game import CardGame
from wargame import Wargame
import unittest


class TestDeck(unittest.TestCase):
    def setUp(self) -> None:
        self.test_deck = Deck()

    def test_reshuffle(self):
        deck_to_reshuffle = tuple(self.test_deck.deck)
        self.assertEqual(len(self.test_deck.deck), 24)
        self.test_deck.reshuffle()
        self.assertEqual(len(self.test_deck.deck), 24)
        self.assertNotEqual(self.test_deck.deck, deck_to_reshuffle)

    def test_deal(self):
        test_deck_p1 = []
        test_deck_p2 = []
        self.assertEqual(len(self.test_deck.deck), 24)
        self.assertEqual(len(test_deck_p1), 0)
        self.assertEqual(len(test_deck_p2), 0)
        self.test_deck.deal(test_deck_p1, test_deck_p2)
        self.assertEqual(len(self.test_deck.deck), 0)
        self.assertEqual(len(test_deck_p1), 12)
        self.assertEqual(len(test_deck_p2), 12)


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self.test_game = CardGame()

    def test_play_cards(self):
        self.test_game.prepare()
        self.assertEqual(len(self.test_game.deck_p1), 12)
        self.assertEqual(len(self.test_game.deck_p2), 12)
        self.test_game.p1_play_card()
        self.assertEqual(len(self.test_game.deck_p1), 11)
        self.test_game.p2_play_card()
        self.test_game.p2_play_card()
        self.assertEqual(len(self.test_game.deck_p2), 10)

    def test_figure_value(self):
        self.assertEqual(self.test_game.figure_value("ace"), self.test_game.main_deck.figures["ace"])
        self.assertEqual(self.test_game.figure_value("jack"), 11)

    def tearDown(self) -> None:
        del self.test_game


class TestWargame(unittest.TestCase):
    def setUp(self) -> None:
        self.test_wargame = Wargame()

    def test_higher_card_wins(self):
        len_of_p1_deck = len(self.test_wargame.deck_p1)
        len_of_p2_deck = len(self.test_wargame.deck_p2)
        self.test_wargame.higher_card_wins("ace of spades", "king of spades")
        self.assertEqual(len(self.test_wargame.deck_p1), len_of_p1_deck + 2)
        self.test_wargame.higher_card_wins("nine", "king")
        self.assertEqual(len(self.test_wargame.deck_p2), len_of_p2_deck + 2)

    def test_draw_and_trophy_on_table(self):
        self.assertEqual(len(self.test_wargame.cards_on_table), 0)
        self.test_wargame.draw("ace of spades", "ace of hearts")
        self.assertEqual(len(self.test_wargame.cards_on_table), 2)
        self.test_wargame.draw("jack of spades", "jack of hearts")
        self.assertEqual(len(self.test_wargame.cards_on_table), 4)
        self.test_wargame.higher_card_wins("ace of spades", "king of spades")
        self.assertEqual(len(self.test_wargame.cards_on_table), 0)

    def test_players_have_cards(self):
        self.assertEqual(self.test_wargame.players_have_cards(), True)
        self.test_wargame.deck_p1.clear()
        self.assertEqual(self.test_wargame.players_have_cards(), False)

    def tearDown(self) -> None:
        del self.test_wargame


if __name__ == '__main__':
    unittest.main()
