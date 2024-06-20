import random
class Deck:
    def __init__(self):
        self.deck = []
        suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10}
        ]

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        if len(self.deck) > 1:
            random.shuffle(self.deck)

    def deal(self, num):
        cards_dealt = []
        for x in range(num):
            if num > 0:
                card = self.deck.pop()
                cards_dealt.append(card)
        return cards_dealt
    
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

class Hand:
    def __init__(self, dealer = False):
        self.cards = []
        self.value = 0
        self.dealer = dealer
    
    def add_card(self, card_list):
        self.cards.extend(card_list)
    
    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            card_value = int(card.rank['value'])
            self.value += card_value
            if card.rank['rank'] == "A":
                has_ace = True
        if has_ace and self.value > 21:
            self.value -= 10
    
    def get_value(self):
        self.calculate_value()
        return self.value
    
    def is_blackjack(self):
        return self.get_value() == 21
    
    def display(self):
        print(f'''{} hand:''')

deck = Deck()
deck.shuffle()

hand = Hand()

hand.add_card(deck.deal(2))

print(hand.cards[0], hand.cards[1])
