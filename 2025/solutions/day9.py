from dataclasses import dataclass
from itertools import combinations


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


@dataclass
class Rectangle:
    top_left: Point
    top_right: Point
    bottom_left: Point
    bottom_right: Point

    top_red: Point
    bottom_red: Point

    def __init__(self, a: Point, b: Point):
        top_row = min(a.row, b.row)
        left_col = min(a.col, b.col)

        top = a if a.row == top_row else b
        bottom = a if top == b else b

        self.top_left = Point(top.row, left_col)
        self.top_right = Point(top_row, max(a.col, b.col))
        self.bottom_left = Point(bottom.row, left_col)
        self.bottom_right = Point(bottom.row, max(a.col, b.col))

        self.top_red = top
        self.bottom_red = bottom


def calc_area(a: Point, b: Point):
    rows = [a.row, b.row]
    cols = [a.col, b.col]
    w = 1 + max(cols) - min(cols)
    h = 1 + max(rows) - min(rows)
    area = w * h
    return area


def print_grid(points, greens=[], area=[]):
    rows = max([p.row for p in points]) + 3
    cols = max([p.col for p in points]) + 3

    def char(row, col):
        p = Point(row, col)
        if p in points:
            return "#"
        if p in greens:
            return "X"
        if p in area:
            return "O"
        return "."

    for row in range(rows):
        print("".join([char(row, col) for col in range(cols)]))


def is_left_fully_covered(rect, v_lines):
    col_left = rect.top_left.col
    rect_top = rect.top_left.row
    rect_bottom = rect.bottom_left.row

    segments = []
    for line in v_lines:
        p1, p2 = line
        if p1.col <= col_left:
            if p1.row <= rect_top and rect_bottom <= p2.row:
                return True
            if rect_top <= p1.row <= rect_bottom:
                segments.append(line)
            elif rect_top <= p2.row <= rect_bottom:
                segments.append(line)

    if len(segments) <= 1:
        return False

    segments = sorted(segments, key=lambda x: (x[0].row, x[1].row))
    covered_bottom = segments[0][0].row
    if covered_bottom > rect_top:
        return False
    for line in segments:
        p1, p2 = line
        if p1.row > covered_bottom:
            return False
        covered_bottom = max(p2.row, covered_bottom)

    if covered_bottom < rect_bottom:
        return False

    return True


def is_right_fully_covered(rect, v_lines):
    col_right = rect.top_right.col
    rect_top = rect.top_right.row
    rect_bottom = rect.bottom_right.row

    segments = []
    for line in v_lines:
        p1, p2 = line
        if p1.col >= col_right:
            if p1.row <= rect_top and rect_bottom <= p2.row:
                return True
            if rect_top <= p1.row <= rect_bottom:
                segments.append(line)
            elif rect_top <= p2.row <= rect_bottom:
                segments.append(line)

    if len(segments) <= 1:
        return False

    segments = sorted(segments, key=lambda x: (x[0].row, x[1].row))
    covered_bottom = segments[0][0].row
    if covered_bottom > rect_top:
        return False
    for line in segments:
        p1, p2 = line
        if p1.row > covered_bottom:
            return False
        covered_bottom = max(p2.row, covered_bottom)

    if covered_bottom < rect_bottom:
        return False

    return True


def is_bottom_fully_covered(rect, h_lines):
    row_bottom = rect.bottom_left.row
    rect_left = rect.bottom_left.col
    rect_right = rect.bottom_right.col

    segments = []
    for line in h_lines:
        p1, p2 = line
        if p1.row >= row_bottom:
            if p1.col <= rect_left and rect_right <= p2.col:
                return True
            if rect_left <= p1.col <= rect_right:
                segments.append(line)
            elif rect_left <= p2.col <= rect_right:
                segments.append(line)

    if len(segments) <= 1:
        return False

    segments = sorted(segments, key=lambda x: (x[0].col, x[1].col))
    covered_right = segments[0][0].col
    if covered_right > rect_left:
        return False
    for line in segments:
        p1, p2 = line
        if p1.col > covered_right:
            return False
        covered_right = max(p2.col, covered_right)

    if covered_right < rect_right:
        return False

    return True


def is_top_fully_covered(rect, h_lines):
    row_top = rect.top_left.row
    rect_left = rect.top_left.col
    rect_right = rect.top_right.col

    segments = []
    for line in h_lines:
        p1, p2 = line
        if p1.row <= row_top:
            if p1.col <= rect_left and rect_right <= p2.col:
                return True
            if rect_left <= p1.col <= rect_right:
                segments.append(line)
            elif rect_left <= p2.col <= rect_right:
                segments.append(line)

    if len(segments) <= 1:
        return False

    segments = sorted(segments, key=lambda x: (x[0].col, x[1].col))
    covered_right = segments[0][0].col
    if covered_right > rect_left:
        return False
    for line in segments:
        p1, p2 = line
        if p1.col > covered_right:
            return False
        covered_right = max(p2.col, covered_right)

    if covered_right < rect_right:
        return False

    return True


def is_red_green(a: Point, b: Point, points: list[Point], v_lines, h_lines):
    rect = Rectangle(a, b)

    for p in points:
        if (
            rect.top_left.row < p.row < rect.bottom_left.row
            and rect.top_left.col < p.col < rect.top_right.col
        ):
            return False

    valid_top = is_top_fully_covered(rect, h_lines)
    if not valid_top:
        return False

    valid_bottom = is_bottom_fully_covered(rect, h_lines)
    if not valid_bottom:
        return False

    valid_right = is_right_fully_covered(rect, v_lines)
    if not valid_right:
        return False

    valid_left = is_left_fully_covered(rect, v_lines)
    if not valid_left:
        return False

    return True


def part_one(input: str):
    points = []
    for line in input.split("\n"):
        col, row = [int(_) for _ in line.split(",")]
        points.append(Point(row, col))

    answer = 0
    for a, b in combinations(points, 2):
        if a.row == b.row or a.col == b.col:
            continue
        area = calc_area(a, b)
        answer = max(area, answer)

    return answer


def part_two(input: str):
    points = []
    for line in input.split("\n"):
        col, row = [int(_) for _ in line.split(",")]
        points.append(Point(row, col))

    h_lines = []
    v_lines = []
    for start, end in zip(points, points[1:] + [points[0]]):
        if start.col == end.col:
            v_lines.append(sorted((start, end), key=lambda x: x.row))
        if start.row == end.row:
            h_lines.append(sorted((start, end), key=lambda x: x.col))

    answer = 0
    for a, b in combinations(points, 2):
        if a.row == b.row or a.col == b.col:
            continue
        area = calc_area(a, b)
        new_max = max(area, answer)
        if new_max != answer:
            if is_red_green(a, b, points, v_lines, h_lines):
                answer = new_max

    return answer
