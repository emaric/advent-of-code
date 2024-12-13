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
    print("files", files, "sum", sum(files))
    print("free", free, "sum", sum(free))
    out = [0 for _ in range(sum(files))]

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
            for _2 in range(free[file_i]):
                out[i] = -1
                i += 1
                if i >= len(out):
                    end = True
                    break

    rl_i = -1
    for out_i, out_v in enumerate(out):
        if out_v < 0:
            out[out_i] = remaining_files[rl_i]
            rl_i -= 1

    checksum = 0
    for out_i, out_v in enumerate(out):
        checksum += out_i * out_v

    return checksum


@timer
def part2(input):
    return ""


print()
example_input = example_cl[0]
print("part1 (example)", part1(example_input))
print("part2 (example)", part2(example_input))

print()
input = cl[0]
print("part1", part1(input))
print("part2", part2(input))
