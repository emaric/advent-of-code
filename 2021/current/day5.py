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

DAY = 5
logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")


# content = read_input(locations.example_file)
content = read_input(locations.input_file)

cl = content.split("\n")
# cl = cl[3:-4]


def part1(input):
    grid = []
    grid_width = 1
    for segment in input:
        [x1, y1], [x2, y2] = segment

        vertical = False
        horizontal = False
        if x1 == x2:
            vertical = True
        if y1 == y2:
            horizontal = True

        min_x = min(x1, x2)
        min_y = min(y1, y2)

        max_x = max(x1, x2)
        max_y = max(y1, y2)

        grid_width = max(max_x + 1, grid_width)

        # increase grid size / vertically
        if len(grid) <= max_y:
            for _ in range(len(grid), max_y + 1):
                grid.append([0 for _ in range(grid_width)])

        # increase grid width
        for h_line in grid:
            if grid_width > len(h_line) + 1:
                for _ in range(len(h_line), grid_width + 1):
                    h_line.append(0)

        if horizontal:
            for x in range(min_x, max_x + 1):
                grid[y1][x] += 1

        if vertical:
            for y in range(min_y, max_y + 1):
                grid[y][x1] += 1

    intersections = 0
    for h_line in grid:
        intersections += sum([1 for i in h_line if i > 1])
    return intersections


def part2(input):
    grid = []
    grid_width = 1
    for segment in input:
        [x1, y1], [x2, y2] = segment

        vertical = False
        horizontal = False
        diagonal = False
        if x1 == x2:
            vertical = True
        if y1 == y2:
            horizontal = True
        if not vertical and not horizontal:
            diagonal = True

        min_x = min(x1, x2)
        min_y = min(y1, y2)

        max_x = max(x1, x2)
        max_y = max(y1, y2)

        grid_width = max(max_x + 1, grid_width)

        # increase grid size / vertically
        if len(grid) <= max_y:
            for _ in range(len(grid), max_y + 1):
                grid.append([0 for _ in range(grid_width)])

        # increase grid width
        for h_line in grid:
            if grid_width > len(h_line) + 1:
                for _ in range(len(h_line), grid_width + 2):
                    h_line.append(0)

        if horizontal:
            for x in range(min_x, max_x + 1):
                grid[y1][x] += 1

        if vertical:
            for y in range(min_y, max_y + 1):
                grid[y][x1] += 1

        if diagonal:
            # print("diagonal", segment)
            x = x1
            y = y1
            right_to_left = False
            left_to_right = False
            upwards = False
            downwards = False
            # right to left
            if x1 > x2:
                right_to_left = True
                x = max_x
                # print("right to left")
            # left to right
            if x2 > x1:
                left_to_right = True
                x = min_x
                # print("left to right")
            if y1 > y2:
                upwards = True
                y = max_y
                # print("upwards")
            if y2 > y1:
                downwards = True
                y = min_y
                # print("downwards")
            for _ in range(min_y, max_y + 1):
                # print(
                # "----------x:", x, "y:", y, "min", min_x, min_y, "max", max_x, max_y
                # )
                grid[y][x] += 1
                if right_to_left:
                    x -= 1
                if left_to_right:
                    x += 1
                    # print("x+=1", x)
                if upwards:
                    y -= 1
                if downwards:
                    y += 1

            # print("cur grid")
            # for h_line in grid:
            # print(h_line)

    # for h_line in grid:
    # print(h_line)

    intersections = 0
    for h_line in grid:
        intersections += sum([1 for i in h_line if i > 1])
    return intersections


input = cl

input = [
    [
        list(map(int, coordinates_str.split(",")))
        for coordinates_str in segment.split(" -> ")
    ]
    for segment in input
]

# print("input", input)
print("part1", part1(input))
print("part2", part2(input))
