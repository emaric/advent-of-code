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
        str_value = "".join((digits[0], digits[-1]))

        str_value = str_value.replace("one", "1")
        str_value = str_value.replace("two", "2")
        str_value = str_value.replace("three", "3")
        str_value = str_value.replace("four", "4")
        str_value = str_value.replace("five", "5")
        str_value = str_value.replace("six", "6")
        str_value = str_value.replace("seven", "7")
        str_value = str_value.replace("eight", "8")
        str_value = str_value.replace("nine", "9")
        answer += int(str_value)
    return answer


def main(part=1):
    with open("inputs\\day1.txt", "r") as f:
        input = f.read()

    if part == 1:
        return part_one(input)
    elif part == 2:
        return part_two(input)
    else:
        raise Exception("Not implemented.")


if __name__ == "__main__":
    main()
