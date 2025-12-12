import math
from dataclasses import dataclass
from itertools import combinations
from math import sqrt


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int

    def __eq__(self, other: Point) -> bool:  # type: ignore
        return self.x == other.x and self.y == other.y and self.z == other.z


def distance(p: Point, q: Point):
    return sqrt((p.x - q.x) ** 2 + (p.y - q.y) ** 2 + (p.z - q.z) ** 2)


@dataclass
class Pair:
    p: Point
    q: Point
    distance: float

    def __eq__(self, other: Pair) -> bool:  # type: ignore
        return (self.p == other.q and self.q == other.p) or (
            self.p == other.p and self.q == other.q
        )

    def __lt__(self, other: Pair):
        return self.distance < other.distance

    def __le__(self, other: Pair):
        return self.distance <= other.distance

    def __gt__(self, other: Pair):
        return self.distance > other.distance

    def __ge__(self, other: Pair):
        return self.distance >= other.distance


def part_one(input: str, requirement=1000):
    lines = input.strip().split("\n")

    points: list[Point] = []
    for line in lines:
        x, y, z = line.split(",")
        points.append(Point(int(x), int(y), int(z)))

    results: list[Pair] = []

    for p, q in combinations(points, 2):
        pair = Pair(p, q, distance(p, q))

        results.append(pair)

    results.sort()
    results = results[:requirement]

    result_sets = [set((p.q, p.p)) for p in results]

    for x in range(len(result_sets)):
        _set = result_sets.pop(0)
        flag = False
        for y in range(len(result_sets)):
            other_set = result_sets.pop(0)
            if len(_set.intersection(other_set)) > 0:
                new_set = _set.union(other_set)
                result_sets.append(new_set)
                flag = True
            else:
                result_sets.append(other_set)

        if not flag:
            result_sets.append(_set)

    answer = math.prod(sorted([len(s) for s in result_sets])[-3:])
    return answer


def part_two(input: str):
    lines = input.strip().split("\n")

    points: list[Point] = []
    for line in lines:
        x, y, z = line.split(",")
        points.append(Point(int(x), int(y), int(z)))

    results: list[Pair] = []

    for p, q in combinations(points, 2):
        pair = Pair(p, q, distance(p, q))

        results.append(pair)

    results.sort()

    len_points = len(points)

    result_sets = []
    while True:
        last_pair = results.pop(0)
        result_sets.append(set((last_pair.p, last_pair.q)))

        for x in range(len(result_sets)):
            _set = result_sets.pop(0)
            flag = False
            for y in range(len(result_sets)):
                other_set = result_sets.pop(0)
                if len(_set.intersection(other_set)) > 0:
                    new_set = _set.union(other_set)
                    if len(new_set) == len_points:
                        return last_pair.q.x * last_pair.p.x
                    result_sets.append(new_set)
                    flag = True
                else:
                    result_sets.append(other_set)

            if not flag:
                result_sets.append(_set)
