import itertools
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

DAY = 7

logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")


example_content = read_input(locations.example_file)
example_cl = example_content.split("\n")
example_cl = example_cl[3:-4]

content = read_input(locations.input_file)
cl = content.split("\n")


def parse_input_str(input_str):
    parsed_input = []
    for line in input_str:
        sub_total_str, nums_str = line.split(":")
        sub_total = int(sub_total_str)
        nums = list(map(int, nums_str.strip().split(" ")))
        parsed_input.append([sub_total, nums])
    return parsed_input


def create_cartesian_product(length, operators=["*", "+"]):
    return list(itertools.product(operators, repeat=length))


@timer
def part1(input):
    total_calibration_result = 0

    for line in input:
        sub_total, nums = line

        operators_perm = create_cartesian_product(len(nums) - 1)
        for operators in operators_perm:
            _sub_total = nums[0]
            for num, operator in zip(nums[1:], operators):
                if operator == "*":
                    _sub_total *= num
                if operator == "+":
                    _sub_total += num
            if _sub_total == sub_total:
                total_calibration_result += sub_total
                break

    return total_calibration_result


@timer
def part2(input):
    total_calibration_result = 0

    for line in input:
        sub_total, nums = line

        operators_perm = create_cartesian_product(len(nums) - 1, ["*", "+", "||"])
        for operators in operators_perm:
            _sub_total = nums[0]
            for num, operator in zip(nums[1:], operators):
                if operator == "*":
                    _sub_total *= num
                if operator == "+":
                    _sub_total += num
                if operator == "||":
                    _sub_total = int(f"{_sub_total}{num}")
            if _sub_total == sub_total:
                total_calibration_result += sub_total
                break

    return total_calibration_result

    return ""


print()
example_input = example_cl
example_input = parse_input_str(example_input)
print("part1 (example)", part1(example_input))
print("part2 (example)", part2(example_input))

print()
input = cl
input = parse_input_str(input)
print("part1", part1(input))
print("part2", part2(input))
