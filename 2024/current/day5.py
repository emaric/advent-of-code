import math
import re
from collections import Counter
from dataclasses import dataclass, field
from functools import cmp_to_key, reduce
from pprint import pprint

from shared.decorators import timer
from shared.helpers import Grid, Point, Vectors, get_locations, read_input
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

DAY = 5

logger_init()
logger_enable(log, f"day{DAY}")

locations = get_locations(f"day{DAY}")


# content = read_input(locations.example_file)
content = read_input(locations.input_file)

cl = content.split("\n")
# cl = cl[3:-4]


@timer
def part1(input):
    mid_pages_sum = 0
    rules, updates = input

    def _is_correctly_ordered(_rules, _pages):
        relevant_rules = []
        for page in _pages:
            relevant_rules.append(_rules[page])

        # print(pages, "relevant rules:", relevant_rules)
        for rules in relevant_rules:
            for x, y in rules:
                if x in pages and y in pages:
                    x_index = pages.index(x)
                    y_index = pages.index(y)
                    if x_index > y_index:
                        return False
        return True

    for pages in updates:
        if _is_correctly_ordered(rules, pages):
            mid = pages[int(len(pages) / 2)]
            mid_pages_sum += mid

    return mid_pages_sum


def _sort(arr, comparator):
    if len(arr) > 1:
        if len(arr) > 2:
            mid_index = int(len(arr) / 2) + 1
            left = _sort(arr[:mid_index], comparator)
            right = _sort(arr[mid_index:], comparator)
        else:
            left = [arr[0]]
            right = [arr[1]]
        merged = []

        _r = 0
        _l = 0

        while _l < len(left) and _r < len(right):
            if comparator(left[_l], right[_r]):
                merged.append(left[_l])
                _l += 1
            else:
                merged.append(right[_r])
                _r += 1

        for i in range(_l, len(left)):
            merged.append(left[i])

        for i in range(_r, len(right)):
            merged.append(right[i])

        return merged

    else:
        return arr


@timer
def part2(input):
    mid_pages_sum = 0
    rules, updates = input

    def _is_correctly_ordered(_rules, _pages):
        relevant_rules = []
        for page in _pages:
            relevant_rules.append(_rules[page])

        # print(pages, "relevant rules:", relevant_rules)
        for rules in relevant_rules:
            for x, y in rules:
                if x in pages and y in pages:
                    x_index = pages.index(x)
                    y_index = pages.index(y)
                    if x_index > y_index:
                        return False
        return True

    def _is_printed_before_target(page, target):
        for x, y in rules[page]:
            if x == target and y == page:
                return False
        return True

    for pages in updates:
        if not _is_correctly_ordered(rules, pages):
            corrected = _sort(pages, _is_printed_before_target)
            mid_pages_sum += corrected[int(len(corrected) / 2)]

    return mid_pages_sum


input = cl
rules = input[: input.index("")]
rules = [list(map(int, rule.split("|"))) for rule in rules]

rules_dict = {}
for x, y in rules:
    if x not in rules_dict:
        rules_dict[x] = []
    if y not in rules_dict:
        rules_dict[y] = []
    rules_dict[x].append((x, y))
    rules_dict[y].append((x, y))

rules = rules_dict
updates = input[input.index("") + 1 :]
updates = [list(map(int, update.split(","))) for update in updates]
input = [rules, updates]
print("part1", part1(input))

# failed: 4917 -> answer is too low
# failed: 4946 -> answer is too low
print("part2", part2(input))
