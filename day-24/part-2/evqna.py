from tool.runners.python import SubmissionPy

from collections import defaultdict

def neighbors(pos):
    x, y = pos
    return [(x+2, y), (x-2, y), (x+1, y+2), (x-1, y+2), (x+1, y-2), (x-1, y-2)]

class Simulation:
    def __init__(self, initial_state):
        self.black_tiles = initial_state
        self.frontier_active_neighbors = defaultdict(int)   # {pos: count}

    def step(self):
        next_state = set()

        for tile in self.black_tiles:
            black_neighbors = 0
            for n in neighbors(tile):
                if n in self.black_tiles:
                    black_neighbors += 1
                else:
                    self.frontier_active_neighbors[n] += 1
            if black_neighbors == 1 or black_neighbors == 2:
                next_state.add(tile)
        for pos in self.frontier_active_neighbors:
            if self.frontier_active_neighbors[pos] == 2:
                next_state.add(pos)

        self.black_tiles = next_state
        self.frontier_active_neighbors.clear()


class EvqnaSubmission(SubmissionPy):    
    def parse_coordinates(self, tile):
        DELTAS = {'e': (2, 0), 'w': (-2, 0), 'se': (1, 2), 'sw': (-1, 2), \
                  'ne': (1, -2), 'nw': (-1, -2)}
        x, y = 0, 0
        i = 0
        while i < len(tile):
            dir = tile[i]
            if dir == 's' or dir == 'n':
                i += 1
                dir += tile[i]
            dx, dy = DELTAS[dir]
            x, y = x + dx, y + dy
            i += 1
        return x, y

    def flip(self, tile):
        if tile in self.black_tiles:
            self.black_tiles.remove(tile)
        else:
            self.black_tiles.add(tile)

    def run(self, s):
        self.black_tiles = set()
        for tile in s.splitlines():
            coord = self.parse_coordinates(tile)
            self.flip(coord)

        S = Simulation(self.black_tiles)
        for _ in range(100):
            S.step()
        return len(S.black_tiles)
