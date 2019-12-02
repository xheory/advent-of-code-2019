import math
from common.functions import map_over_input


def get_required_fuel(mass: int) -> int:
    required_fuel = math.floor(mass / 3.0) - 2
    return required_fuel


def sanitize_input(value):
    return int(value.strip())


def run():
    input_lines = map_over_input(
        get_required_fuel, "stars/star1.input", sanitize=sanitize_input
    )
    total_fuel = sum(input_lines)
    return f"The total fuel required is: {total_fuel}"
