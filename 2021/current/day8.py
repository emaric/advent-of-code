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

DAY = 8

logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")


# content = read_input(locations.example_file)
content = read_input(locations.input_file)

cl = content.split("\n")
# cl = cl[4:-4]


def part1(input):
    unique_combo_count = 0
    unique_combo_lengths = [2, 7, 3, 4]
    for line in input:
        line_count = sum(
            [
                1
                for combo in strs(line[line.find("|") + 1 :])
                if len(combo) in unique_combo_lengths
            ]
        )
        unique_combo_count += line_count

    return unique_combo_count


def _int_array_to_str(pattern):
    key = "".join(list(map(str, pattern)))
    return key


def _pattern_to_binary_str(pattern: str):
    unique_segments = "a b c d e f g".split(" ")
    value_pattern = [0 if segment not in pattern else 1 for segment in unique_segments]
    return _int_array_to_str(value_pattern)


def _pattern_to_binary_arr(pattern: str):
    unique_segments = "a b c d e f g".split(" ")
    value_pattern = [0 if segment not in pattern else 1 for segment in unique_segments]
    return value_pattern


##cf

# from 1, and 7 -> (top segment)

##a
## bd

## eg
# from 4, and top segment -> (top-left and middle)
# from 8, and (top-left and middle segment) -> (bottom-left and bottom segment)

# 0: zero should match 7; should match 8's bottom-left and bottom segments; and should match (4's top-left or middle segment)
# 2: should match 7's top-segment; 8's bottom-left and bottom segments;


def part2(input):
    output_value_sum = 0
    unique_combo_lengths = [None, 2, None, None, 4, None, None, 3, 7, None]
    for line in input:
        unique_signal_patterns = strs(line[: line.find("|")])
        value_output_strs = strs(line[line.find("|") + 1 :])

        # track unique combo patterns
        unique_combo_bi_arr_tracker = [None for _ in unique_combo_lengths]
        remaining_patterns_fives = []
        remaining_patterns_sixes = []
        for signal in unique_signal_patterns:
            signal_len = len(signal)
            binary_pattern = _pattern_to_binary_arr(signal)
            if signal_len in unique_combo_lengths:
                combo_index = unique_combo_lengths.index(signal_len)
                unique_combo_bi_arr_tracker[combo_index] = binary_pattern
            else:
                if signal_len == 5:
                    remaining_patterns_fives.append(binary_pattern)
                else:
                    remaining_patterns_sixes.append(binary_pattern)

        # decode remainig patterns (2, 3, 5)
        for signal in remaining_patterns_fives:
            seven = unique_combo_bi_arr_tracker[7]
            signal_minus_seven = [
                0 if seven[i] == signal[i] else signal[i] for i in range(len(signal))
            ]
            if sum(signal_minus_seven) == 2:
                unique_combo_bi_arr_tracker[3] = signal
            else:
                four = unique_combo_bi_arr_tracker[4]
                minus_four = [
                    0 if four[i] == signal_minus_seven[i] else signal_minus_seven[i]
                    for i in range(len(signal))
                ]
                if sum(minus_four) == 1:
                    unique_combo_bi_arr_tracker[5] = signal
                else:
                    unique_combo_bi_arr_tracker[2] = signal

        # decode remainig patterns (0, 6, 9)
        for signal in remaining_patterns_sixes:
            seven = unique_combo_bi_arr_tracker[7]
            signal_minus_seven = [
                0 if seven[i] == signal[i] else signal[i] for i in range(len(signal))
            ]

            if sum(signal_minus_seven) == 4:
                unique_combo_bi_arr_tracker[6] = signal
            else:
                three = unique_combo_bi_arr_tracker[3]
                minus_three = [
                    0 if three[i] == signal[i] else signal[i]
                    for i in range(len(signal))
                ]
                if sum(minus_three) == 1:
                    unique_combo_bi_arr_tracker[9] = signal
                else:
                    unique_combo_bi_arr_tracker[0] = signal

        # decode value output
        value_arr = []
        for value in value_output_strs:
            v = _pattern_to_binary_arr(value)
            int_value = unique_combo_bi_arr_tracker.index(v)
            value_arr.append(str(int_value))
        output_value_sum += int("".join(value_arr))

    return output_value_sum


def part2v2(input):
    # get the new value of each segment [a, b, c, d, e, f, g]

    pass


input = cl
print("part1", part1(input))
print("part2", part2(input))
