from tool.runners.python import SubmissionPy

from collections import defaultdict
from math import prod


class Tile:
    def __init__(self, id, bitmap):
        self.id = id
        self.bitmap = bitmap

        self.S = self.sides(bitmap)
        self.T = self.sides(list(reversed(bitmap)))

    def sides(self, bitmap):
        top = list(bitmap[0])
        right = [row[-1] for row in bitmap]
        bot = list(reversed(bitmap[-1]))
        left = [row[0] for row in reversed(bitmap)]
        return tuple(self.to_int(S) for S in (top, right, bot, left))

    def to_int(self, bits):
        s = ''.join(bits).replace('#', '1').replace('.', '0')
        return int(s, base=2)


class EvqnaSubmission(SubmissionPy):
    def parse_tiles(self, input):
        tiles = []
        for tile in input.split('\n\n'):
            _, id, *bitmap = tile.split()
            id = int(id[:-1])
            tiles.append(Tile(id, bitmap))
        return tiles

    def build_lookup(self, tiles):
        lookup = defaultdict(list)
        for tile in tiles:
            for side in tile.S:
                lookup[side].append(tile.id)
            for side in tile.T:
                lookup[side].append(tile.id)
        return lookup

    def find_corner_tiles(self, tiles, edge_lookup):
        corner_tiles = []
        for tile in tiles:
            # Tiles that do not admit more than two neighbors on either side must be in a corner
            A = [edge for edge in tile.S if len(edge_lookup[edge]) == 1]
            B = [edge for edge in tile.T if len(edge_lookup[edge]) == 1]
            if len(A) >= 2 and len(B) >= 2:
                corner_tiles.append(tile.id)
        return corner_tiles

    def run(self, input):
        tiles = self.parse_tiles(input)
        edge_lookup = self.build_lookup(tiles)

        corner_tiles = self.find_corner_tiles(tiles, edge_lookup)
        return prod(corner_tiles)
