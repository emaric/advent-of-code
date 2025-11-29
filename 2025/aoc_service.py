import importlib
import os
import re
import subprocess
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import db

PERSON = "m"


def download(current_date=datetime.now()):
    # Get current date
    print(current_date)

    # Ensure we're in December
    if current_date.month != 12:
        print("Not in December, exiting.")
        return

    # Loop through days 1 to current day
    for day in range(1, current_date.day + 1):
        # Construct filenames
        input_filename = f"inputs\\day{day}.txt"
        example_filename = f"inputs\\day{day}example.txt"

        # Download puzzle input
        if not os.path.exists(input_filename):
            command = f"aocd {day} {current_date.year} > {input_filename}"
            subprocess.run(command, shell=True, check=True)
            print(f"Downloaded input for day {day}, year {current_date.year}")
        else:
            print(f"Input file for day {day}, year {current_date.year} already exists.")

        # Download example
        if not os.path.exists(example_filename):
            command = f"aocd {day} {current_date.year} --example > {example_filename}"
            subprocess.run(command, shell=True, check=True)
            print(f"Downloaded example for day {day}, year {current_date.year}")
        else:
            print(
                f"Example file for day {day}, year {current_date.year} already exists."
            )


def generate_scripts(date=datetime.now()):
    # Generate test script
    if date.month != 12:
        print("Not in December, exiting.")
        return

    day = date.day
    test_fn = f"test_day{day}.py"
    test_fpath = f"tests\\{test_fn}"

    content = f"""
from aoc_service import parse_example
from solutions import day{day}

example_input = "inputs\\\\day{day}example.txt"


def test_day{day}example():
    examples = parse_example({day})

    for example in examples:
        input = example.input_data
        expected_answer_a = example.answer_a
        expected_answer_b = example.answer_b

        actual_answer_a, actual_answer_b = day{day}.solution(input)

        assert expected_answer_a == actual_answer_a 
        assert expected_answer_b == actual_answer_b

    assert len(examples) > 0
    
    """
    if not Path(test_fpath).exists():
        with open(test_fpath, "w") as f:
            f.write(content.strip())

    # Generate solution script
    solution_fpath = f"solutions\\day{day}.py"
    solution_content = """
def solution(input):
    answer_a = part_one(input)
    answer_b = part_two(input)

    return answer_a, answer_b


def part_one(input):
    return "-"


def part_two(input):
    return "-"


def main(part=1):
    with open("inputs\\\\day1.txt", "r") as f:
        input = f.read()

    if part == 1:
        return part_one(input)
    elif part == 2:
        return part_two(input)
    else:
        raise Exception("Not implemented.")


if __name__ == "__main__":
    main()
    """
    if not Path(solution_fpath).exists():
        with open(solution_fpath, mode="w") as f:
            f.write(solution_content.strip())


def submit_solution():
    pass


def record_run_result(
    year: int,
    day: int,
    part: int,
    result_time: float,
    comment: str = "",
    person=PERSON,
    timestamp: datetime = datetime.now(),
):
    with open(f"solutions\\day{day}.py", "r") as f:
        code = f.read()
        db.create_record(year, day, part, result_time, timestamp, comment, person, code)


def run(day: int, part: int):
    try:
        module = importlib.import_module(f"solutions.day{day}")
        main_func = getattr(module, "main")
        start = time.perf_counter()
        answer = main_func(part)
        end = time.perf_counter()
        result_time = end - start
        print(f"day{day} part{part} answer: {answer}, time: {result_time:.6f} seconds")
        return answer, result_time
    except ImportError as e:
        print(f"Error importing module: {e}")
    except AttributeError:
        print("Module imported but 'main' function not found")


def parse_example(day: int):
    with open(f"inputs\\day{day}example.txt") as f:
        input = f.read().strip()
        lines = input.split("\n")[2:]

        examples = []

        for line in lines:
            example_title_line = re.findall(r"(Example data .*) -", line)
            if len(example_title_line):
                examples.append(Example())
            elif line.startswith(
                "--------------------------------------------------------------------------------"
            ):
                pass
            elif line.startswith("answer_a"):
                examples[-1].answer_a = line.lstrip("answer_a: ")
            elif line.startswith("answer_b"):
                examples[-1].answer_b = line.lstrip("answer_b: ")
            else:
                examples[-1].input_lines.append(line)

        return examples


@dataclass
class Example:
    input_lines: list[str] = field(default_factory=list)
    answer_a: str = ""
    answer_b: str = ""

    @property
    def input_data(self):
        return "\n".join(self.input_lines)
