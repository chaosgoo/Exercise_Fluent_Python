import collections 
Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    clubs = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._card[position]

    def __setitem__(self, position, value):
        self._card[position] = value

    def __delitem__(self, position):
        del self._card[position]

    def insert(self, position, value):
        self._cards.insert(position, value)