from tool.runners.python import SubmissionPy

from collections import deque

class Game:
    def __init__(self, cups) -> None:
        self.cups = deque(cups, len(cups))

    def pickup_cups(self, i, n):
        self.cups.rotate(-i)
        cups = [self.cups.popleft() for _ in range(n)]
        self.cups.rotate(+i)
        return cups

    def place_cups(self, cups, i):
        self.cups.rotate(-i)
        self.cups.extend(cups)
        self.cups.rotate(+i + len(cups))
 
    def get_destination(self, current, pickup):
        destination = current - 1
        while destination < 1 or destination in pickup:
            if destination < 1:
                destination = 9
            else:
                destination -= 1
        return destination
   
    def move(self):
        # The current cup is always at index 0 on round start.
        current = self.cups[0]
        pickup = self.pickup_cups(i=1, n=3)
        i_dest = self.cups.index(self.get_destination(current, pickup))
        self.place_cups(pickup, i_dest + 1)
        # Rotate clockwise to select next cup
        self.cups.rotate(-1)
    
    def format_state(self):
        pos_1 = self.cups.index(1)
        self.cups.rotate(-pos_1)
        s = ''.join(str(c) for c in self.cups)
        self.cups.rotate(+pos_1)
        return s[1:]


class EvqnaSubmission(SubmissionPy):
    def run(self, s):
        cups = [int(c) for c in s.strip()]
        game = Game(cups)

        for _ in range(100):
            game.move()
        return game.format_state()
