from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    row: int
    col: int

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


def to_grid(input: str):
    grid = {}
    for row, line in enumerate(input.strip().split("\n")):
        for col in range(len(line)):
            point = Point(row, col)
            grid[point] = line[col]
    return grid


def part_one(input: str):
    answer = 0

    grid = to_grid(input)
    for point in grid.keys():
        if grid[point] == "@":
            adjacent_rolls_count = 0
            for adjacent_point in point.adjacent_points:
                if adjacent_point in grid and grid[adjacent_point] == "@":
                    adjacent_rolls_count += 1

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
    answer = 0
    for point in grid:
        if grid[point] == "@":
            adjacent_rolls_count = 0
            for adjacent_point in point.adjacent_points:
                if adjacent_point in grid and grid[adjacent_point] == "@":
                    adjacent_rolls_count += 1
            if adjacent_rolls_count < 4:
                answer += 1
                grid[point] = "."
    return answer
