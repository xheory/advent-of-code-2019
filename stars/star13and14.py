from stars.star9and10 import IntcodeComputer
from itertools import permutations

amplifiers = None


def find_single_phase_signals(phase_settings):
    possible_phase_settings = permutations([0, 1, 2, 3, 4], 5)
    thruster_signals = {}
    amplifier_index = 0
    for phase_settings in possible_phase_settings:
        phase_setting_str = "".join(map(str, phase_settings))
        input_signal = 0
        for phase_setting in phase_settings:
            amplifier = amplifiers[amplifier_index]
            amplifier.input(phase_setting)
            amplifier.input(input_signal)
            input_signal = amplifier.run()
        thruster_signals[phase_setting_str] = input_signal
    return thruster_signals


def run_star13():
    global amplifiers
    with open("input/star13", "r") as input_file:
        amplifier_program = input_file.read().strip()
    amplifiers = [IntcodeComputer(amplifier_program) for _ in range(5)]
    thruster_signals = find_single_phase_signals([0, 1, 2, 3, 4])
    thruster_signals = find_single_phase_signals([0, 1, 2, 3, 4])
    thruster_signals = find_single_phase_signals([0, 1, 2, 3, 4])
    thruster_signals = find_single_phase_signals([0, 1, 2, 3, 4])
    highest_truster_signal = max(thruster_signals.items(), key=lambda item: item[1])[1]
    return f"Highest thruster signal: {highest_truster_signal}"


def run_star14():
    result = None
    return f"???: {result}"
