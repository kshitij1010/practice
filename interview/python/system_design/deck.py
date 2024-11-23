# simple deck of cards
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def show(self):
        print (str(self.rank) + " of " + str(self.suit))

class Deck:
    def __init__(self):
        self.deck = []
        self.build()

    def build(self):
        for suit in ["Hearts", "Spades", "Diamonds", "Clubs"]:
            for rank in range(1,14):
                if rank == 1:
                    self.deck.append(Card(suit, "Ace"))
                elif rank == 11:
                    self.deck.append(Card(suit, "Jack"))
                elif rank == 12:
                    self.deck.append(Card(suit, "Queen"))
                elif rank == 13:
                    self.deck.append(Card(suit, "King"))
                else:
                    self.deck.append(Card(suit, rank))
        return

    def show_all(self):
        for i in range(len(self.deck)):
            print (str(self.deck[i].rank) + " of " + str(self.deck[i].suit))
        return

    def shuffle(self):
        for i in range(len(self.deck)):
            r = random.randint(i, len(self.deck)-1)
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]
        return

    def draw_card(self):
        self.shuffle()
        return self.deck.pop()

class Player:
    def __init__(self, name=None):
        self.name = name
        self.hand = []

    def draw(self, deck, num=1):
        for i in range(num):
            self.hand.append(deck.draw_card())
        return

    def show_hand(self):
        for i in range(len(self.hand)):
            print (str(self.hand[i].rank) + " of " + str(self.hand[i].suit))
        return

d = Deck()
# d.show_all()
# d.shuffle()
# d.show_all()

# c1 = d.draw().show()
# c2 = d.draw().show()
# c3 = d.draw().show()
# c4 = d.draw().show()

p = Player()
p.draw(d, 5)
p.show_hand()
