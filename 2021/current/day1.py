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


def part1(cl):
    count_increase = 0
    for i, cur in enumerate(cl):
        prev = cl[i - 1] if i > 0 else None
        if prev and (int(cur) - int(prev)) > 0:
            count_increase += 1
    print(count_increase)


part2cl = []
start = False
for i, cur in enumerate(cl):
    prev1 = cl[i - 1] if i > 0 else None
    prev2 = cl[i - 2] if i > 0 else None
    if prev2 == cl[0]:
        start = True
    if start:
        _sum = sum([int(prev2), int(prev1), int(cur)])
        part2cl.append(_sum)
        print(prev2, prev1, cur, _sum)

part1(part2cl)
