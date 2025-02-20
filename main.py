import pydealer as pd

class BigTwo:
    def __init__(self, num_players=4):
        self.num_players = num_players
        self.decl = pd.Deck()
        self.players = [pd.Stack() for _ in range(num_players)]
        self.current_play = pd.Stack()
        self.current_player = 0
        self.pass_count = 0
        self.last_player = -1
    
    def deal_cards(self):
        # Deal 13 cards to each player
        self.deck.shuffle()
        cards_per_player = 13

        for x in range(self.num_players):
            self.players[x].add(self.deck.deal(cards_per_player))
            self.players[x].sort()

    def three_of_diamonds(self) -> int:
        #Find player with 3 or diamonds
        for x, player in enumerate(self.players):
            for card in player:
                if card.value == "3" and card.suit == "Diamonds":
                    return x
        return 0
    
    def card_ranks(self, card1: pd.Card, card2: pd.Card):

        card_ranks = {
            "2" : 13,
            "Ace": 12,
            "King": 11,
            "Queen": 10,
            "Jack": 9,
            "10": 8,
            "9": 7,
            "8": 6,
            "7": 5,
            "6": 4,
            "5": 3,
            "4": 2,
            "3": 1
        }

        suit_order = {
            "Spades": 4,
            "Hearts": 3,
            "Clubs": 2,
            "Diamonds": 1
        }

        hands = {
            "Single",
            "Pair",
            "Three of a Kind",
            "Straight",
            "Flush",
            "Full House",
            "Four of a Kind",
            "Straight Flush"
        }