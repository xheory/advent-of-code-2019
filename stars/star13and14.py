from common.intcode import IntcodeComputer
from itertools import permutations


with open("input/star13", "r") as input_file:
    amplifier_program = input_file.read().strip()


def setup_amplifier_chain(phase_settings, daisy_chain=False):
    amplifiers = []
    for amplifier_index in range(5):
        input_array = [] if amplifier_index == 0 else amplifiers[-1].output_array
        input_array.append(phase_settings[amplifier_index])
        amplifier = IntcodeComputer(amplifier_program, input_array, [])
        amplifiers.append(amplifier)
    if daisy_chain:
        amplifiers[-1].output_array = amplifiers[0].input_array
    amplifiers[0].input_array.append(0)
    return amplifiers


def run_star13():
    highest_signal = 0
    for permutation in permutations(range(0, 5)):
        amplifiers = setup_amplifier_chain(permutation)
        for amp in amplifiers:
            amp.run()
        highest_signal = max(highest_signal, amplifiers[-1].output_array[-1])
    return f"Highest thruster signal: {highest_signal}"


def run_star14():
    highest_signal = 0
    for permutation in permutations(range(5, 10)):
        amplifiers = setup_amplifier_chain(permutation, daisy_chain=True)
        itcount = 0
        while not amplifiers[-1].is_terminated:
            itcount += 1
            for index, amp in enumerate(amplifiers):
                amp.run()
        highest_signal = max(highest_signal, amplifiers[-1].output_array[-1])
    return f"Highest thruster signal: {highest_signal}"
