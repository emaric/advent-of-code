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
content = read_input(locations.input_file)
# part1 ans: 2250415
cl = content.split("\n")
# cl = cl[3:-4]


def part1(input):
    gamma_rate_bi = ""
    epsilon_rate_bi = ""
    line_count = len(input)
    for pos in range(len(input[0])):
        x = [int(line[pos]) for line in input]
        gbit = 1 if sum(x) <= line_count / 2 else 0
        ebit = 0 if gbit == 1 else 1
        gamma_rate_bi += str(gbit)
        epsilon_rate_bi += str(ebit)

    gamma_rate = int(gamma_rate_bi, 2)
    epsilon_rate = int(epsilon_rate_bi, 2)

    consumption = gamma_rate * epsilon_rate
    return consumption


def part2(input):
    most_common_list = [i for i in input]
    least_common_list = [i for i in input]
    for pos in range(0, len(input[0])):
        x = [int(line[pos]) for line in most_common_list]
        y = [int(line[pos]) for line in least_common_list]

        cur_most_common_bit = 1 if sum(x) >= len(most_common_list) / 2 else 0
        cur_least_common_bit = 1 if sum(y) < len(least_common_list) / 2 else 0
        if len(most_common_list) > 1:
            most_common_list = [
                line
                for line in most_common_list
                if int(line[pos]) == cur_most_common_bit
            ]

        if len(least_common_list) > 1:
            least_common_list = [
                line
                for line in least_common_list
                if int(line[pos]) == cur_least_common_bit
            ]

    oxygen_generator_rating = int(most_common_list[0], 2)
    co2_scrubber_rating = int(least_common_list[0], 2)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating

    return life_support_rating


input = cl
print("part1", part1(input))
print("part2", part2(input))
