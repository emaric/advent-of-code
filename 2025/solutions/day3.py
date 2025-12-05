def get_next_sub_array(arr, remaining_right_length, orig_arr=None):
    max_value = max(arr)
    max_idx = arr.index(max_value)
    if orig_arr is None:
        orig_arr = [n for n in arr]

    right_arr = orig_arr[max_idx + 1 :]
    if len(right_arr) >= remaining_right_length - 1:
        return max_value, right_arr
    else:
        left_arr = orig_arr[:max_idx]
        if len(left_arr) <= 0:
            max_left = max_value
        else:
            max_left, _ = get_next_sub_array(left_arr, remaining_right_length, orig_arr)
        max_left_idx = orig_arr.index(max_left)
        remaining_arr = orig_arr[max_left_idx + 1 :]
        return max_left, remaining_arr


def calc_value(arr):
    v = 0
    for idx, d in enumerate(arr):
        v += d * (10 ** (12 - (idx + 1)))
    return v


def part_one(input: str):
    answer = 0
    for line in input.strip().split("\n"):
        int_array = [int(n) for n in line]
        first = max(int_array)
        first_idx = int_array.index(first)

        left_arr = int_array[:first_idx]
        right_arr = int_array[first_idx + 1 :]
        if len(right_arr) <= 0:
            second = max(left_arr)
            answer += second * 10 + first
        else:
            second = max(right_arr)
            answer += first * 10 + second

    return answer


def part_two(input: str):
    answer = 0
    for line in input.strip().split("\n"):
        int_array = [int(n) for n in line]

        value_arr = []

        sub_arr = int_array
        for r in range(12, 0, -1):
            max_value, sub_arr = get_next_sub_array(sub_arr, r)
            value_arr.append(max_value)
        answer += calc_value(value_arr)

    return answer
