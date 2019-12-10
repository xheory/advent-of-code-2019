from common.intcode import IntcodeComputer

with open("input/star17") as input_file:
    program_code = input_file.read().strip()


def run_star17():
    ic = IntcodeComputer(program_code)
    ic.run()
    ic.input_array.append(1)
    ic.run()
    return f"BOOST keycode: {ic.output_array[0]}"


def run_star18():
    ic = IntcodeComputer(program_code)
    ic.run()
    ic.input_array.append(2)
    ic.run()
    return f"Coordinates: {ic.output_array[0]}"
