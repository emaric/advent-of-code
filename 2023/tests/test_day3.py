from aoc_service import parse_example
from solutions import day3

example_input = "inputs\\day3example.txt"


def test_day3part_one():
    print("\nRunning test_day3part_one...\n\n")
    examples = parse_example(3)

    for example in examples:
        input = example.input_data
        expected_answer_a = example.answer_a
        assert expected_answer_a == str(day3.part_one(input))


def test_day3part_two():
    print("\nRunning test_day3part_two...\n\n")
    examples = parse_example(3)

    for example in examples:
        input = example.input_data
        expected_answer_b = example.answer_b
        assert expected_answer_b == str(day3.part_two(input))


def test_day3custom():
    print("\nRunning test_day3custom...\n\n")
    input = ""

    actual = ""
    # actual = day3.part_one(input.strip())
    # actual = day3.part_two(input.strip())

    expected = ""
    assert expected == actual