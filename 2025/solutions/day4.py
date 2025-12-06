from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Point:
    row: int
    col: int
    getter: callable = None
    setter: callable = None

    @property
    def N(self):
        return Point(self.row - 1, self.col, self.getter, self.setter)

    @property
    def E(self):
        return Point(self.row, self.col + 1, self.getter, self.setter)

    @property
    def W(self):
        return Point(self.row, self.col - 1, self.getter, self.setter)

    @property
    def S(self):
        return Point(self.row + 1, self.col, self.getter, self.setter)

    @property
    def NE(self):
        return Point(self.row - 1, self.col + 1, self.getter, self.setter)

    @property
    def NW(self):
        return Point(self.row - 1, self.col - 1, self.getter, self.setter)

    @property
    def SE(self):
        return Point(self.row + 1, self.col + 1, self.getter, self.setter)

    @property
    def SW(self):
        return Point(self.row + 1, self.col - 1, self.getter, self.setter)

    @property
    def adjacent_points(self):
        adjacent_points = [
            self.N,
            self.E,
            self.W,
            self.S,
            self.NE,
            self.NW,
            self.SE,
            self.SW,
        ]
        return [p for p in adjacent_points if p is not None]

    @property
    def value(self):
        val = self.getter(self.row, self.col)
        return val

    def __setattr__(self, name, value):
        if self.setter is not None and name == "value":
            self.setter(self.row, self.col, value)
        else:
            super().__setattr__(name, value)


@dataclass
class Grid:
    grid_array: list[list[Any]]

    def _is_valid_pos(self, row, col):
        if len(self.grid_array) <= 0:
            return False
        if len(self.grid_array[0]) <= 0:
            return False
        return (
            row >= 0
            and row < len(self.grid_array)
            and col >= 0
            and col < len(self.grid_array[0])
        )

    def get_value(self, row, col):
        if self._is_valid_pos(row, col):
            return self.grid_array[row][col]

    def set_value(self, row, col, value):
        if self._is_valid_pos(row, col):
            self.grid_array[row][col] = value

    def __iter__(self):
        cols = len(self.grid_array[0])
        for row in range(len(self.grid_array)):
            for col in range(cols):
                point = Point(row, col, self.get_value, self.set_value)
                yield point

    def __str__(self):
        str_v = []
        for row in self.grid_array:
            str_v.append(str(row))

        return "\n".join(str_v)


def to_grid(input: str):
    grid_array = []
    for line in input.strip().split("\n"):
        grid_array.append([_ for _ in line])
    grid = Grid(grid_array)
    return grid


def part_one(input: str):
    answer = 0

    grid = to_grid(input)
    for point in grid:
        if point.value == "@":
            adjacent_rolls_count = len(
                [n for n in point.adjacent_points if n.value == "@"]
            )
            if adjacent_rolls_count < 4:
                answer += 1

    return answer


def part_two(input: str):
    answer = 0

    grid = to_grid(input)

    found = part_two_with_grid(grid)
    answer += found
    while found > 0:
        found = part_two_with_grid(grid)
        answer += found
    return answer


def part_two_with_grid(grid):
    valid_points = []
    for point in grid:
        if point.value == "@":
            adjacent_rolls_count = len(
                [n for n in point.adjacent_points if n.value == "@"]
            )
            if adjacent_rolls_count < 4:
                valid_points.append(point)
    for point in valid_points:
        point.value = "."
    return len(valid_points)
