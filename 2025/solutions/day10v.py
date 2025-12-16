import re
from dataclasses import dataclass
from functools import cached_property
from itertools import permutations
from typing import Any


@dataclass()
class Branch:
    current_joltage: list[int]
    buttons: list[list[int]]
    button: list[int]
    press_count: int

    def min_presses(self):
        current_joltage = [self.current_joltage[l] for l in self.button]
        # find highest and second highest joltage
        if len(set(current_joltage)) <= 1:
            target_jolt = 0
            max_jolt = current_joltage[0]
        else:
            target_jolt, max_jolt = sorted(set(current_joltage))[-2:]

        print(f"min_presses: {current_joltage}, {max_jolt}, {target_jolt}")
        return min(max_jolt - target_jolt, min(current_joltage))

    def max_jolt_idx(self):
        return self.current_joltage.index(max(self.current_joltage))

    def check_zero(self) -> bool:
        return sum(self.current_joltage) <= 0

    def process(self):
        # update current joltage of this step
        min_presses = self.min_presses()
        for idx in self.button:
            self.current_joltage[idx] -= min_presses
        self.press_count += min_presses

    def get_next_branches(self):
        wl = self.get_working_list()

        branches = []
        for button in wl:
            branches.append(
                Branch(
                    self.current_joltage.copy(), self.buttons, button, self.press_count
                ),
            )
        return branches

    def get_working_list(self):
        current_joltage = self.current_joltage
        # find highest and second highest joltage
        if len(set(current_joltage)) == 1:
            target_jolt = 0
            max_jolt = current_joltage[0]
        else:
            target_jolt, max_jolt = sorted(set(current_joltage))[-2:]

        max_jolt_indices = set(
            [idx for idx, l in enumerate(current_joltage) if l == max_jolt]
        )
        target_jolt_indices = set(
            [idx for idx, l in enumerate(current_joltage) if l == target_jolt]
        )

        print(f"MAX: {max_jolt}, TARGET: {target_jolt}")

        working_list = []

        # find button set(s) that includes this idx and sort by # of lights affected
        for button in sorted(self.buttons, key=lambda b: -len(b)):
            if len(max_jolt_indices.intersection(set(button))) > 0:
                for l in button:
                    if self.current_joltage[l] == 0:
                        break
                working_list.append(button)

        return working_list


@dataclass(init=False)
class Machine:
    lights: int
    solution: list[int]
    buttons: list[list[int]]
    jolts: list[int]

    def __init__(self, input: str):
        _, lights, buttons, jolts, _ = re.split(r"[\[\]\{\}]", input)

        self.solution = [c == "#" for c in lights]
        self.lights = len(lights)

        self.buttons = []
        buttons = buttons.strip().replace("(", "").replace(")", "").split(" ")
        for b in buttons:
            bs = b.split(",")
            li = [int(n) for n in bs]
            self.buttons.append(li)

        self.jolts = [int(j) for j in jolts.split(",")]

    def brute(self) -> int:
        for i in range(len(self.buttons)):
            for perm in permutations(self.buttons, i):
                if self._press(perm) == self.solution:
                    return i
        return 0

    def _press(self, perm):
        result = [False] * self.lights
        for buttons in perm:
            for b in buttons:
                result[b] = not result[b]
        return result

    def by_joltage(self) -> int:
        current_joltage = [j for j in self.jolts]
        button_presses = 0
        branches: list[Branch] = []
        results = []

        print(f"Machine: {self}")

        # find highest and second highest joltage
        target_jolt, max_jolt = sorted(set(current_joltage))[-2:]

        max_jolt_indices = set(
            [idx for idx, l in enumerate(current_joltage) if l == max_jolt]
        )
        target_jolt_indices = set(
            [idx for idx, l in enumerate(current_joltage) if l == target_jolt]
        )

        print(f"MAX: {max_jolt}, TARGET: {target_jolt}")

        working_list = []

        # find button set(s) that includes this idx and sort by # of lights affected
        for button in sorted(self.buttons, key=lambda b: -len(b)):
            if len(max_jolt_indices.intersection(set(button))) > 0:
                for l in button:
                    if current_joltage[l] == 0:
                        break
                working_list.append(button)

        # create a branch for every working set we dont use and add it to our branches
        for button in working_list:
            branches.append(
                Branch(current_joltage.copy(), self.buttons, button, button_presses),
            )

        # process branches

        while len(branches) > 0 and len(results) <= 10:
            branch: Branch = branches.pop(0)
            print(f"\tbranch: {branch}")
            print(f"\t\tbutton: {branch.button}, min_presses: {branch.min_presses()}")
            branch.process()

            # win con
            if branch.check_zero():
                results.append(branch.press_count)
            else:
                li = branch.get_next_branches()
                for b in li:
                    branches.insert(0, b)

        print(f"\t\tcurrent_joltage: {current_joltage}")
        return min(results)


def part_one(input: str):
    lines = input.strip().split("\n")

    machines = []

    for line in lines:
        machine = Machine(line)
        machines.append(machine)

    sum = 0
    for machine in machines:
        sum += machine.brute()

    return sum


def part_two(input: str):
    lines = input.strip().split("\n")

    machines = []

    for line in lines:
        machine = Machine(line)
        machines.append(machine)

    sum = 0
    for machine in machines:
        joltage = machine.by_joltage()
        print(machine, joltage)
        sum += joltage

    return sum
