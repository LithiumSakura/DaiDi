import pydealer
import pydealer.const

deck = pydealer.Deck()
deck.shuffle()

player1 = deck.deal(13)
player2 = deck.deal(13)
player3 = deck.deal(13)
player4 = deck.deal(13)
player1.sort(ranks=pydealer.const.BIG2_RANKS)
player2.sort(ranks=pydealer.const.BIG2_RANKS)
player3.sort(ranks=pydealer.const.BIG2_RANKS)
player4.sort(ranks=pydealer.const.BIG2_RANKS)

print("Player 1 \n", player1)
print("Player 2 \n", player2)
print("Player 3 \n", player3)
print("Player 4 \n", player4)