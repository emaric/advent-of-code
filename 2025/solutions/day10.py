import itertools
from collections import Counter, defaultdict
from dataclasses import dataclass


@dataclass
class ButtonPresser:
    joltage: list[int]
    button: set[int]
    press_count = 0

    def press(self):
        excluded_jolts = set()
        jolts_in_button = set()

        lights = range(len(self.joltage))

        for light in lights:
            jolt = self.joltage[light]
            if light in self.button:
                jolts_in_button.add(jolt)
            else:
                excluded_jolts.add(jolt)

        min_jolt = min(jolts_in_button)
        target_min = 0
        for jolt in sorted(excluded_jolts, reverse=True):
            if jolt < min_jolt:
                target_min = jolt
                break
        self.press_count = min_jolt - target_min

        if self.press_count > 0:
            # print(f"\n[{self.joltage}]")
            for light in self.button:
                self.joltage[light] -= self.press_count
                if self.joltage[light] < 0:
                    pass

        if self.press_count > 0:
            # print(
            #     f"[{self.joltage}] press count: {self.press_count} -> [{target_min}] -> button: {self.button}"
            # )
            if target_min == 0:
                pass


@dataclass
class JoltageRunner:
    joltage: list
    buttons: list[set[int]]
    press_count: int = 0

    def run(self):
        unique_jolts = set(self.joltage)
        max_jolt = max(unique_jolts)

        if max_jolt == 0:
            return [self.press_count]
        elif max_jolt < 0:
            raise Exception("Unexpected jolt value.")
        else:
            results = []

            lights_with_max_jolt = set(
                [light for light, j in enumerate(self.joltage) if j == max_jolt]
            )
            start_buttons = []
            for b in self.buttons:
                if len(b.intersection(lights_with_max_jolt)) > 0 and 0 not in [
                    self.joltage[light] for light in b
                ]:
                    start_buttons.append(b)
            # print(f"start_buttons: {start_buttons}")

            valid_pressers = []
            for button in start_buttons:
                presser = ButtonPresser(self.joltage.copy(), button)
                presser.press()
                if sum(presser.joltage) == 0:
                    results.append(presser.press_count + self.press_count)
                    return results
                if presser.press_count > 0:
                    if len(results) == 0:
                        runner = JoltageRunner(
                            presser.joltage.copy(),
                            self.buttons,
                            presser.press_count + self.press_count,
                        )
                        results.extend(runner.run())
                    else:
                        return results

            return results


@dataclass
class Machine:
    on_lights: set
    buttons: list
    joltage: list

    def calc_min_presses_to_match_jolt(self):
        buttons = sorted(self.buttons, key=lambda b: -len(b))

        print("Running calc_min_presses_to_match_jolt...")
        print(buttons)
        print("")
        print(self.joltage)
        print("\n\n")

        press_count = max(0, min(self.joltage) - (len(self.buttons) + 1))
        for light in range(len(self.joltage)):
            self.joltage[light] -= press_count

        answer = 0
        runner = JoltageRunner(self.joltage.copy(), buttons, press_count)

        print(self.joltage)
        results = runner.run()
        answer = min(results)

        print("==========================MACHINE RESULT=======================")
        print(self)

        return answer


def part_one(input: str):
    machines: list[Machine] = []
    for line in input.split("\n"):
        light_diagram = line[: line.index("]") + 1]
        joltage = line[line.index("{") :]
        buttons = line[len(light_diagram) + 1 : -len(joltage) - 1]

        on_lights = light_diagram.strip(r"[|]")
        on_lights = set([idx for idx in range(len(on_lights)) if on_lights[idx] == "#"])

        buttons = buttons.split(" ")
        buttons = [set(int(n) for n in b.strip(r"(|)").split(",")) for b in buttons]

        joltage = [int(j) for j in joltage.strip(r"{|}").split(",")]
        machines.append(Machine(on_lights, buttons, joltage))

    answer = 0

    for machine in machines:
        found = False
        count = 0
        while not found:
            count += 1
            for presses in itertools.permutations(machine.buttons, count):
                lights = set()
                for press in presses:
                    lights = lights.symmetric_difference(press)
                if lights == machine.on_lights:
                    answer += count
                    found = True
                    break

    return answer


def part_two(input: str):
    machines: list[Machine] = []
    for line in input.split("\n"):
        light_diagram = line[: line.index("]") + 1]
        joltage = line[line.index("{") :]
        buttons = line[len(light_diagram) + 1 : -len(joltage) - 1]

        on_lights = light_diagram.strip(r"[|]")
        on_lights = set([idx for idx in range(len(on_lights)) if on_lights[idx] == "#"])

        buttons = buttons.split(" ")
        buttons = [set(int(n) for n in b.strip(r"(|)").split(",")) for b in buttons]

        joltage = [int(j) for j in joltage.strip(r"{|}").split(",")]
        machines.append(Machine(on_lights, buttons, joltage))

    answer = 0
    for machine in machines:
        print(machine.buttons)
        print("")
        print(machine.joltage)
        print("\n\n")

        answer += machine.calc_min_presses_to_match_jolt()

    return answer
