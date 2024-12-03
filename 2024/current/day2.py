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
    sign,
    strs,
    wait_for_input,
)

DAY = 2

logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")


# content = read_input(locations.example_file)
content = read_input(locations.input_file)

cl = content.split("\n")
# cl = cl[3:-4]


@timer
def part1(input):
    count = 0
    valid_diff = {1, 2, 3, -1, -2, -3}
    for line, i in zip(input, range(len(input))):
        levels = list(map(int, line.split(" ")))
        duplicates = len(levels) - len(set(levels))
        if duplicates <= 0:
            level_diffs = [a - b for a, b in zip(levels, levels[1:])]
            level_diffs_signs = [
                1 for a, b in zip(level_diffs, level_diffs[1:]) if sign(a) == sign(b)
            ]
            is_all_decreasing_or_increasing = (
                len(level_diffs) - len(level_diffs_signs) == 1
            )
            if is_all_decreasing_or_increasing:
                count += 1 if len(set(level_diffs) - valid_diff) == 0 else 0
    return count


@timer
def part2(input):
    count = 0
    decreasing_diffs = {1, 2, 3}
    increasing_diffs = {-1, -2, -3}

    def is_safe(a, b, c):
        diff_prev = a - b
        diff = b - c
        if (
            sign(diff_prev) == sign(diff)
            and abs(diff_prev) in decreasing_diffs
            and abs(diff) in decreasing_diffs
        ):
            return True
        return False

    def is_arr_safe(arr):
        diffs = [a - b for a, b in zip(arr, arr[1:])]
        is_decreasing = len(set(diffs) - decreasing_diffs) == 0
        is_increasing = len(set(diffs) - increasing_diffs) == 0
        return (
            is_decreasing
            and (not is_increasing)
            or is_increasing
            and (not is_decreasing)
        )

    for line in input:
        levels = list(map(int, line.split(" ")))
        unsafe_sequences = []

        def unsafe_sequences_count():
            return len(unsafe_sequences)

        for a, b, c in zip(levels, levels[1:], levels[2:]):
            if not is_safe(a, b, c):
                unsafe_sequences.append([a, b, c])
                if unsafe_sequences_count() > 2:
                    break
        if unsafe_sequences_count() == 0:
            count += 1
        else:
            if unsafe_sequences_count() == 1:
                if is_arr_safe(levels[1:]) or is_arr_safe(levels[:-1]):
                    count += 1
            elif unsafe_sequences_count() == 2:
                for index_to_exclude in range(len(levels)):
                    if is_arr_safe(
                        [levels[i] for i in range(len(levels)) if i != index_to_exclude]
                    ):
                        count += 1
                        break

    return count


input = cl
print("part1", part1(input))
print("part2", part2(input))
