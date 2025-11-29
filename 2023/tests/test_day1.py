from aoc_service import parse_example
from solutions import day1

example_input = "inputs\\day1example.txt"


def test_day1example():
    examples = parse_example(1)

    for idx, example in enumerate(examples):
        part = idx + 1
        input = example.input_data
        expected_answer_a = example.answer_a
        expected_answer_b = example.answer_b

        actual_answer_a, actual_answer_b = day1.solution(input)

        if part == 1:
            assert expected_answer_a == actual_answer_a

        if part == 2:
            assert expected_answer_b == actual_answer_b

    assert len(examples) > 0
