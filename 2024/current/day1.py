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

DAY = 1

logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")


content = read_input(locations.example_file)
# content = read_input(locations.input_file)

cl = content.split("\n")
cl = cl[3:-4]


def part1(input):
    return input


def part2(input):
    return input


input = cl
print("part1", part1(input))
print("part2", part2(input))
