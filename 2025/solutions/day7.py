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


def part_one(input: str):
    answer = 0

    lines = input.split("\n")
    s_idx = lines[0].index("S")
    S = Point(0, s_idx)

    _set = set()
    _set.add(S)
    points = [_set]
    rows = len(lines) - 1
    for row in range(1, rows):
        line = lines[row]

        _set = set()
        for point in points[row - 1]:
            s = point.S
            if line[s.col] == "^":
                _set.add(s.W)
                _set.add(s.E)
                answer += 1
            else:
                _set.add(s)
        points.append(_set)

    return answer


def part_two(input: str):
    answer = 0

    lines = input.split("\n")
    s_idx = lines[0].index("S")
    S = Point(0, s_idx)

    _dict = {}

    def add_dict(p: Point, n=1):
        if p in _dict:
            _dict[p] += n
        else:
            _dict[p] = n

    _set = set()
    _set.add(S)
    add_dict(S)

    points = [_set]
    rows = len(lines) - 1
    for row in range(1, rows):
        line = lines[row]

        _set = set()
        for point in points[row - 1]:
            s = point.S
            n = _dict[point]
            if line[s.col] == "^":
                _set.add(s.W)
                _set.add(s.E)
                add_dict(s.W, n)
                add_dict(s.E, n)
            else:
                _set.add(s)
                add_dict(s, n)
        points.append(_set)

    answer = sum([_dict[p] for p in points[-1]])

    return answer
