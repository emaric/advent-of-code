import math
import re
from collections import Counter, defaultdict
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

DAY = 9

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
    arr = list(map(int, input))
    files = arr[::2]
    free = arr[1::2]
    out = [-1 for _ in range(sum(files))]

    i = 0
    end = False
    remaining_files = []
    for (
        file_i,
        file,
    ) in enumerate(files):
        for _1 in range(file):
            if not end:
                out[i] = file_i
                i += 1
                if i >= len(out):
                    end = True

            if end:
                remaining_files.append(file_i)

        if not end:
            i += free[file_i]
            if i >= len(out):
                end = True

    rl_i = -1
    for out_i, out_v in enumerate(out):
        if out_v < 0:
            out[out_i] = remaining_files[rl_i]
            rl_i -= 1

    checksum = 0
    for out_i, out_v in enumerate(out):
        checksum += out_i * out_v

    return checksum


class Space:
    def __init__(self, starting_index: int, size: int):
        self.starting_index = starting_index
        self.size = size

    def fill_space(self, space: int):
        self.starting_index += space
        self.size -= space

    def __str__(self):
        return f"{self.starting_index} : {self.size}"


@timer
def part2(input):
    arr = list(map(int, input))
    files = arr[::2]
    free = arr[1::2]
    out_size = sum(files) + sum(free)
    out = [0 for _ in range(out_size)]

    free_spaces: list[Space] = []
    starting_i_files = []

    i = 0
    for (
        file_i,
        file,
    ) in enumerate(files):
        starting_i_files.append(i)
        for _ in range(file):
            out[i] = file_i
            i += 1

        if file_i < len(free):
            free_length = free[file_i]
            free_spaces.append(Space(i, free_length))
            i += free_length

    for file_size, starting_i in zip(files[::-1], starting_i_files[::-1]):
        for free_space in free_spaces:
            if free_space.size >= file_size:
                if starting_i < free_space.starting_index:
                    break
                out[starting_i]
                value = out[starting_i]
                for i in range(file_size):
                    out[free_space.starting_index + i] = value
                    out[starting_i + i] = 0
                free_space.fill_space(file_size)
                break

    checksum = 0
    for out_i, out_v in enumerate(out):
        checksum += out_i * out_v

    return checksum


print()
example_input = example_cl[0]
print("part1 (example)", part1(example_input))
print("part2 (example)", part2(example_input))

print()
input = cl[0]
print("part1", part1(input))
print("part2", part2(input))
# failed: 8623254343177 is too high
