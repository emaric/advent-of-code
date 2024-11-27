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

DAY = 6

logger_init()
logger_enable(log, f"day{DAY}")


locations = get_locations(f"day{DAY}")


# content = read_input(locations.example_file)
content = read_input(locations.input_file)

cl = content.split("\n")
# cl = cl[3:-4]


def part1(input, days=80):
    if len(input) == 0:
        return 0
    new_lantern_fish = []
    for day in range(0, days):
        print("day", day, input, len(new_lantern_fish))
        zeroes = len([_ for _ in input if _ == 0])
        new_lantern_zeroes = len([_ for _ in new_lantern_fish if _ == 0])
        for _ in range(zeroes):
            new_lantern_fish.append(9)
        for _ in range(new_lantern_zeroes):
            new_lantern_fish.append(9)
        input = [i - 1 if i - 1 >= 0 else 6 for i in input]
        new_lantern_fish = [i - 1 if i - 1 >= 0 else 6 for i in new_lantern_fish]

    return len(new_lantern_fish) + len(input)


def solution(input, days):
    fish_count = [0 for _ in range(9)]
    # print(fish_count)
    for fish in input:
        fish_count[fish] += 1
    for day in range(0, days):
        # print("day", day, fish_count, sum(fish_count))
        new_fishes = fish_count[0]
        sixes = new_fishes + fish_count[7]
        eights = fish_count[8]
        fish_count = fish_count[1:7]
        fish_count.append(sixes)
        fish_count.append(eights)
        fish_count.append(new_fishes)
    return sum(fish_count)


input = cl
input = list(map(int, input[0].split(",")))
print("part1", solution([_ for _ in input], 80))
print("part2", solution([_ for _ in input], 256))
