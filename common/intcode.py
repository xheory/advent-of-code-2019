class IntcodeMemory(object):
    def __init__(self, init_data=None):
        self.data = {}
        for address, value in enumerate(init_data):
            self.data[address] = value

    def __repr__(self):
        return repr(self.data)

    def __setitem__(self, address, value):
        self.data[address] = value

    def _load_memory_value(self, address):
        if address not in self.data:
            self.data[address] = 0
        return self.data[address]

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._load_memory_value(key)
        elif isinstance(key, slice):
            indices = key.indices(len(self.data))
            indice_range = range(*indices)
            slice_result = [self._load_memory_value(x) for x in indice_range]
            return slice_result

    def __delitem__(self, index):
        if index in self.data:
            del self.data[index]


class IntcodeInstruction(object):
    def __init__(self, method, param_count=0):
        self.method = method
        self.param_count = param_count

    def __repr__(self):
        return f"Instruction({self.method.__name__}, param_count={self.param_count})"


class IntcodeComputer(object):
    def __init__(self, program_code=None, input_array=None, output_array=None):
        self._running = False  # Whether or not the program is running.
        self._should_halt = False
        self._head_jump = None
        self.is_terminated = False  # True, if opcode 99 was encountered.
        self.original_code = None  # Last program code loaded into the computer.
        self.program = None  # Currently loaded/running program.
        self.input_array = input_array if input_array is not None else []
        self.output_array = output_array if output_array is not None else []
        self.head = 0  # Program execution position.
        self.relative_base = 0

        self.instructions = {
            1: IntcodeInstruction(self.add, param_count=3),
            2: IntcodeInstruction(self.multiply, param_count=3),
            3: IntcodeInstruction(self.read, param_count=1),
            4: IntcodeInstruction(self.write, param_count=1),
            5: IntcodeInstruction(self.jump_if_true, param_count=2),
            6: IntcodeInstruction(self.jump_if_false, param_count=2),
            7: IntcodeInstruction(self.less_than, param_count=3),
            8: IntcodeInstruction(self.equals, param_count=3),
            9: IntcodeInstruction(self.adjust_relative_base, param_count=1),
            99: IntcodeInstruction(self.terminate),
        }

        if program_code is not None:
            self.load_program(program_code)

    def load_program(self, program_code=None):
        if program_code is not None:
            self.original_code = program_code
        if self.original_code is not None:
            parsed_code = [int(num.strip()) for num in program_code.split(",")]
            self.program = IntcodeMemory(parsed_code)

    def get_parameters(self, *values, literals=[]):
        parameters = []
        for index, (value, mode) in enumerate(zip(values, self._param_modes)):
            if index in literals:
                if mode == 0 or mode == 1:
                    parameters.append(value)
                else:
                    parameters.append(value + self.relative_base)
            else:
                if mode == 0:  # position mode
                    parameters.append(self.program[value])
                elif mode == 1:  # immediate mode
                    parameters.append(value)
                elif mode == 2:  # relative mode
                    parameters.append(self.program[value + self.relative_base])
        return tuple(parameters) if len(parameters) > 1 else parameters[0]

    def write_value_to_program(self, index, value):
        self.program[index] = value

    # 1
    def add(self, arg1, arg2, position):
        value1, value2, value3 = self.get_parameters(arg1, arg2, position, literals=[2])
        self.write_value_to_program(value3, value1 + value2)

    # 2
    def multiply(self, arg1, arg2, position):
        value1, value2, value3 = self.get_parameters(arg1, arg2, position, literals=[2])
        self.write_value_to_program(value3, value1 * value2)

    # 3
    def read(self, position):
        if len(self.input_array) > 0:
            value = self.input_array.pop(0)
            param = self.get_parameters(position, literals=[0])
            self.program[param] = value
            self._should_halt = False
        else:
            self._should_halt = True

    # 4
    def write(self, position):
        output = self.get_parameters(position)
        self.output_array.append(output)

    # 5
    def jump_if_true(self, value, jump_position):
        value, jump_position = self.get_parameters(value, jump_position)
        if value != 0:
            self._head_jump = jump_position

    # 6
    def jump_if_false(self, value, jump_position):
        value, jump_position = self.get_parameters(value, jump_position)
        if value == 0:
            self._head_jump = jump_position

    # 7
    def less_than(self, arg1, arg2, position):
        value1, value2, value3 = self.get_parameters(arg1, arg2, position, literals=[2])
        self.program[value3] = 1 if value1 < value2 else 0

    # 8
    def equals(self, arg1, arg2, position):
        value1, value2, value3 = self.get_parameters(arg1, arg2, position, literals=[2])
        self.program[value3] = 1 if value1 == value2 else 0

    # 9
    def adjust_relative_base(self, arg1):
        adjustment_value = self.get_parameters(arg1)
        self.relative_base += adjustment_value

    # 99
    def terminate(self):
        self._running = False
        self.is_terminated = True

    def _parse_instruction_head(self):
        head = f"{self.program[self.head]:05}"
        return int(head[-2:]), list(map(int, head[2::-1]))

    def run(self):
        self._running = True
        self._should_halt = False
        while self._running:
            opcode, self._param_modes = self._parse_instruction_head()
            instruction = self.instructions[opcode]
            if instruction.param_count > 0:
                param_start_index = self.head + 1
                param_end_index = self.head + instruction.param_count + 1
                method_args = self.program[param_start_index:param_end_index]
                instruction.method(*method_args)
            else:
                instruction.method()

            if self._should_halt:
                self._running = False
            else:
                self.head = (
                    self.head + instruction.param_count + 1
                    if self._head_jump is None
                    else self._head_jump
                )
                self._head_jump = None
