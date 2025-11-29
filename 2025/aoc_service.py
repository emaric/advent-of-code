import os
import re
import subprocess
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


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

example_input = "inputs\\day{day}example.txt"


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
            f.write(content)

    # Generate solution script
    solution_fpath = f"solutions\\day{day}.py"
    solution_content = """
def solution(input):
    answer_a = "-"
    answer_b = "-"

    return answer_a, answer_b
    """
    if not Path(solution_fpath).exists():
        with open(solution_fpath, mode="w") as f:
            f.write(solution_content)


def submit_solution():
    pass


def submit_results_to_db():
    pass


def run(solution_file):
    pass


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
