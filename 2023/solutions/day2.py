def parse_line(line: str):
    game_info, cubes = line.split(":")
    id = game_info.strip().split(" ")[-1]
    return int(id), cubes.strip().split(";")


def is_valid(cubes: [str]):
    red = 12
    green = 13
    blue = 14
    for draw in cubes:
        for colors in draw.split(","):
            n_str, color = colors.strip().split(" ")
            n = int(n_str)
            if color == "red" and n > red:
                return False
            elif color == "green" and n > green:
                return False
            elif color == "blue" and n > blue:
                return False
    return True


def calc_power(cubes: [str]):
    red = 1
    green = 1
    blue = 1
    for draw in cubes:
        for colors in draw.split(","):
            n_str, color = colors.strip().split(" ")
            n = int(n_str)
            if color == "red" and n > red:
                red = max(red, n)
            elif color == "green" and n > green:
                green = max(green, n)
            elif color == "blue" and n > blue:
                blue = max(blue, n)
    return red * green * blue


def part_one(input: str):
    ans = 0
    for line in input.strip().split("\n"):
        id, cubes = parse_line(line)
        if is_valid(cubes):
            ans += id
    return ans


def part_two(input: str):
    ans = 0
    for line in input.strip().split("\n"):
        id, cubes = parse_line(line)
        ans += calc_power(cubes)
    return ans


if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip()
    print(part_one(data))
    print(part_two(data))
