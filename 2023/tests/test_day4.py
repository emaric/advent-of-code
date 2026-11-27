from aoc_service import parse_example
from solutions import day4

example_input = "inputs\\day4example.txt"


def test_day4part_one():
    print("\nRunning test_day4part_one...\n\n")
    examples = parse_example(4)

    for example in examples:
        input = example.input_data
        expected_answer_a = example.answer_a
        assert expected_answer_a == str(day4.part_one(input))


def test_day4part_two():
    print("\nRunning test_day4part_two...\n\n")
    examples = parse_example(4)

    for example in examples:
        input = example.input_data
        expected_answer_b = example.answer_b
        assert expected_answer_b == str(day4.part_two(input))


def test_day4custom():
    print("\nRunning test_day4custom...\n\n")
    input = ""

    actual = ""
    # actual = day4.part_one(input.strip())
    # actual = day4.part_two(input.strip())

    expected = ""
    assert expected == actual