from aoc_service import parse_example
from solutions import day12

example_input = "inputs\\day12example.txt"


def test_day12part_one():
    print("\nRunning test_day12part_one...\n\n")
    examples = parse_example(12)

    for example in examples:
        input = example.input_data
        expected_answer_a = example.answer_a
        assert expected_answer_a == str(day12.part_one(input))


def test_day12part_two():
    print("\nRunning test_day12part_two...\n\n")
    examples = parse_example(12)

    for example in examples:
        input = example.input_data
        expected_answer_b = example.answer_b
        assert expected_answer_b == str(day12.part_two(input))


def test_day12custom():
    print("\nRunning test_day12custom...\n\n")
    input = ""

    actual = ""
    # actual = day12.part_one(input.strip())
    # actual = day12.part_two(input.strip())

    expected = ""
    assert expected == actual