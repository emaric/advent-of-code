import math
import re
from collections import Counter
from dataclasses import dataclass, field
from functools import reduce
from pprint import pprint

from shared.helpers import Grid, Point, Vectors, get_locations, read_input
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

DAY = 4

logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")


# content = read_input(locations.example_file)
content = read_input(locations.input_file)

cl = content.split("\n")
# cl = cl[3:-4]


def part1(input):
    count = 0
    patterns = [r"XMAS", r"SAMX"]

    def count_matches(source):
        matches_found = 0
        for pattern in patterns:
            matches = re.findall(pattern, source)
            matches_found += len(matches)
            # if matches:
            #     for match in matches:
            #         print(match)
        return matches_found

    # horizontal
    # print("horizontal matches:")
    for hline, i in zip(input, range(len(input))):
        # print(i, hline, ":")
        count += count_matches(hline)
    print()

    # vertical
    # print("vertical matches:")
    vlines = []
    for line in input:
        for x in range(len(line)):
            vline_arr = [input[y][x] for y in range(len(input))]
            vlines.append("".join(vline_arr))
        break
    for vline, i in zip(vlines, range(len(vlines))):
        # print(i, vline, ":")
        count += count_matches(vline)
    print()

    # diagonal
    # print("diagonal matches:")
    dlines = []
    # left to right-up
    # min x is len("XMAS")
    # min y is len("XMAS")
    # start (x,y) -> (0, len("XMAS"))
    #   line 0: (0, len("XMAS")) to (len("XMAS") or max(x), 0)
    #   line 1: (0, len("XMAS")+1) to (len("XMAS") or max(x), 0)

    # upper left
    pattern_len = len(patterns[0])
    for y in range(pattern_len - 1, len(input)):
        # print("y:", y)
        line = []
        _y = y
        for x in range(len(vlines)):
            # print("(", x, _y, ")", input[_y][x])
            line.append(input[_y][x])
            _y -= 1
            if _y < 0:
                break
        dlines.append("".join(line))
        # print()

    # lower right

    # print(input[-1])
    for x in range(1, len(vlines) - 3):
        _x = x
        # print("x:", x)
        line = []
        for y in range(1, len(input)):
            # print("(", _x, -y, ")", input[-y][_x])
            line.append(input[-y][_x])
            _x += 1
            if _x == len(vlines):
                break
        dlines.append("".join(line))

    # left to down right
    # upper right
    for x in range(0, len(vlines) - 3):
        # print("x:", x)
        _x = x
        line = []
        for y in range(len(input)):
            # print(_x, y, input[y][_x])
            line.append(input[y][_x])
            _x += 1
            if _x == len(vlines):
                break
        dlines.append("".join(line))

    # lower left
    for y in range(1, len(input) - 3):
        # print("y:", y)
        _y = y
        line = []
        for x in range(len(vlines)):
            # print(x, _y, input[_y][x])
            line.append(input[_y][x])
            _y += 1
            if _y == len(input):
                break
        dlines.append("".join(line))

    for line in dlines:
        count += count_matches(line)

    return count


def part2(input):
    return ""


input = cl
print("part1", part1(input))
print("part2", part2(input))
