import random
class Card():
        def __init__(self, value, suit):
                self.value = value
                self.suit = suit

        def showcard(self):
                output = f"{self.value} of {self.suit}."
                return output

class Deck():
        def __init__(self):
                self.deck = []
        def build(self):
                value= ["A","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
                suit = ["Hearts","Diamonds","Spades","Clubs"]
                for v in value:
                        for s in suit:
                                self.deck.append(Card(v,s))
        def showdeck(self):
                for card in self.deck:
                        print(Card.showcard(card))


deck1 = Deck()
deck1.build()
deck1.showdeck()


