from datetime import datetime

import pytest

import aoc_service as a

REPEAT = 1000


def main():
    date = datetime(year=2025, month=12, day=3)
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
        run_one("-", date, "init")
        run_two("-", date, "init")


def run_one(
    expected, date=datetime.now(), comment="", record_run_result=False, repeat=REPEAT
):
    run(1, expected, date, comment, record_run_result, repeat)


def run_two(
    expected, date=datetime.now(), comment="", record_run_result=False, repeat=REPEAT
):
    run(2, expected, date, comment, record_run_result, repeat)


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
    result = pytest.main([f"tests\\test_day{day}.py::test_day{day}example"])
    if result == pytest.ExitCode.OK:
        print(f"Running day{day} part{part} solution...")
        actual, result_time = a.run(day, part)
        print("")
        assert expected == actual
        if record_run_result:
            print(f"Running day{day} part{part} solution {repeat} times...")
            actual, avg_run_time = a.run(day, part, repeat)
            a.record_run_result(year, day, part, avg_run_time, comment)
            print("")


if __name__ == "__main__":
    main()
