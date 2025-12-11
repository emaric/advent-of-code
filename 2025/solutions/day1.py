import math


def part_one(input):
    answer = 0
    dial = 50
    for line in input.strip().split("\n"):
        dir, turns = line[0], int(line[1:])
        turns = -turns if dir == "L" else turns
        dial += turns
        if dial % 100 == 0:
            answer += 1
    return answer


def part_two(input):
    answer = 0
    dial = 50
    for line in input.strip().split("\n"):
        dir, turns = line[0], int(line[1:])

        answer += math.trunc(turns / 100)
        turns = turns % 100

        turns = -turns if dir == "L" else turns

        after_turn = dial + turns
        after_turn = after_turn % 100

        if after_turn < dial and dir == "R":
            answer += 1

        if dir == "L" and dial > 0:
            if after_turn > dial or after_turn == 0:
                answer += 1

        dial = after_turn

    return answer
