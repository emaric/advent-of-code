from __future__ import annotations

import enum
import math
import re
import sys
from collections import Counter, defaultdict
from copy import deepcopy
from dataclasses import dataclass, field
from functools import reduce
from pprint import pprint
from time import sleep
from typing import Any, ItemsView, Type

from shared.decorators import timer
from shared.helpers import Point, Vectors, get_locations, read_input
from shared.util import (
    clear_print,
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

DAY = 6

logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")

example_content = read_input(locations.example_file)
example_cl = example_content.split("\n")
example_cl = example_cl[3:-4]

content = read_input(locations.input_file)
cl = content.split("\n")


class Direction(enum.Enum):
    N = Point(0, -1)
    E = Point(1, 0)
    W = Point(-1, 0)
    S = Point(0, 1)

    @staticmethod
    def get_dir(dir_str: str) -> Direction:
        match dir_str:
            case "^":
                return Direction.N
            case ">":
                return Direction.E
            case "<":
                return Direction.W
            case "v":
                return Direction.S

    @property
    def turn_right(self):
        match self:
            case Direction.N:
                return Direction.E
            case Direction.E:
                return Direction.S
            case Direction.S:
                return Direction.W
            case Direction.W:
                return Direction.N

    def __str__(self):
        match self:
            case Direction.N | Direction.S:
                return "|"
            case Direction.E | Direction.W:
                return "-"


def clear_lines(lines_to_clear):
    """Clears the specified number of lines from the console."""
    for _ in range(lines_to_clear):
        # Move cursor up one line and clear the line
        sys.stdout.write("\033[F\033[K")


def update_line(line_number, text):
    """Update a specific line in the console."""
    # Move the cursor to the specific line number
    sys.stdout.write(f"\033[{line_number}F")  # Move up to the desired line
    sys.stdout.write("\033[K")  # Clear the line
    sys.stdout.write(text)  # Write the new content
    sys.stdout.write(f"\033[{line_number}E")  # Move up to the desired line
    # sys.stdout.flush()


def update_char(line_number, char_pos, char):
    sys.stdout.write(f"\033[{line_number}F")
    sys.stdout.write(f"\033[{char_pos}C")
    # sys.stdout.write("\033[P")
    sys.stdout.write(char)
    sys.stdout.write(f"\033[{line_number}E")
    # sys.stdout.flush()


class Map:
    def __init__(self, input: list[str]):
        self.g: dict[Point, str] = {}
        self.rows = len(input)
        self.cols = len(input[0])
        self.guard: Point
        self.guard_dir: Direction

        for row, line in enumerate(input):
            for col, char in enumerate(line):
                if char == "." or char == "#":
                    pass
                else:
                    self.guard = Point(col, row)
                    self.guard_dir = Direction.get_dir(char)
                    char = "."
                self.g[Point(col, row)] = char

    def print(self, grid=None):
        if grid is None:
            grid = self.g
        for row in range(self.rows):
            line_str = "".join(grid[Point(col, row)] for col in range(self.cols))
            line_str += "\n"
            sys.stdout.write(line_str)
        sys.stdout.flush()
        # sleep(0.1)

    def clear_console_grid(self):
        for _ in range(self.rows):
            sys.stdout.write("\033[F\033[K")
        sys.stdout.flush()

    def is_in_bounds(self, pos: Point) -> bool:
        return 0 <= pos.x < self.cols and 0 <= pos.y < self.rows

    def part_one(self):
        self.print()
        visited_positions: set[Point] = set()
        pos = self.guard
        next_dir = self.guard_dir
        while self.is_in_bounds(pos):
            if self.g[pos] != "#":
                visited_positions.add(pos)
                self.g[pos] = "X"
                update_char(self.rows - pos.row, pos.col, self.g[pos])
            else:
                pos -= next_dir.value
                next_dir = next_dir.turn_right
            pos += next_dir.value

        return len(visited_positions)

    def part_two(self):
        self.print()
        obstuctions: set[Point] = set()
        pos = self.guard
        next_dir = self.guard_dir
        while self.is_in_bounds(pos):
            if (
                self.is_in_bounds(pos + next_dir.value)
                and self.g[pos + next_dir.value] == "#"
            ):
                next_dir = next_dir.turn_right
                self.g[pos] = "+"
            else:
                if self.g[pos] != ".":
                    self.g[pos] = "+"
                else:
                    self.g[pos] = str(next_dir)
                if self.is_valid_obstruction(pos, next_dir):
                    obstuctions.add(pos + next_dir.value)
                    if len(obstuctions) > 1800:
                        self.clear_console_grid()
                        self.print()
                pos += next_dir.value

        for obstrucion in obstuctions:
            self.g[obstrucion] = "O"
        self.clear_console_grid()
        self.print()
        return len(obstuctions)

    def is_valid_obstruction(self, start: Point, dir: Direction) -> bool:
        if not self.is_in_bounds(start + dir.value):
            return False
        if self.g[start + dir.value] == "#":
            return False
        if self.g[start + dir.value] != ".":
            return False

        grid = deepcopy(self.g)
        grid[start + dir.value] = "#"
        # self.clear_console_grid()
        # for p in grid.keys():
        # update_char(self.rows - p.row, p.col, grid[p])
        # self.print(grid)
        visited: Counter[Point] = Counter()
        pos = start
        next_dir = dir.turn_right
        while self.is_in_bounds(pos):
            if (
                self.is_in_bounds(pos + next_dir.value)
                and grid[pos + next_dir.value] == "#"
            ):
                next_dir = next_dir.turn_right
                grid[pos] = "+"
            else:
                visited[pos] += 1
                if visited[pos] > 4 and (
                    grid[pos] == "+" or grid[pos] == str(next_dir)
                ):
                    return True

                if grid[pos] != "." and grid[pos] != str(next_dir):
                    grid[pos] = "+"
                else:
                    grid[pos] = str(next_dir)
                # update_char(self.rows - pos.row, pos.col, grid[pos])
                pos += next_dir.value
        return False


@timer
def part1(input):
    m = Map(input)
    return m.part_one()


@timer
def part2(input):
    m = Map(input)
    return m.part_two()


clear_print()
print("------------------------------------------------------------")
print("EXAMPLE INPUT")
print("------------------------------------------------------------")
example2 = """..#.....
.......#
........
.#......
#...#...
#.......
..^...#."""
# should be 4
print(part2(example2.split("\n")))

example3 = """...#
#...
.^#."""
# should be 0
print(part2(example3.split("\n")))

example4 = """...........
.#.........
.........#.
..#........
.......#...
....#......
...#...#...
......#....
...........
........#..
.^........."""
# should be 4
print(part2(example4.split("\n")))

example_input = example_cl
print(part1(example_input))
print()
print(part2(example_input))

print()
print()
print("------------------------------------------------------------")
print("REAL INPUT")
print("------------------------------------------------------------")
input = cl
print(part1(input))
print()
# 1770
print(part2(input))

# part 1
# failed: 5085 is too low

# part 2
# failed: 1884 is too high
# failed: 491 is too low
# failed: 721 is too low
# failed: 889
# failed: 745
# failed: 781
# failed: 813
# failed: 774
# failed: 1251
# failed: 1819
# failed: 1862
# failed: 1867
# failed: 1725
# failed: 1738
# failed: 1769
# failed: 1723
# failed: 1828
# failed: 1729
