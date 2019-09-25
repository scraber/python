from cards import deck, figures
from random import shuffle

shuffle(deck)

deck_p1 = []
deck_p2 = []
war_trophy = []

# Split deck between two players
for i in range(len(deck)):
    if i % 2 == 0:
        deck_p1.append(deck.pop())
    else:
        deck_p2.append(deck.pop())

while True:
    print("deck 1:", len(deck_p1))
    print("deck 2:", len(deck_p2))
    # Get a card
    if 0 == len(deck_p1) or 0 == len(deck_p2):
        break
    p1_card = deck_p1.pop(0)
    p2_card = deck_p2.pop(0)

    if figures[p1_card.split()[0]] > figures[p2_card.split()[0]]:
        deck_p1.append(p1_card)
        deck_p1.append(p2_card)
        if 0 != len(war_trophy):
            deck_p1 += war_trophy
            war_trophy.clear()
    elif figures[p1_card.split()[0]] == figures[p2_card.split()[0]]:
        war_trophy.append(p1_card)
        war_trophy.append(p2_card)
    else:
        deck_p2.append(p1_card)
        deck_p2.append(p2_card)
        if 0 != len(war_trophy):
            deck_p2 += war_trophy
            war_trophy.clear()

print("P1 won" if 0 == len(deck_p2) else "P2 won")
