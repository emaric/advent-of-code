import math
import re
from collections import Counter
from dataclasses import dataclass, field
from enum import Enum
from functools import reduce
from pprint import pprint

from shared.decorators import timer
from shared.helpers import Grid, Point, VectorDicts, Vectors, get_locations, read_input
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

DAY = 6

logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")


# content = read_input(locations.example_file)
content = read_input(locations.input_file)

cl = content.split("\n")
# cl = cl[3:-4]


class Steps(Enum):
    N = Point(0, -1)
    S = Point(0, 1)
    W = Point(-1, 0)
    E = Point(1, 0)


class GuardMap:
    OBSTACLE_MARK = "#"

    grid_map = []
    width: int
    height: int

    starting_point: Point
    obstacles = []
    next_step: Steps
    all_points = []

    def __init__(self, input):
        self.width = len(input[0])
        self.height = len(input)
        for y in range(self.height):
            line = input[y]
            self.grid_map.append(line)
            matches = re.finditer(r"(\^|v|<|>)|(" + self.OBSTACLE_MARK + ")", line)
            for m in matches:
                x = m.start()
                if m.group(1):
                    self.starting_point = Point(x, y)
                    self.next_step = self._get_next_step(m.group(1))
                if m.group(2):
                    self.obstacles.append(Point(x, y))

    def _get_next_step(self, arrow_str):
        match arrow_str:
            case "^":
                return Steps.N
            case "v":
                return Steps.S
            case "<":
                return Steps.W
            case ">":
                return Steps.E

    def _get_right_turn_step(self, start: Steps):
        match start:
            case Steps.N:
                return Steps.E
            case Steps.E:
                return Steps.S
            case Steps.S:
                return Steps.W
            case Steps.W:
                return Steps.N

    def _is_in_range(self, point):
        x, y = point.x, point.y
        return x >= 0 and y >= 0 and x < self.width and y < self.height

    def get_visits(self):
        visits = set()

        p = self.starting_point
        next_step = self.next_step

        # test_input = [[line[i] for i in range(len(line))] for line in self.grid_map]

        while True:
            while p not in self.obstacles and self._is_in_range(p):
                # test_input[p.y][p.x] = "X"
                visits.add(p)
                p += next_step.value

            # for test_line in test_input:
            # print("".join(test_line))

            if self._is_in_range(p):
                p -= next_step.value
                next_step = self._get_right_turn_step(next_step)
            else:
                break

        return visits


@timer
def part1(input):
    visits = GuardMap(input).get_visits()
    test_input = [[line[i] for i in range(len(line))] for line in input]
    for v in visits:
        test_input[v.y][v.x] = "X"

    test = 0
    for l in test_input:
        l.count("X")
        test += l.count("X")
        print("".join(l))
    return test


@timer
def part2(input):
    return ""


input = cl

print()
# failed: 5085 is too low
print("part1", part1(input))

print()
print("part2", part2(input))
