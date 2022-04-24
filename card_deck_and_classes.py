import random
import time
class Card():
        def __init__(self, value, suit):
                self.value = value
                self.suit = suit
                self.points =points

        def showcard(self):
                print(f"{self.value} of {self.suit}.")
                

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
                        Card.showcard(card)

        def getvalueofcard(self):



        def shuffledeck(self):
                for i in range(len(self.deck)-1,0,-1):
                        r = random.randint(0,i)
                        self.deck[i], self.deck[r] = self.deck[r], self.deck[i]

        def drawcard(self):
                card = self.deck.pop()
                return card


class Player():
        def __init__(self,name):
                self.name=name
                self.heldcards = []

        def showplayershand(self):
                for card in self.heldcards:
                        Card.showcard(card)
                        

        def takecard(self,deck,amount):
                for x in range(amount):
                        self.heldcards.append(deck.drawcard())



##Tests to make sure classes work~
print("====Blackjack=====")
name = input("Please enter your name > ")
player = Player(name)
print(f"Okay {name} here are you first two cards")
deck1 = Deck()
deck1.build()
player.takecard(deck1,2)
cpu = Player("cpu")
cpu.takecard(deck1,2)
print(f"Dealer takes two cards.")
time.sleep(1.5)
print("Okay, here are your first two cards:")
time.sleep(1.5)
player.showplayershand()
choice = input("What would you like to do? [hit], [stick] > ")
if choice == 'hit':
        player.takecard(deck1,1)
        print("Your cards are now:")
        player.showplayershand()


