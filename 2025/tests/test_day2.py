from aoc_service import parse_example
from solutions import day2

example_input = "inputs\\day2example.txt"


def test_day2example():
    examples = parse_example(2)

    for example in examples:
        input = example.input_data
        expected_answer_a = example.answer_a
        expected_answer_b = example.answer_b

        assert expected_answer_a == str(day2.part_one(input))
        assert expected_answer_b == str(day2.part_two(input))

    assert len(examples) > 0


def test_day2part2():
    input = "95-115"
    actual = day2.part_two(input)

    expected = "210"
    assert expected == str(actual)


def test_day2part2_2():
    input = "824824821-824824827"
    actual = day2.part_two(input)

    expected = "824824824"
    assert expected == str(actual)


def test_day2part2_3():
    input = "1188511880-1188511890"
    actual = day2.part_two(input)

    expected = "1188511885"
    assert expected == str(actual)


def test_day2part2_4():
    input = "1-14"
    actual = day2.part_two(input)

    expected = 11
    assert expected == actual


def test_day2part1_1():
    input = "998-1012"
