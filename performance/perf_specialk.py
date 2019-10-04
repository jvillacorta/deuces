from __future__ import print_function
import time
from deuces import Deck, Evaluator


def setup(n, m):
    _hands = []
    _boards = []

    for i in range(n):

        deck = Deck()
        hand = []
        board = []
        for j in range(2):
            hand.append(deck.draw())
        for j in range(m):
            board.append(deck.draw())

        _hands.append(hand)
        _boards.append(board)

    return _boards, _hands


for M in (3, 4, 5):
    N = 10000
    cumulative_time = 0.0
    evaluator = Evaluator()
    boards, hands = setup(N, M)
    for i in range(len(boards)):
        start = time.time()
        evaluator.evaluate(hands[i], boards[i])
        cumulative_time += (time.time() - start)

    avg = float(cumulative_time / N)
    print("%i card evaluation:" % M)
    print("[*] Pokerhand-eval: Average time per evaluation: %f" % avg)
    print("[*] Pokerhand-eval: Evaluations per second = %f" % (1.0 / avg))
