class Card:
    SUITS = 'SHDC'
    RANKS = '__23456789JQKA'
    
    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank
        self.image = pygame.image.load(f"images/{rank}.png")
        
    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
    
    def __repr__(self):
        return self.rank + self.suit
    
    def worth(self):
        return Card.RANKS.index(self.rank)

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS[2:]]
    
    def withdraw(self, card):
        self.cards.remove(card)
        return card
    
    def withdraw_all(self, suit):
        to_withdraw = [card for card in self.cards if card.suit == suit]
        for card in to_withdraw:
            self.withdraw(card)
        return to_withdraw

class Hand:
    def __init__(self, cards):
        self.cards = cards
    
    def withdraw(self, card):
        self.cards.remove(card)
        return card
    
    def shuffle(self):
        random.shuffle(self.cards)
    
class Player:
    def __init__(self, suit, hand):
        self.suit = suit
        self.score = 0
        self.hand = hand
        self.current_bet = None
        self.elapsed_bets = []
        
    def bet(self, card):
        self.current_bet = self.hand.withdraw(card)
        self.elapsed_bets.append(self.current_bet)
        
    def __eq__(self, other):
        return self.suit == other.suit
    
    def __hash__(self):
        return hash(self.suit)
    
    def __repr__(self):
        return f'Suit:{self.suit}, score: {self.score}, elapsed bets:{self.elapsed_bets}'

class Human(Player):
    def decide(self, prize, elapsed_prizes, elapsed_bets):
        print(f'''Player of suit {self.suit}:''')
        print(f'''Your elapsed bets are: {self.elapsed_bets}''')
        print(f'''Just enter the rank you want to bet 23456789TJQKA''')
        choice = input()
        return Card(self.suit, choice)

class RandomComputer(Player):
    def decide(self, prize, elapsed_prizes, elapsed_bets):
        return random.choice(self.hand.cards)

# Run the game
d = Diamonds_Game()
d.main()
