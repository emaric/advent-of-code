from aoc_service import parse_example
from solutions import day10

example_input = "inputs\\day10example.txt"


def test_day10part_one():
    print("\nRunning test_day10part_one...\n\n")
    examples = parse_example(10)

    for example in examples:
        input = example.input_data
        expected_answer_a = example.answer_a
        assert expected_answer_a == str(day10.part_one(input))


def test_day10part_two():
    print("\nRunning test_day10part_two...\n\n")
    examples = parse_example(10)

    for example in examples:
        input = example.input_data
        expected_answer_b = example.answer_b
        assert expected_answer_b == str(day10.part_two(input))


def test_day10custom():
    print("\nRunning test_day10custom...\n\n")
    input = ""

    actual = ""
    # actual = day10.part_one(input.strip())
    # actual = day10.part_two(input.strip())

    expected = ""
    assert expected == actual