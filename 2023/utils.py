import sys
from dataclasses import dataclass
from functools import cached_property


@dataclass
class Point:
    row: int
    col: int

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Point):
            return self.row == value.row and self.col == value.col
        return False

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
            self.N,
            self.E,
            self.W,
            self.S,
            self.NE,
            self.NW,
            self.SE,
            self.SW,
        ]

    @property
    def adjacent_points_async(self):
        ap_str = ["N", "E", "W", "S", "NE", "NW", "SE", "SW"]
        for p in ap_str:
            yield self.__getattribute__(p)


def print_grid(point_value_dict: {Point: object}):
    start = Point(0, 0)
    keys = [_ for _ in point_value_dict.keys()]
    p = start

    while p in keys:
        sys.stdout.write(point_value_dict[p])
        sys.stdout.flush()
        p = p.E
        if p not in keys:
            sys.stdout.write("\n")
            p = p.S
            p.col = 0
    
