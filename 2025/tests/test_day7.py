from aoc_service import parse_example
from solutions import day7

example_input = "inputs\\day7example.txt"


def test_day7example():
    examples = parse_example(7)

    for example in examples:
        input = example.input_data
        expected_answer_a = example.answer_a
        expected_answer_b = example.answer_b

        assert expected_answer_a == str(day7.part_one(input))
        assert expected_answer_b == str(day7.part_two(input))

    assert len(examples) > 0


def test_day7custom():
    input = ""

    actual = ""
    # actual = day7.part_one(input.strip())
    # actual = day7.part_two(input.strip())

    expected = ""
    assert expected == actual