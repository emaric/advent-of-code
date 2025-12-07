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

    TRACKER = sorted(TRACKER, key=lambda x: x[-1])

    answer = 0
    for idx, (cur_start, cur_end) in enumerate(TRACKER):
        for start, _ in TRACKER[idx + 1 :]:
            if cur_end < start:
                continue
            elif cur_end > start:
                cur_end = start - 1
                if cur_end <= 0 or cur_end <= cur_start:
                    break
            else:
                cur_end -= 1
                if cur_end <= 0 or cur_end <= cur_start:
                    break

        fresh_count = cur_end + 1 - cur_start
        fresh_count = max(0, fresh_count)
        answer += fresh_count

    return answer
