from tool.runners.python import SubmissionPy

from collections import deque

class EvqnaSubmission(SubmissionPy):
    def score(self, deck):
        return sum([(i + 1) * n for i, n in enumerate(reversed(deck))])

    def run(self, s):
        player1, player2 = s.split('\n\n')
        P1 = deque([int(c) for c in player1.splitlines()[1:]])
        P2 = deque([int(c) for c in player2.splitlines()[1:]])

        while len(P1) > 0 and len(P2) > 0:
            c1, c2 = P1.popleft(), P2.popleft()
            if c1 > c2:
                P1.extend((c1, c2))
            else:
                P2.extend((c2, c1))

        return self.score(P1) + self.score(P2)
