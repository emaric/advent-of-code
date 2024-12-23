from __future__ import annotations

import enum
import math
import re
import sys
from collections import Counter, defaultdict
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

    @staticmethod
    def turn_right(cur_dir: Direction):
        match cur_dir:
            case Direction.N:
                return Direction.E
            case Direction.E:
                return Direction.S
            case Direction.S:
                return Direction.W
            case Direction.W:
                return Direction.N


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
    sys.stdout.flush()


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

        self.console_lines = []

    def print(self):
        clear_lines(self.rows)
        for row in range(self.rows):
            line_str = "".join(self.g[Point(col, row)] for col in range(self.cols))
            line_str += "\n"
            sys.stdout.write(line_str)
            self.console_lines.append(line_str)
        sys.stdout.flush()
        sleep(0.1)

    def is_in_bounds(self, pos: Point) -> bool:
        return 0 <= pos.x < self.cols and 0 <= pos.y < self.rows

    def part_one(self):
        # clear_print()
        self.print()
        # for i in range(1, self.rows):
        #     update_line(i, str(i))
        visited_positions: set[Point] = set()
        pos = self.guard
        next_dir = self.guard_dir
        while self.is_in_bounds(pos):
            if self.g[pos] != "#":
                visited_positions.add(pos)
                self.g[pos] = "X"
                line_str = "".join(
                    self.g[Point(col, pos.row)] for col in range(self.cols)
                )
                line_str
                update_line(self.rows - pos.row, line_str)
                # self.print()
            else:
                pos -= next_dir.value
                next_dir = Direction.turn_right(next_dir)
            pos += next_dir.value

        return len(visited_positions)


@timer
def part1(input):
    m = Map(input)
    return m.part_one()


@timer
def part2(input):
    return ""


print("------------------------------------------------------------")
print("EXAMPLE INPUT")
print("------------------------------------------------------------")
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
