from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    row: int
    col: int

    @property
    def adjacent_points(self):
        N = Point(self.row - 1, self.col)
        E = Point(self.row, self.col + 1)
        W = Point(self.row, self.col - 1)
        S = Point(self.row + 1, self.col)
        NE = Point(self.row - 1, self.col + 1)
        NW = Point(self.row - 1, self.col - 1)
        SE = Point(self.row + 1, self.col + 1)
        SW = Point(self.row + 1, self.col - 1)

        return [
            N,
            E,
            W,
            S,
            NE,
            NW,
            SE,
            SW,
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
            adjacent_rolls_count = len(
                [n for n in point.adjacent_points if n in grid and grid[n] == "@"]
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
    answer = 0
    for point in grid:
        if grid[point] == "@":
            adjacent_rolls_count = len(
                [n for n in point.adjacent_points if n in grid and grid[n] == "@"]
            )
            if adjacent_rolls_count < 4:
                answer += 1
                grid[point] = "."
    return answer
