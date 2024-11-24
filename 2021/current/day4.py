import math
import re
from collections import Counter
from dataclasses import dataclass, field
from functools import reduce
from pprint import pprint

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

logger_init()
logger_enable(log, "day4")

DAY = 4

locations = get_locations(f"day{DAY}")


# content = read_input(locations.example_file)
content = read_input(locations.input_file)

cl = content.split("\n")
# cl = cl[3:-4]


def part1(input):
    drawings = [int(i) for i in input[0].split(",")]
    boards = input[1:]
    bingo_boards = []
    board_marks = []
    for line in boards:
        if line == "":
            bingo_boards.append([])
            board_marks.append([])
        else:
            pos = len(bingo_boards) - 1
            row = ints(line)[0]
            bingo_boards[pos].append(row)
            board_marks[pos].append([0 for _ in row])

    line_length = len(bingo_boards[0][0])
    print("length", line_length)
    for drawn, i in zip(drawings, range(len(drawings))):
        for board, marked_board in zip(bingo_boards, board_marks):
            for row in range(len(board)):
                for col in range(len(board[row])):
                    board_value = board[row][col]
                    if board_value == drawn:
                        marked_board[row][col] = 1
        if i >= line_length - 1:

            def sum_unmarked_values(values, markings):
                sum = 0
                for vals, marks in zip(values, markings):
                    for val, mark in zip(vals, marks):
                        if mark == 0:
                            sum += val
                return sum

            # check for winning boards
            for board, marked_board in zip(bingo_boards, board_marks):
                for h in marked_board:
                    if sum(h) == line_length:
                        _sum = sum_unmarked_values(board, marked_board)
                        score = _sum * drawn
                        return score
                for col in range(len(marked_board[0])):
                    v = [marked_board[_i][col] for _i in range(len(marked_board[col]))]
                    if sum(v) == line_length:
                        _sum = sum_unmarked_values(board, marked_board)
                        score = _sum * drawn
                        return score

    return -1


def part2(input):
    drawings = [int(i) for i in input[0].split(",")]
    boards = input[1:]
    bingo_boards = []
    board_marks = []
    for line in boards:
        if line == "":
            bingo_boards.append([])
            board_marks.append([])
        else:
            pos = len(bingo_boards) - 1
            row = ints(line)[0]
            bingo_boards[pos].append(row)
            board_marks[pos].append([0 for _ in row])

    line_length = len(bingo_boards[0][0])
    print("length", line_length)
    last_winning_boards = None
    last_winning_drawn_value = -1
    for drawn, i in zip(drawings, range(len(drawings))):
        for board, marked_board in zip(bingo_boards, board_marks):
            for row in range(len(board)):
                for col in range(len(board[row])):
                    board_value = board[row][col]
                    if board_value == drawn:
                        marked_board[row][col] = 1
        if i >= line_length - 1:
            # check for winning boards
            for board, marked_board in zip(bingo_boards, board_marks):
                won = False
                for h in marked_board:
                    if sum(h) == line_length:
                        won = True
                for col in range(len(marked_board[0])):
                    v = [marked_board[_i][col] for _i in range(len(marked_board[col]))]
                    if sum(v) == line_length:
                        won = True
                if won:
                    last_winning_drawn_value = drawn
                    last_winning_boards = board, marked_board
                    # remove the winning board from the bingo_boards and board_marks
                    bingo_boards.remove(board)
                    board_marks.remove(marked_board)

        def sum_unmarked_values(values: list[list[int]], markings) -> int:
            sum = 0
            for vals, marks in zip(values, markings):
                for val, mark in zip(vals, marks):
                    if mark == 0:
                        sum += val
            return sum

    _sum = sum_unmarked_values(last_winning_boards[0], last_winning_boards[1])
    return _sum * last_winning_drawn_value


input = cl
print("part1", part1(input))
print("part2", part2(input))
