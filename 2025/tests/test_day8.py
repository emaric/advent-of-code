from aoc_service import parse_example
from solutions import day8

example_input = "inputs\\day8example.txt"


def test_day8part_one():
    print("\nRunning test_day8part_one...\n\n")
    examples = parse_example(8)

    for example in examples:
        input = example.input_data
        expected_answer_a = example.answer_a
        assert expected_answer_a == str(day8.part_one(input, 10))


def test_day8part_two():
    print("\nRunning test_day8part_two...\n\n")
    examples = parse_example(8)

    for example in examples:
        input = example.input_data
        expected_answer_b = example.answer_b
        assert expected_answer_b == str(day8.part_two(input))


def test_day8custom():
    print("\nRunning test_day8custom...\n\n")
    input = ""

    actual = ""
    # actual = day8.part_one(input.strip())
    # actual = day8.part_two(input.strip())

    expected = ""
    assert expected == actual
