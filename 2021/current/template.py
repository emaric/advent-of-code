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
logger_enable(log, "day3")

DAY = 3

locations = get_locations(f"day{DAY}")


content = read_input(locations.example_file)
# content = read_input(locations.input_file)

cl = content.split("\n")


def part1(input):
    def _most_common_bit_in_position():
        return 0

    def _least_common_bit_in_position():
        return 0

    gamma_rate = _most_common_bit_in_position()
    epsilon_rate = _least_common_bit_in_position()
    consumption = gamma_rate * epsilon_rate
    return consumption


def part2(input):
    return input


input = cl[3:-4]
print("part1", part1(input))
print("part2", part2(input))
