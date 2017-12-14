from random import shuffle
import collections
Card = collections.namedtuple("Card",["rank", "suit"])
class FranchDeck:
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    suits = "spades diamonds clubs herats".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, card):
        self._cards[position] = card
l = list(range(10))
shuffle(l)
print(l)
deck = FranchDeck()
shuffle(deck)
print(deck[:5])
