from datetime import datetime

import pytest

import aoc_service as a


def main():
    date = datetime(year=2024, month=12, day=1)
    run("11", "31", date, "test run", True)


def run(
    expected_a, expected_b, date=datetime.now(), comment="", record_run_result=False
):
    day = date.day

    a.download(date)
    a.generate_scripts(date)
    result = pytest.main([f"tests\\test_day{day}.py"])
    if result == pytest.ExitCode.OK:
        print(f"Running day{day}.py...")
        actual_a, result_time_a = a.run(day, 1)
        actual_b, result_time_b = a.run(day, 2)
        assert expected_a == actual_a
        assert expected_b == actual_b
        if record_run_result:
            a.record_run_result(day, 1, result_time_a, comment)
            a.record_run_result(day, 2, result_time_b, comment)


if __name__ == "__main__":
    main()
