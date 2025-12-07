import math


def part_one(input: str):
    lines = input.strip().split("\n")
    operators = lines[-1].split()

    results = [1 if o == "*" else 0 for o in operators]
    for line in lines[:-1]:
        for idx, value_str in enumerate(line.split()):
            value = int(value_str)
            operator = operators[idx]
            if operator == "*":
                results[idx] *= value
            else:
                results[idx] += value

    return sum(results)


def part_two(input: str):
    lines = input.split("\n")

    rows = len(lines)
    cols = len(lines[0])

    answer = 0

    values = []
    value = []
    for col in range(cols - 1, -1, -1):
        for row in range(rows):
            v_str = lines[row][col].strip()

            if len(v_str) > 0:
                end = v_str[-1]
                if end == "*" or end == "+":
                    n = int("".join(value))
                    values.append(n)
                    if end == "*":
                        answer += math.prod(values)
                    else:
                        answer += sum(values)
                    values = []
                    value = []
                else:
                    value.append(v_str)

        if len(value) > 0:
            values.append(int("".join(value)))
            value = []

    return answer
