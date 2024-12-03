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

DAY = 3

logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")


# content = read_input(locations.example_file)
content = read_input(locations.input_file)

cl = content.split("\n")
# cl = cl[3:-4]


@timer
def part1(input):
    matches = re.findall(r"mul\((\d+),(\d+)\)", input)
    ans = sum(int(match[0]) * int(match[1]) for match in matches)

    # 31103311 - wrong! answer too low
    return ans


def part2(input):
    return input


input = cl
input = content
print("part1", part1(input))
# print("part2", part2(input))
