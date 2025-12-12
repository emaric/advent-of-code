from aoc_service import parse_example
from solutions import day9

example_input = "inputs\\day9example.txt"


def test_day9part_one():
    print("\nRunning test_day9part_one...\n\n")
    examples = parse_example(9)

    for example in examples:
        input = example.input_data
        expected_answer_a = example.answer_a
        assert expected_answer_a == str(day9.part_one(input))


def test_day9part_two():
    print("\nRunning test_day9part_two...\n\n")
    examples = parse_example(9)

    for example in examples:
        input = example.input_data
        expected_answer_b = example.answer_b
        assert expected_answer_b == str(day9.part_two(input))


def test_day9custom():
    input = ""

    actual = ""
    # actual = day9.part_one(input.strip())
    # actual = day9.part_two(input.strip())

    expected = ""
    assert expected == actual
