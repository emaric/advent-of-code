from dataclasses import dataclass
from functools import cached_property


@dataclass
class Point:
    row: int
    col: int
    _ap = None

    def __eq__(self, point: Point):
        return self.row == point.row and self.col == point.col

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

    @property
    def adjacent_points(self):
        if self._ap is None:
            self._ap = [
                self.N,
                self.E,
                self.W,
                self.S,
                self.NE,
                self.NW,
                self.SE,
                self.SW,
            ]

        return self._ap

    @property
    def adjacent_points_async(self):
        ap_str = ["N", "E", "W", "S", "NE", "NW", "SE", "SW"]
        for p in ap_str:
            yield self.__getattribute__(p)


def to_grid(input: str):
    grid = {}
    for row, line in enumerate(input.split("\n")):
        for col, val in enumerate(line):
            if val == "@":
                point = Point(row, col)
                grid[point] = val
    return grid


def part_one(input: str):
    answer = 0

    grid = to_grid(input)
    for point in grid:
        adjacent_rolls_count = 0
        for adjacent_point in point.adjacent_points_async:
            if adjacent_point in grid:
                adjacent_rolls_count += 1
            if adjacent_rolls_count >= 4:
                break

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


def part_two_with_grid(grid: dict):
    answer = 0
    keys = [p for p in grid.keys()]
    for point in keys:
        adjacent_rolls_count = 0
        for adjacent_point in point.adjacent_points:
            if adjacent_point in grid:
                adjacent_rolls_count += 1
            if adjacent_rolls_count >= 4:
                break

        if adjacent_rolls_count < 4:
            answer += 1
            del grid[point]

    return answer
