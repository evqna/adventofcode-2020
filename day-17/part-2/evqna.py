from tool.runners.python import SubmissionPy

from collections import defaultdict
from itertools import product
    
def neighbors(pos):
    x, y, z, w = pos
    deltas = (-1, 0, +1)
    N = [(x + i, y + j, z + k, w + l) for i, j, k, l in product(deltas, repeat=4)]
    N.remove(pos)
    return N

class Simulation:
    def __init__(self, initial_state):
        self.state = initial_state
        self.frontier_active_neighbors = defaultdict(int)   # {pos: count}
    
    def step(self):
        next_state = set()

        for cube in self.state:
            active_neighbors = 0
            for n in neighbors(cube):
                if n in self.state:
                    active_neighbors += 1
                else:
                    self.frontier_active_neighbors[n] += 1
            if active_neighbors == 2 or active_neighbors == 3:
                next_state.add(cube)
        for pos in self.frontier_active_neighbors:
            if self.frontier_active_neighbors[pos] == 3:
                next_state.add(pos)

        self.state = next_state
        self.frontier_active_neighbors.clear()

class EvqnaSubmission(SubmissionPy):

    def run(self, s):
        active_cells = set()
        for i, row in enumerate(s.splitlines()):
            for j, cell in enumerate(row):
                if cell == '#':
                    active_cells.add((i, j, 0, 0))
        
        S = Simulation(active_cells)
        for _ in range(6):
            S.step()
        return len(S.state)
