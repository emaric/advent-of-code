import math
import re
from collections import Counter, defaultdict
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


example_content = read_input(locations.example_file)
example_cl = example_content.split("\n")
example_cl = example_cl[3:-4]

content = read_input(locations.input_file)
cl = content.split("\n")


class Steps(Enum):
    N = Point(0, -1)
    S = Point(0, 1)
    W = Point(-1, 0)
    E = Point(1, 0)


class GuardMap:
    OBSTACLE_MARK = "#"

    width: int
    height: int

    starting_point: Point
    next_step: Steps

    def __init__(self, input):
        self.obstacles = []
        self.all_points = []
        self.grid_map = []
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
        visits = []

        p = self.starting_point
        next_step = self.next_step

        # test_input = [[line[i] for i in range(len(line))] for line in self.grid_map]

        while True:
            while p not in self.obstacles and self._is_in_range(p):
                # test_input[p.y][p.x] = "X"
                visits.append(p)
                p += next_step.value

            # for test_line in test_input:
            # print("".join(test_line))

            if self._is_in_range(p):
                p -= next_step.value
                next_step = self._get_right_turn_step(next_step)
            else:
                break

        return visits

    def get_visits_direction_map(self):
        visits_direction_map: dict[str:set] = defaultdict(set)

        position = self.starting_point
        next_step = self.next_step

        test_input = [[line[i] for i in range(len(line))] for line in self.grid_map]

        def _print():
            for test_line in test_input:
                print("".join(test_line))

        # move to the next step
        while True:
            # for debug:
            if test_input[position.y][position.x] == ".":
                test_input[position.y][position.x] = next_step.name

            visits_direction_map[next_step.name].add(position)

            next_position = position + next_step.value
            if not self._is_in_range(next_position):
                break

            # turn right if the next position is an obstacle
            if next_position in self.obstacles:
                next_step = self._get_right_turn_step(next_step)
            # else:
            #     right_step = self._get_right_turn_step(next_step)
            #     right_position = position + right_step.value
            #     if self._is_creates_a_loop(
            #         right_position, right_step, visits_direction_map
            #     ):
            #         obstraction_points.add(next_position)
            #         # for debug:
            #         test_input[next_position.y][next_position.x] = "O"
            else:
                position += next_step.value

        return visits_direction_map

    def get_obstruction_positions(self):
        obstraction_points = set()
        visits_direction_map = self.get_visits_direction_map()
        visited = defaultdict(set)
        visited_test = self.get_visits()
        visited_arr = []

        position = self.starting_point
        next_step = self.next_step

        test_input = [[line[i] for i in range(len(line))] for line in self.grid_map]

        def _print():
            for test_line in test_input:
                print("".join(test_line))

        # move to the next step
        while True:
            # for debug:
            if test_input[position.y][position.x] == ".":
                test_input[position.y][position.x] = next_step.name

            visited[next_step.name].add(position)
            visited_arr.append(position)

            next_position = position + next_step.value
            if not self._is_in_range(next_position):
                break
            # turn right if the next position is an obstacle
            if next_position in self.obstacles:
                next_step = self._get_right_turn_step(next_step)
            else:
                right_step = self._get_right_turn_step(next_step)
                right_position = position + right_step.value
                if (
                    # and right_position in visits_direction_map[right_step.name]
                    # and right_position in visited_test
                    next_position not in visited_arr
                    and self._is_creates_a_loop(position, right_step, visited)
                ):
                    obstraction_points.add(next_position)
                    # for debug:
                    test_input[next_position.y][next_position.x] = "O"
                    _print()
                    print()

                position += next_step.value

        _print()
        return len(obstraction_points)

    def _is_creates_a_loop(self, start, starting_step, visited_map):
        # returns True if moving in next_step creates a loop or visits the point in the same direction twice
        # returns False if visited map is empty or the the position is out of the map
        # if len(visited_map) < 4:
        #     return False

        test_input = [[line[i] for i in range(len(line))] for line in self.grid_map]

        def _print():
            print("-----")
            for test_line in test_input:
                print("".join(test_line))
            print("-----")

        position = start
        next_step = starting_step
        visited = defaultdict(set)
        while True:
            if not self._is_in_range(position):
                return False

            if position in visited[next_step.name]:
                _print()
                return True

            if position in visited_map[next_step.name]:
                _print()
                return True

            if test_input[position.y][position.x] == ".":
                test_input[position.y][position.x] = next_step.name

            visited[next_step.name].add(position)
            next_position = position + next_step.value
            if next_position in self.obstacles:
                next_step = self._get_right_turn_step(next_step)
            else:
                position += next_step.value

        return False


@timer
def part1(input):
    visits = GuardMap(input).get_visits()
    return len(set(visits))


@timer
def part2(_input):
    return GuardMap(_input).get_obstruction_positions()


example_input = example_cl
input = cl

print()
# failed: 5085 is too low
# print("part1", part1(input))

print("part2 (example):", part2(example_input))
print()
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
print("part2", part2(input))
