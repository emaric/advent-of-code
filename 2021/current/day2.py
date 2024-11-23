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


# content = read_input(locations.example_file)
content = read_input(locations.input_file)

cl = content.split("\n")

"""
horizontal = 0
depth = 0

for line in cl:
    command = strs(line)[0]
    steps = ints(line)[0][0]
    if command == "forward":
        horizontal += int(steps)
    elif command == "down":
        depth += int(steps)
    else:
        depth -= steps

print(horizontal * depth)
"""
horizontal = 0
depth = 0
aim = 0

for line in cl:
    command = strs(line)[0]
    steps = ints(line)[0][0]
    if command == "forward":
        horizontal += steps
        depth += aim * steps
    elif command == "down":
        aim += steps
    else:
        aim -= steps

print(horizontal * depth)
