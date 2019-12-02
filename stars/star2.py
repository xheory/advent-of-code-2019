from stars.star1 import get_required_fuel, map_over_input, sanitize_input


def get_required_fuel_fuel(mass):
    total_fuel = 0
    fuel_required = True
    while fuel_required:
        added_fuel = get_required_fuel(mass)
        if added_fuel > 0:
            total_fuel += added_fuel
            mass = added_fuel
        else:
            fuel_required = False
    return total_fuel


def run():
    hindsight_fuels = map_over_input(
        get_required_fuel_fuel, "input/star1.input", sanitize=sanitize_input
    )
    total_fuel = sum(hindsight_fuels)
    print(f"In hindsight, the total fuel required is: {total_fuel}")


if __name__ == "__main__":
    get_required_fuel_fuel(654)
