from common.intcode import IntcodeComputer


def run_star3():
    with open("input/star3.input") as input_file:
        input_text = input_file.read().strip()
    ic = IntcodeComputer(input_text)
    ic.program[1] = 12
    ic.program[2] = 2
    ic.run()
    return f"[Intcode Computer] Value at position 0: {ic.program[0]}"


def run_star4():
    with open("input/star3.input") as input_file:
        input_text = input_file.read().strip()
    ic = IntcodeComputer(input_text)
    ic.program[1] = 76
    ic.program[2] = 3
    ic.run()
    return f"[Intcode Computer] Value at position 0: {ic.program[0]}, noun=76, verb=3"
