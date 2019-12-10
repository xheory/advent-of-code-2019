from common.intcode import IntcodeComputer

with open("input/star17") as input_file:
    program_code = input_file.read().strip()


def run_star17():
    ic = IntcodeComputer(program_code)
    ic.run()
    ic.input_array.append(1)
    ic.run()
    return f"???: {ic.output_array}"


def run_star18():
    return f"???: {'???'}"
