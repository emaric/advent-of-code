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
    sign,
    strs,
    wait_for_input,
)

DAY = 7

logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")


# content = read_input(locations.example_file)
content = read_input(locations.input_file)

cl = content.split("\n")
# cl = cl[3:-4]


def part1(input):
    # count crabs in position
    crab_count_in_pos = {}
    for crab in input:
        if crab not in crab_count_in_pos:
            crab_count_in_pos[crab] = 0
        crab_count_in_pos[crab] += 1

    # calculate fuel for each position to max
    max_pos = max(input)
    min_fuel = None
    for pos in range(max_pos):
        total_fuel = 0
        for crab in crab_count_in_pos.keys():
            fuel = max(crab, pos) - min(crab, pos)
            fuel *= crab_count_in_pos.get(crab)
            total_fuel += fuel
            # print("crab", crab, "fuel", fuel)
        if min_fuel is None:
            min_fuel = total_fuel
        min_fuel = min(min_fuel, total_fuel)
        # print("pos", pos, "fuel", total_fuel)

    return min_fuel


def part2(input):
    # count crabs in position
    crab_count_in_pos = {}
    for crab in input:
        if crab not in crab_count_in_pos:
            crab_count_in_pos[crab] = 0
        crab_count_in_pos[crab] += 1

    # calculate fuel for each position to max
    max_pos = max(input)
    min_fuel = None
    for pos in range(max_pos):
        total_fuel = 0
        for crab in crab_count_in_pos.keys():
            start = min(crab, pos)
            end = max(crab, pos)
            fuel = start - end
            fuel = (fuel / 2) * (fuel - 1)
            fuel *= crab_count_in_pos.get(crab)
            total_fuel += fuel
            # print("crab", crab, "fuel", fuel)
        if min_fuel is None:
            min_fuel = total_fuel
        min_fuel = min(min_fuel, total_fuel)
        # print("pos", pos, "fuel", total_fuel)

    return min_fuel


input = cl
input = list(map(int, input[0].split(",")))
print("part1", part1(input))
print("part2", part2(input))
