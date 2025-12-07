import io
import sys
from datetime import datetime

import pytest

import aoc_service as a

REPEAT = 100


def main():
    date = datetime(year=2025, month=12, day=5)
    if date.day == 1:
        run_one(1081, date, "final")
        run_two(6689, date, "final")
    elif date.day == 2:
        run_one(35367539282, date, "final")
        run_two(45814076230, date, "final")
    elif date.day == 3:
        run_one(16946, date, "final")
        run_two(168627047606506, date, "final")
    elif date.day == 4:
        run_one(1495, date, "test utc timestamp")
        run_two(8768, date, "test utc timestamp")
    elif date.day == 5:
        run_one(664, date, "unwrapped func calls")
        run_two(350780324308385, date, "init")


def run_one(
    expected, date=datetime.now(), comment="", record_run_result=False, repeat=REPEAT
):
    run(1, expected, date, comment, record_run_result, repeat)


def run_two(
    expected, date=datetime.now(), comment="", record_run_result=False, repeat=REPEAT
):
    run(2, expected, date, comment, record_run_result, repeat)


def _run_pytest(day: int):
    pytest_output = io.StringIO()
    sys.stdout = pytest_output
    result = pytest.main(
        [f"tests\\test_day{day}.py::test_day{day}example", "--color=yes"]
    )
    sys.stdout = sys.__stdout__
    return result, pytest_output.getvalue()


def run(
    part,
    expected,
    date=datetime.now(),
    comment="",
    record_run_result=False,
    repeat=REPEAT,
):
    year = date.year
    day = date.day
    a.download(date)
    a.generate_scripts(date)

    result, pytest_output = _run_pytest(day)

    if result == pytest.ExitCode.OK:
        print(f"Running Day {day} Part {part} solution...")
        print("======================================================================")
        actual, _ = a.run(day, part, 10)
        print("======================================================================")
        print("")
        color = a.PART_ONE_COLOR if part == 1 else a.PART_TWO_COLOR
        assert expected == actual, (
            f"Day {day} Part {part} Failed! {a.RESET}Expected = {color}{expected}{a.RESET}; Actual = {a.ORANGE}{actual}{a.RESET}"
        )
        if record_run_result:
            print(f"Running Day{day} Part {part} solution {repeat} times...")
            actual, avg_run_time = a.run(day, part, repeat)
            a.record_run_result(year, day, part, avg_run_time, comment)
            print("")
    else:
        print(pytest_output)


if __name__ == "__main__":
    main()
