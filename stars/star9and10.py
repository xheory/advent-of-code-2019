from common.intcode import IntcodeComputer

with open("input/star9.input", "r") as input_file:
    program_code = input_file.read().strip()


def run_star9():
    output_array = []
    ic = IntcodeComputer(program_code, [1], output_array)
    ic.run()
    return f"[Intcode Computer] Output: {output_array[-1]}"


def run_star10():
    output_array = []
    ic = IntcodeComputer(program_code, [5], output_array)
    ic.run()
    return f"[Intcode Computer] *TEST INPUT*: {output_array[-1]}"
