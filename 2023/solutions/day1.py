import re


def part_one(input):
    answer = 0
    for line in input.strip().split("\n"):
        digits = re.findall(r"\d", line)
        str_value = "".join((digits[0], digits[-1]))
        answer += int(str_value)
    return answer


def part_two(input):
    answer = 0
    for line in input.strip().split("\n"):
        digits = re.findall(
            r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line
        )

        d1 = parse_d(digits[0])
        d2 = parse_d(digits[-1])
        answer += d1 * 10 + d2
    return answer


VALUE_MAP = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def parse_d(d_str):
    return VALUE_MAP.index(d_str) if d_str in VALUE_MAP else int(d_str)
