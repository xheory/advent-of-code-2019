class IntcodeComputer:
    def __init__(self, input_string):
        self.initial_state = [int(value) for value in input_string.split(",")]
        self.memory = self.initial_state
        self.instruction_pointer = 0

    def add(self, first_index, second_index, storage_index):
        self.memory[storage_index] = (
            self.memory[first_index] + self.memory[second_index]
        )

    def multiply(self, first_index, second_index, storage_index):
        self.memory[storage_index] = (
            self.memory[first_index] * self.memory[second_index]
        )

    def run(self):
        self.instruction_pointer = 0
        running = True
        while running:
            start_address = self.instruction_pointer
            instruction = self.memory[start_address : start_address + 4]
            opcode = instruction[0]

            if opcode == 1:
                self.add(*instruction[1:])
            elif opcode == 2:
                self.multiply(*instruction[1:])
            elif opcode == 99:
                running = False
                break

            self.instruction_pointer += 4


def run_star3():
    with open("input/star3.input") as input_file:
        input_text = input_file.read().strip()
    ic = IntcodeComputer(input_text)
    ic.memory[1] = 12
    ic.memory[2] = 2
    ic.run()
    return f"[Intcode Computer] Value at position 0: {ic.memory[0]}"


def run_star4():
    with open("input/star3.input") as input_file:
        input_text = input_file.read().strip()
    ic = IntcodeComputer(input_text)
    ic.memory[1] = 76
    ic.memory[2] = 3
    ic.run()
    return f"[Intcode Computer] Value at position 0: {ic.memory[0]}"
