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
    log,
    logger_config,
    logger_enable,
    logger_init,
    print_array,
    wait_for_input,
)

logger_init()
logger_enable(log, "day1")

DAY = 1

locations = get_locations(f"day{DAY}")


# content = read_input(locations.example_file)
content = read_input(locations.input_file)

cl = content.split("\n")
# cl = cl[3:-4]

# print(content)
# print("cl:", cl)


def part1(ar):
    return sum([(1 if pair[1] > pair[0] else 0) for pair in zip(ar, ar[1:])])


def part2(ar):
    summed_triplets = [sum(triplet) for triplet in zip(ar, ar[1:], ar[2:])]
    return part1(summed_triplets)


input = [int(x) for x in cl]
print("part1", part1(input))
print("part2", part2(input))
