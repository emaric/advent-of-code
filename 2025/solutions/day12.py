import math
import re
from collections import defaultdict
from dataclasses import dataclass
from functools import cached_property
from itertools import combinations
from turtle import poly
from typing import ClassVar
from xml.etree.ElementTree import register_namespace


@dataclass
class Point:
    row: int
    col: int

    def __hash__(self):
        return hash((self.row, self.col))

    @property
    def N(self):
        return Point(self.row - 1, self.col)

    @property
    def E(self):
        return Point(self.row, self.col + 1)

    @property
    def W(self):
        return Point(self.row, self.col - 1)

    @property
    def S(self):
        return Point(self.row + 1, self.col)

    @property
    def NE(self):
        return Point(self.row - 1, self.col + 1)

    @property
    def NW(self):
        return Point(self.row - 1, self.col - 1)

    @property
    def SE(self):
        return Point(self.row + 1, self.col + 1)

    @property
    def SW(self):
        return Point(self.row + 1, self.col - 1)

    @cached_property
    def adjacent_points(self):
        return [
            self.NW,
            self.N,
            self.NE,
            self.W,
            self.E,
            self.SW,
            self.S,
            self.SE,
        ]

    @property
    def adjacent_points_async(self):
        ap_str = ["NW", "N", "NE", "W", "E", "SW", "S", "SE"]
        for p in ap_str:
            yield self.__getattribute__(p)

    @property
    def distance(self):
        return math.sqrt(self.col**2 + self.row**2)


@dataclass
class Shape:
    index: int
    grid: dict[Point, str]
    center: ClassVar[Point] = Point(1, 1)

    def __hash__(self):
        return hash((self.index))

    def print(self):
        for row in range(3):
            print([self.grid[Point(row, col)] for col in range(3)])

    @cached_property
    def hflip(self) -> Shape:
        grid = {}
        for row in range(3):
            _col = 0
            for col in range(2, -1, -1):
                grid[Point(row, _col)] = self.grid[Point(row, col)]
                _col += 1

        return Shape(self.index, grid)

    @cached_property
    def r90deg(self) -> Shape:
        grid = {}
        center = Point(1, 1)
        grid[center.NW] = self.grid[center.SW]
        grid[center.N] = self.grid[center.W]
        grid[center.NE] = self.grid[center.NW]

        grid[center.W] = self.grid[center.S]
        grid[center] = self.grid[center]
        grid[center.E] = self.grid[center.N]

        grid[center.SW] = self.grid[center.SE]
        grid[center.S] = self.grid[center.E]
        grid[center.SE] = self.grid[center.NE]

        return Shape(self.index, grid)

    @cached_property
    def equivalent_shapes(self) -> list[Shape]:
        shapes: list[Shape] = []

        r1 = self.r90deg
        r2 = r1.r90deg
        r3 = r2.r90deg

        shapes.append(r1)
        shapes.append(r2)
        shapes.append(r3)

        shapes.append(self.hflip)

        hflip_r1 = self.hflip.r90deg
        hflip_r2 = hflip_r1.r90deg
        hflip_r3 = hflip_r2.r90deg

        shapes.append(hflip_r1)
        shapes.append(hflip_r2)
        shapes.append(hflip_r3)

        return shapes

    def __lt__(self, other: Shape):
        return self.empty_space_distance < other.empty_space_distance

    def __le__(self, other: Shape):
        return self.empty_space_distance <= other.empty_space_distance

    def __gt__(self, other: Shape):
        return self.empty_space_distance > other.empty_space_distance

    def __ge__(self, other: Shape):
        return self.empty_space_distance >= other.empty_space_distance

    @cached_property
    def empty_space_distance(self):
        total = 0
        if self.grid[Shape.center] == ".":
            total += Shape.center.distance
        for p in Shape.center.adjacent_points:
            if self.grid[p] == ".":
                total += p.distance
        return total


@dataclass
class Region:
    width: int
    length: int
    quantities: list[int]
    grid: dict[Point, str]

    def print(self):
        for row in range(self.length):
            print(
                "".join(
                    [
                        "."
                        if Point(row, col) not in self.grid
                        else self.grid[Point(row, col)]
                        for col in range(self.width)
                    ]
                )
            )


def _can_be_inserted(point, region, shape):
    can_be_inserted = True
    if shape.grid[Shape.center] == "#" and point in region.grid:
        return False
    for rp, sp in zip(point.adjacent_points_async, Shape.center.adjacent_points):
        if shape.grid[sp] == "#" and rp in region.grid:
            can_be_inserted = False
            break
    return can_be_inserted


def _insert(point, region, shape):
    if shape.grid[Shape.center] == "#":
        region.grid[point] = str(shape.index)
    for rp, sp in zip(point.adjacent_points_async, Shape.center.adjacent_points):
        if shape.grid[sp] == "#":
            region.grid[rp] = str(shape.index)  # shape.grid[sp]


def try_insert(point: Point, region: Region, shape: Shape):
    if len(region.grid) <= 0:
        _insert(point, region, shape)
        return True
    else:
        if _can_be_inserted(point, region, shape):
            _insert(point, region, shape)
            return True
        else:
            for trans_shape in shape.equivalent_shapes:
                if _can_be_inserted(point, region, trans_shape):
                    _insert(point, region, trans_shape)
                    return True
    return False


def has_next(point, region):
    max_col = region.width - 1
    max_row = region.length - 1
    return not (point.E.col == max_col and point.S.row == max_row)


def next(point: Point, region: Region):
    max_col = region.width - 1
    max_row = region.length - 1

    if point.E.col == max_col:
        if point.S.row == max_row:
            raise ValueError("Reached end.")
        return Point(point.S.row, 1)
    return point.E


def parse_input(input: str):
    shapes: list[Shape] = []
    regions: list[Region] = []

    shape: Shape | None = None
    row = 0
    for line in input.split("\n"):
        if len(line) == 2:
            row = 0
            shape = Shape(int(line[0]), {})
        elif ":" in line and len(line.split(":")[0]) > 1:
            size, quantities = line.split(":")
            width, length = [int(v) for v in size.split("x")]

            min_v = min(width, length)
            max_v = max(width, length)
            regions.append(
                Region(
                    min_v,
                    max_v,
                    [int(q) for q in quantities.strip().split(" ")],
                    {},
                )
            )
        elif len(line) <= 0:
            continue
        elif shape is not None:
            for col, v in enumerate(line):
                shape.grid[Point(row, col)] = v
            row += 1
            if row > 2:
                shape = max([shape, *shape.equivalent_shapes])
                shapes.append(shape)

    return shapes, regions


def part_one(input: str):
    answer = 0
    shapes, regions = parse_input(input)

    print("Shapes:")
    for shape in shapes:
        print(shape.index, ":")
        shape.print()
        print()

    print("Regions:")
    for region in regions:
        print(region)

        point = Point(1, 1)
        while sum(region.quantities) > 0:
            for shape in shapes:
                if region.quantities[shape.index] > 0:
                    break

            while region.quantities[shape.index] > 0:
                is_inserted = try_insert(point, region, shape)
                if is_inserted:
                    region.quantities[shape.index] -= 1
                elif has_next(point, region):
                    point = next(point, region)
                else:
                    break
            if not has_next(point, region):
                break

        if sum(region.quantities) <= 0:
            answer += 1

        region.print()
        print("------------------------------------")

    return answer


def part_two(input: str):
    return "-"
