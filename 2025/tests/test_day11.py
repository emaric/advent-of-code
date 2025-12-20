from aoc_service import parse_example
from solutions import day11

example_input = "inputs\\day11example.txt"


def test_day11part_one():
    print("\nRunning test_day11part_one...\n\n")
    examples = parse_example(11)

    for example in examples[:-1]:
        input = example.input_data
        expected_answer_a = example.answer_a
        assert expected_answer_a == str(day11.part_one(input))


def test_day11part_two():
    print("\nRunning test_day11part_two...\n\n")
    examples = parse_example(11)

    for example in examples[1:]:
        input = example.input_data
        expected_answer_b = example.answer_b
        assert expected_answer_b == str(day11.part_two(input))
