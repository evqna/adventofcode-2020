from tool.runners.python import SubmissionPy

from collections import deque

class EvqnaSubmission(SubmissionPy):
    def score(self, deck):
        return sum([(i + 1) * n for i, n in enumerate(reversed(deck))])
    
    def play_game(self, deck1, deck2):
        seen_states = set()

        while len(deck1) > 0 and len(deck2) > 0:
            state = (tuple(deck1), tuple(deck2))
            if state in seen_states:
                return 1
            seen_states.add(state)

            c1, c2 = deck1.popleft(), deck2.popleft()
            if c1 <= len(deck1) and c2 <= len(deck2):
                # Play a recursive sub-game
                winner = self.play_game(deque(list(deck1)[:c1]), deque(list(deck2)[:c2]))
            else:
                winner = 1 if c1 > c2 else 2
            
            if winner == 1:
                deck1.extend((c1, c2))
            else:
                deck2.extend((c2, c1))
        
        return 1 if len(deck2) == 0 else 2

    def run(self, s):
        player1, player2 = s.split('\n\n')
        P1 = deque([int(c) for c in player1.splitlines()[1:]])
        P2 = deque([int(c) for c in player2.splitlines()[1:]])

        self.play_game(P1, P2)

        return self.score(P1) + self.score(P2)

def test_evqna():
    """
    Run `python -m pytest ./day-22/part-2/evqna.py` to test the submission.
    """
    assert (
        EvqnaSubmission().run(
            """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
""".strip()
        )
        == 291
    )
