from datetime import datetime

import pytest

import aoc_service as a


def main():
    date = datetime(year=2023, month=12, day=2)
    if date.day == 1:
        run(57346, 57345, date, "test run", True)
    elif date.day == 2:
        run("-", "-", date, "test run", True)


def run(
    expected_a, expected_b, date=datetime.now(), comment="", record_run_result=False
):
    year = date.year
    day = date.day

    a.download(date)
    a.generate_scripts(date)
    result = pytest.main([f"tests\\test_day{day}.py::test_day{day}example"])
    if result == pytest.ExitCode.OK:
        print(f"Running day{day}.py...")
        actual_a, result_time_a = a.run(day, 1)
        actual_b, result_time_b = a.run(day, 2)
        assert expected_a == actual_a
        assert expected_b == actual_b
        if record_run_result:
            a.record_run_result(year, day, 1, result_time_a, comment)
            a.record_run_result(year, day, 2, result_time_b, comment)


if __name__ == "__main__":
    main()
