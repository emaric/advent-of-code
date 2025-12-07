def part_one(input: str):
    TRACKER = []
    answer = 0

    is_range = True
    for line in input.split("\n"):
        if len(line) > 0:
            if is_range:
                TRACKER.append([int(v) for v in line.split("-")])
            else:
                id = int(line)
                for min, max in TRACKER:
                    if id >= min and id <= max:
                        answer += 1
                        break
        else:
            is_range = False

    return answer


def part_two(input: str):
    TRACKER = []

    for line in input.split("\n"):
        if len(line) > 0:
            TRACKER.append([int(v) for v in line.split("-")])
        else:
            break

    TRACKER = sorted(TRACKER)

    answer = 0
    end = 0
    for cur_start, cur_end in TRACKER:
        fresh = cur_end + 1 - cur_start
        if end > cur_end:
            continue
        if end >= cur_start:
            fresh = cur_end - end
        answer += fresh
        end = max(cur_end, end)

    return answer
