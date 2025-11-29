from datetime import datetime

import pytest

import aoc_service as a


def main():
    date = datetime(year=2024, month=12, day=1)
    run(None, date, "test run")


def run(correct_answer, date=datetime.now(), comment="", record_run_result=False):
    day = date.day

    a.download(date)
    a.generate_scripts(date)
    result = pytest.main([f"tests\\test_day{day}.py"])
    if result == pytest.ExitCode.OK:
        print(f"Running day{day}.py...")
        answer, result_time = a.run(day)
        assert answer == correct_answer
        if record_run_result:
            a.record_run_result(day, result_time, comment)


if __name__ == "__main__":
    main()
