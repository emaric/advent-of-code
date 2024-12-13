import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from functools import reduce
from itertools import combinations, permutations
from pprint import pprint

from shared.decorators import timer
from shared.helpers import Point, Vectors, get_locations, read_input
from shared.util import (
    extend_list,
    extend_list_2D,
    extend_list_rect,
    ints,
    log,
    logger_config,
    logger_enable,
    logger_init,
    print_array,
    strs,
    wait_for_input,
)

DAY = 8

logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")


example_content = read_input(locations.example_file)
example_cl = example_content.split("\n")
example_cl = example_cl[3:-4]

content = read_input(locations.input_file)
cl = content.split("\n")


class Grid:
    ANTENNA = r"[a-zA-Z0-9]"
    ANTINODE = "#"

    def __init__(self, input):
        self.grid = input
        self.width = len(input[0])
        self.height = len(input)
        self.antennas = defaultdict(set)
        for y, line in enumerate(input):
            for x, point in enumerate(line):
                if re.match(self.ANTENNA, point):
                    self.antennas[point].add(Point(x, y))

        self.antinodes = set()
        self.resonant_antinodes = set()

    def _is_in_range(self, point: Point) -> bool:
        if 0 <= point.x < self.width and 0 <= point.y < self.height:
            return True
        return False

    def antinode_unique_locations(self):
        for _, antennas in self.antennas.items():
            for a1, a2 in list(combinations(antennas, 2)):
                diffp = a1 - a2
                antinode1 = a1 + diffp
                antinode2 = a2 - diffp
                if self._is_in_range(antinode1):
                    self.antinodes.add(antinode1)
                if self._is_in_range(antinode2):
                    self.antinodes.add(antinode2)

        return self.antinodes

    def _print(self, antinodes):
        _grid = [[_ for _ in line] for line in self.grid]
        for antinode in antinodes:
            _grid[antinode.y][antinode.x] = self.ANTINODE
        for line in _grid:
            print("".join(line))

    def resonant_antinode_unique_locations(self):
        for _, antennas in self.antennas.items():
            for a1, a2 in list(combinations(antennas, 2)):
                diffp = a1 - a2
                antinode1 = a1
                antinode2 = a2
                while self._is_in_range(antinode1):
                    self.resonant_antinodes.add(antinode1)
                    antinode1 += diffp

                while self._is_in_range(antinode2):
                    self.resonant_antinodes.add(antinode2)
                    antinode2 -= diffp

        return self.resonant_antinodes


@timer
def part1(input):
    return len(Grid(input).antinode_unique_locations())


@timer
def part2(input):
    return len(Grid(input).resonant_antinode_unique_locations())


print()
example_input = example_cl
print("part1 (example)", part1(example_input))
print("part2 (example)", part2(example_input))

print()
input = cl
print("part1", part1(input))
print("part2", part2(input))
