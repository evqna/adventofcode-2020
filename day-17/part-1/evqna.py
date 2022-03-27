from tool.runners.python import SubmissionPy

class Simulation:
    def __init__(self, initial_state):
        self.state = initial_state
    
    def neighbors(self, i, j, k):
        deltas = (-1, 0, 1)
        N = {(i + u, j + v, k + w) for u in deltas for v in deltas for w in deltas}
        N.remove((i, j, k))
        return N
    
    def count_active_neighbors(self, i, j, k):
        return len(self.neighbors(i, j, k).intersection(self.state))
    
    def step(self):
        next_state = set()
        activation_zone = set()
        for i, j, k in self.state:
            active_neighbors = 0
            for n in self.neighbors(i, j, k):
                if n in self.state:
                    active_neighbors += 1
                else:
                    activation_zone.add(n)
            if active_neighbors == 2 or active_neighbors == 3:
                next_state.add((i, j, k))
        for i, j, k in activation_zone:
            if self.count_active_neighbors(i, j, k) == 3:
                next_state.add((i, j, k))
        self.state = next_state

class EvqnaSubmission(SubmissionPy):

    def run(self, s):
        active_cells = set()
        for i, row in enumerate(s.splitlines()):
            for j, cell in enumerate(row):
                if cell == '#':
                    active_cells.add((i, j, 0))
        
        S = Simulation(active_cells)
        for _ in range(6):
            S.step()
        return len(S.state)
