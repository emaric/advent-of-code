import io
import sys
from datetime import datetime

import pytest

import aoc_service as a

REPEAT = 1 


def main():
    day = 1
    date = datetime(year=2026, month=12, day=day)
    if date.day == 1:
        run_one("", date, "init")
        run_two("", date, "init")
    elif date.day == 2:
        run_one("", date, "init")
        run_two("", date, "init")


def run_one(
    expected, date=datetime.now(), comment="", record_run_result=False, repeat=REPEAT
):
    run(1, expected, date, comment, record_run_result, repeat)


def run_two(
    expected, date=datetime.now(), comment="", record_run_result=False, repeat=REPEAT
):
    run(2, expected, date, comment, record_run_result, repeat)


def _run_pytest(day: int, part: int, test_fname=None):
    test_fname = (
        f"test_day{day}part_{'one' if part == 1 else 'two'}"
        if test_fname is None
        else test_fname
    )
    pytest_output = io.StringIO()
    # sys.stdout = pytest_output
    result = pytest.main(
        [
            f"tests\\test_day{day}.py::{test_fname}",
            "--color=yes",
            "--capture=tee-sys",
        ]
    )
    # sys.stdout = sys.__stdout__
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

    print(f"Running Example Day {day} Part {part} solution...")
    result, pytest_output = _run_pytest(day, part)
    if result == pytest.ExitCode.USAGE_ERROR:
        result, pytest_output = _run_pytest(day, part, f"test_day{day}example")

    print(pytest_output)

    if result == pytest.ExitCode.OK:
        print(f"Running Day {day} Part {part} solution...")
        print("======================================================================")
        actual, _ = a.run(day, part)
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


if __name__ == "__main__":
    main()
