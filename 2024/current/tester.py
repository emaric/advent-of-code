from __future__ import annotations

import enum
import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from functools import reduce
from pprint import pprint
from typing import Any, ItemsView, Type

from shared.decorators import timer
from shared.helpers import Point, Vectors, get_locations, read_input
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

DAY = 0

logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")

example_content = read_input(locations.example_file)
example_cl = example_content.split("\n")
example_cl = example_cl[3:-4]

content = read_input(locations.input_file)
cl = content.split("\n")


@timer
def part1(input):
    return input


@timer
def part2(input):
    return ""


print("------------------------------------------------------------")
print("EXAMPLE INPUT")
print("------------------------------------------------------------")
example_input = example_cl
print(part1(example_input))
print()
print(part2(example_input))

print()
print()
print("------------------------------------------------------------")
print("REAL INPUT")
print("------------------------------------------------------------")
input = cl
print(part1(input))
print()
print(part2(input))
