from aoc_service import parse_example
from solutions import day1

example_input = "inputs\\day1example.txt"


def test_day1part_one():
    print("\nRunning test_day1part_one...\n\n")
    examples = parse_example(1)

    for example in examples:
        input = example.input_data
        expected_answer_a = example.answer_a
        assert expected_answer_a == str(day1.part_one(input))


def test_day1part_two():
    print("\nRunning test_day1part_two...\n\n")
    examples = parse_example(1)

    for example in examples:
        input = example.input_data
        expected_answer_b = example.answer_b
        assert expected_answer_b == str(day1.part_two(input))


def test_day1custom():
    print("\nRunning test_day1custom...\n\n")
    input = ""

    actual = ""
    # actual = day1.part_one(input.strip())
    # actual = day1.part_two(input.strip())

    expected = ""
    assert expected == actual