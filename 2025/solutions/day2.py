import math


def sum_n_repeated_twice(min_str, max_str):
    n_values = set()
    min_int = int(min_str)
    max_int = int(max_str)
    for length in range(max(len(min_str), 2), len(max_str) + 1):
        if length % 2 != 0:
            continue
        min_by_length = 10 ** (length - 1)
        min_by_length = max(min_int, min_by_length)
        min_by_length_str = str(min_by_length)
        max_by_length = min(max_int, 10 ** (length) - 1)
        max_by_length_str = str(max_by_length)
        factor = int(length / 2)
        z = int(length / factor)
        left = min_by_length_str[:factor]
        n_str = "".join([left] * z)

        min_left_str = min_by_length_str[:factor]
        max_left_str = max_by_length_str[:factor]
        for n_by_length in range(int(min_left_str), int(max_left_str) + 1):
            left = str(n_by_length)[:factor]
            n_str = "".join([left] * z)
            n_values.add(n_str)

    n_values = [int(n) for n in n_values]
    n_values = [n for n in n_values if n >= min_int and n <= max_int]
    return sum(n_values)


def sum_n_atleast_twice(min_str, max_str):
    n_values = set()
    min_int = int(min_str)
    max_int = int(max_str)
    max_length = math.trunc(len(max_str) / 2)
    for length in range(max(len(min_str), 2), len(max_str) + 1):
        min_by_length = 10 ** (length - 1)
        min_by_length = max(min_int, min_by_length)
        min_by_length_str = str(min_by_length)
        max_by_length = min(max_int, 10 ** (length) - 1)
        max_by_length_str = str(max_by_length)
        for factor in range(1, max_length + 1):
            if length % factor == 0:
                z = int(length / factor)
                left = min_by_length_str[:factor]
                n_str = "".join([left] * z)

                min_left_str = min_by_length_str[:factor]
                max_left_str = max_by_length_str[:factor]
                for n_by_length in range(int(min_left_str), int(max_left_str) + 1):
                    left = str(n_by_length)[:factor]
                    n_str = "".join([left] * z)
                    n_values.add(n_str)

    n_values = [int(n) for n in n_values]
    n_values = [n for n in n_values if n >= min_int and n <= max_int]
    return sum(n_values)


def part_one(input):
    answer = 0
    for line in input.split(","):
        first, last = line.split("-")
        answer += sum_n_repeated_twice(first, last)
    return answer


def part_two(input):
    answer = 0
    for line in input.split(","):
        first, last = line.strip().split("-")
        answer += sum_n_atleast_twice(first, last)
    return answer
