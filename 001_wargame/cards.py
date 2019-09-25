suits = ("spades", "hearts", "diamonds", "clubs")
figures = {"ace": 14, "king": 13, "queen": 12, "jack": 11, "ten": 10, "nine": 9}

deck = []

for i in figures:
    for j in suits:
        deck.append(i + " of " + j)
