from dataclasses import dataclass
from functools import cached_property


@dataclass
class Node:
    device: Device
    parent_count: int

    def __hash__(self):
        return hash(self.device)

    def __eq__(self, other):
        return self.device == other.device

    def __repr__(self):
        return f"{self.device.name}: {self.parent_count}"


@dataclass
class Device:
    name: str
    output_names: set[str]
    input_names: set[str]

    source_dict: dict

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    @cached_property
    def outputs(self) -> list[Device]:
        return [v for k, v in self.source_dict.items() if k in self.output_names]

    @cached_property
    def inputs(self) -> list[Device]:
        return [v for k, v in self.source_dict.items() if k in self.input_names]

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def count_paths(start_str: str, target_str: str, source: dict[str, Device]):
    start = source[start_str]
    target = source[target_str]

    ordered: list[list[Node]] = [[Node(start, 0)]]

    output_nodes = []
    for device in start.outputs:
        output_nodes.append(Node(device, parent_count=1))
    ordered.append(output_nodes)

    while True:
        unique = {}
        for nodes in ordered[-1:]:
            for node in nodes:
                for device in node.device.outputs:
                    if device in unique:
                        unique[device].parent_count += node.parent_count
                    else:
                        _node = Node(device, node.parent_count)
                        unique[device] = _node
        if len(unique) > 0:
            ordered.append([v for k, v in unique.items()])
        else:
            break

    count = 0  # noqa: F811
    target_node = Node(target, 0)
    for idx, nodes in enumerate(ordered):
        if target_node in nodes:
            dac_idx = nodes.index(target_node)
            count += nodes[dac_idx].parent_count

    return count


def parse_input(input) -> dict[str, Device]:
    devices_dict: dict[str, Device] = {}

    for line in input.split("\n"):
        device_names = line.split(" ")
        d1 = device_names[0][:-1]
        outputs = device_names[1:]

        if d1 in devices_dict:
            device = devices_dict[d1]
        else:
            device = Device(d1, set(), set(), devices_dict)

        device.output_names.update(outputs)
        devices_dict[d1] = device

        for output in outputs:
            if output in devices_dict:
                device = devices_dict[output]
            else:
                device = Device(output, set(), set(), devices_dict)

            device.input_names.add(d1)
            devices_dict[output] = device
    return devices_dict


def part_one(input: str):
    devices_dict: dict[str, Device] = parse_input(input)

    answer = count_paths("you", "out", devices_dict)

    return answer


def part_two(input: str):
    devices_dict: dict[str, Device] = parse_input(input)

    svr_to_fft = count_paths("svr", "fft", devices_dict)
    fft_to_dac = count_paths("fft", "dac", devices_dict)
    dac_to_out = count_paths("dac", "out", devices_dict)

    return svr_to_fft * fft_to_dac * dac_to_out
