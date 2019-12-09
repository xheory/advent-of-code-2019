from common.intcode import IntcodeComputer
from itertools import permutations


with open("input/star13", "r") as input_file:
    amplifier_program = input_file.read().strip()


def setup_amplifier_chain(daisy_chain=False):
    amplifiers = []
    for amplifier_index in range(5):
        input_array = [] if amplifier_index == 0 else amplifiers[-1].output_array
        amplifier = IntcodeComputer(
            amplifier_program, input_array=input_array, output_array=[]
        )
        amplifiers.append(amplifier)
    if daisy_chain:
        amplifiers[0].input_array = amplifiers[-1].output_array
    return amplifiers


def 


def run_star13():
    amplifiers = setup_amplifier_chain()
    print(f"Amplifiers: {amplifiers}")
    return f"Highest thruster signal: {'???'}"


def run_star14():
    return f"???: {'???'}"
