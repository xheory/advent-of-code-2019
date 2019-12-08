class IntcodeComputer(object):
    @staticmethod
    def parse_program(program):
        return [int(number) for number in program.split(",")]

    def reset(self, program=None):
        self.program = [] if program is None else self.parse_program(program)
        self.program_input = []
        self.current_input_index = 0
        self.program_output = None
        self.memory = self.program
        self.memory_position = 0
        self.running = False

    def __init__(self, input_program=None):
        self.reset(input_program)

    def parse_instruction_head(self, number):
        digits = [int(digit) for digit in f"{number:05}"]
        opcode = digits[-2] * 10 + digits[-1]
        parameter_modes = tuple(digits[-3:-6:-1])
        return opcode, tuple(parameter_modes)

    def parse_parameter(self, position_offset, parameter_mode):
        memory_position = self.memory_position + position_offset
        if parameter_mode == 0:
            value_index = self.memory[memory_position]
            value = self.memory[value_index]
        elif parameter_mode == 1:
            value = self.memory[memory_position]
        return value

    def add(self, parameter_modes):
        parameter1 = self.parse_parameter(1, parameter_modes[0])
        parameter2 = self.parse_parameter(2, parameter_modes[1])
        write_index = self.memory[self.memory_position + 3]
        self.memory[write_index] = parameter1 + parameter2
        return self.memory_position + 4

    def multiply(self, parameter_modes):
        parameter1 = self.parse_parameter(1, parameter_modes[0])
        parameter2 = self.parse_parameter(2, parameter_modes[1])
        write_index = self.memory[self.memory_position + 3]
        self.memory[write_index] = parameter1 * parameter2
        return self.memory_position + 4

    def terminate(self):
        self.running = False
        return 0

    def input(self, program_input):
        self.program_input.append(program_input)

    def save_program_input(self, parameter_modes):
        memory_index = self.memory[self.memory_position + 1]
        self.memory[memory_index] = self.program_input[self.current_input_index]
        self.current_input_index += 1
        return self.memory_position + 2

    def set_program_output(self, parameter_modes):
        memory_index = self.memory[self.memory_position + 1]
        self.program_output = self.memory[memory_index]
        return self.memory_position + 2

    def jump_if_true(self, parameter_modes):
        parameter1 = self.parse_parameter(1, parameter_modes[0])
        if parameter1 != 0:
            parameter2 = self.parse_parameter(2, parameter_modes[1])
            return parameter2
        else:
            return self.memory_position + 3

    def jump_if_false(self, parameter_modes):
        parameter1 = self.parse_parameter(1, parameter_modes[0])
        if parameter1 == 0:
            parameter2 = self.parse_parameter(2, parameter_modes[1])
            return parameter2
        else:
            return self.memory_position + 3

    def less_than(self, parameter_modes):
        parameter1 = self.parse_parameter(1, parameter_modes[0])
        parameter2 = self.parse_parameter(2, parameter_modes[1])
        write_index = self.memory[self.memory_position + 3]
        self.memory[write_index] = 1 if parameter1 < parameter2 else 0
        return self.memory_position + 4

    def equals(self, parameter_modes):
        parameter1 = self.parse_parameter(1, parameter_modes[0])
        parameter2 = self.parse_parameter(2, parameter_modes[1])
        write_index = self.memory[self.memory_position + 3]
        self.memory[write_index] = 1 if parameter1 == parameter2 else 0
        return self.memory_position + 4

    def parse_instruction(self):
        instruction_head = self.memory[self.memory_position]
        opcode, parameter_modes = self.parse_instruction_head(instruction_head)
        if opcode == 1:
            return self.add, 3, parameter_modes
        elif opcode == 2:
            return self.multiply, 3, parameter_modes
        elif opcode == 3:
            return self.save_program_input, 1, parameter_modes
        elif opcode == 4:
            return self.set_program_output, 1, parameter_modes
        elif opcode == 5:
            return self.jump_if_true, 2, parameter_modes
        elif opcode == 6:
            return self.jump_if_false, 2, parameter_modes
        elif opcode == 7:
            return self.less_than, 3, parameter_modes
        elif opcode == 8:
            return self.equals, 3, parameter_modes
        elif opcode == 99:
            return self.terminate, 0, None

    def load_program(self, program):
        self.reset(program)

    def run(self):
        self.running = True
        while self.running:
            method, parameter_count, parameter_modes = self.parse_instruction()
            if parameter_count > 0:
                self.memory_position = method(parameter_modes)
            else:
                self.memory_position = method()
        return self.program_output


intcode_computer = IntcodeComputer()


def run_star9():
    with open("input/star9.input", "r") as input_file:
        program = input_file.read().strip()
        program_input = 1
        intcode_computer.load_program(program)
        intcode_computer.input(program_input)
        program_output = intcode_computer.run()
    return f"[Intcode Computer] Output: {program_output}"


def run_star10():
    with open("input/star9.input", "r") as input_file:
        program = input_file.read().strip()
        program_input = 5
        intcode_computer.load_program(program)
        intcode_computer.input(program_input)
        program_output = intcode_computer.run()
    return f"[Intcode Computer] Output: {program_output}"


# When the commputer wants to receive input, halt until input is received then continue using the input gotten.
# If you rewrite the array-method into something that just halts, then continues when input has been gotten,
# the problem of daisy-chaining as in part 2 day 7 should solve itself.
