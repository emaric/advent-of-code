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

DAY = 8

logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")


# content = read_input(locations.example_file)
content = read_input(locations.input_file)

cl = content.split("\n")
# cl = cl[4:-4]


def part1(input):
    unique_combo_count = 0
    unique_combo_lengths = [2, 7, 3, 4]
    for line in input:
        line_count = sum(
            [
                1
                for combo in strs(line[line.find("|") + 1 :])
                if len(combo) in unique_combo_lengths
            ]
        )
        unique_combo_count += line_count

    return unique_combo_count


def part2(input):
    return input


input = cl
print("part1", part1(input))
# print("part2", part2(input))
