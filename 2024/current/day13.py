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

DAY = 13

logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")

example_content = read_input(locations.example_file)
example_cl = example_content.split("\n")
example_cl = example_cl[3:-4]

content = read_input(locations.input_file)
cl = content.split("\n")


class ClawMachine:
    def __init__(self, input):
        self.configs = []
        for i in range(0, len(input), 4):
            A, B, P = input[i : i + 3]
            # print(A, B, P)
            ax, ay = ints(A)[0]
            bx, by = ints(B)[0]
            px, py = ints(P)[0]
            self.configs.append(
                ButtonPrizeConfig(Point(ax, ay), Point(bx, by), Point(px, py))
            )

    def part_one(self):
        # Px = n*Ax + m*Bx
        # (Px - m*Bx) / Ax = n
        # Py = n*Ay + m*By
        # (Py - m*By) / Ay = (Px - m*Bx) / Ax
        # (Py - m*By) = (Ay*Px - Ay * m*Bx) / Ax
        # Ax*Py - Ax*m*By = Ay*Px - Ay * m*Bx
        # Ax*Py - Ay*Px = - Ay*m*Bx + Ax*m*By
        # Ax*Py - Ay*Px = m(- Ay*Bx + Ax*By)
        # m = (Ax*Py - Ay*Px) / (- Ay*Bx + Ax*By)
        min_token = 0
        for config in self.configs:
            Ax, Ay = config.A.x, config.A.y
            Bx, By = config.B.x, config.B.y
            Px, Py = config.P.x, config.P.y
            m = (Ax * Py - Ay * Px) / (-Ay * Bx + Ax * By)
            n = (Px - m * Bx) / Ax
            # print(f"B: {m}, A: {n} times")
            # print(n * 3 + m)
            # print(m.is_integer())
            if m.is_integer() and n.is_integer():
                min_token += n * 3 + m

        return int(min_token)

    def part_two(self):
        min_token = 0
        for config in self.configs:
            Ax, Ay = config.A.x, config.A.y
            Bx, By = config.B.x, config.B.y
            Px, Py = config.P.x + 10000000000000, config.P.y + 10000000000000
            m = (Ax * Py - Ay * Px) / (-Ay * Bx + Ax * By)
            n = (Px - m * Bx) / Ax
            # print(f"B: {m}, A: {n} times")
            # print(n * 3 + m)
            # print(m.is_integer())
            if m.is_integer() and n.is_integer():
                min_token += n * 3 + m

        return int(min_token)


class ButtonPrizeConfig:
    A: Point
    B: Point
    P: Point

    def __init__(self, A, B, P):
        self.A = A
        self.B = B
        self.P = P


@timer
def part1(input):
    c = ClawMachine(input)
    return c.part_one()


@timer
def part2(input):
    c = ClawMachine(input)
    return c.part_two()


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
