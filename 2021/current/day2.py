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

logger_init()
logger_enable(log, "day2")

DAY = 2

locations = get_locations(f"day{DAY}")


content = read_input(locations.example_file)
# content = read_input(locations.input_file)

cl = content.split("\n")


def part1(steps):
    horizontal = 0
    depth = 0
    for step, value in steps:
        if step == "forward":
            horizontal += value
        if step == "down":
            depth += value
        if step == "up":
            depth -= value
    return horizontal * depth


def part2(steps):
    horizontal = 0
    depth = 0
    aim = 0
    for step, value in steps:
        if step == "down":
            aim += value
        if step == "up":
            aim -= value
        if step == "forward":
            horizontal += value
            depth += aim * value
    return depth * horizontal


cl = cl[3:-4]
input = [[i for i in line.split(" ")] for line in cl]
input = [[line[0], int(line[1])] for line in input]
print("part1", part1(input))
print("part2", part2(input))
