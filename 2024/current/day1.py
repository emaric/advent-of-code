import math
import re
from collections import Counter
from dataclasses import dataclass, field
from functools import reduce
from pprint import pprint

from shared.decorators import timer
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

DAY = 1

logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")


# content = read_input(locations.example_file)
content = read_input(locations.input_file)

cl = content.split("\n")
# cl = cl[3:-4]


def part1(input):
    lines = [ints(_) for _ in input]
    left = [line[0][0] for line in lines]
    right = [line[0][1] for line in lines]
    left = sorted(left)
    right = sorted(right)
    return sum([abs(a - b) for a, b in zip(left, right)])


@timer
def part2(input):
    lines = [ints(_) for _ in input]
    left = [line[0][0] for line in lines]
    right = [line[0][1] for line in lines]
    return sum([sum([_ for _ in right if _ == l]) for l in left])


@timer
def part2v2(input):
    lines = [ints(_) for _ in input]
    counter = {}
    left = [line[0][0] for line in lines]
    right = [line[0][1] for line in lines]
    counter = Counter(right)
    return sum([l * counter[l] for l in left])


input = cl
print("part1", part1(input))

print("part2", part2(input))
print("part2v2", part2v2(input))
