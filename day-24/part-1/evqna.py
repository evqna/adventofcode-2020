from tool.runners.python import SubmissionPy


class EvqnaSubmission(SubmissionPy):
    def flip(self, tile):
        if tile in self.black_tiles:
            self.black_tiles.remove(tile)
        else:
            self.black_tiles.add(tile)
    
    def get_coordinates(self, tile):
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

    def run(self, s):
        self.black_tiles = set()
        for tile in s.splitlines():
            coord = self.get_coordinates(tile)
            self.flip(coord)

        return len(self.black_tiles)
