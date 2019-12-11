from common.intcode import IntcodeComputer
from enum import IntEnum


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def turn_left(direction):
        return Direction(direction - 1) if direction > 0 else Direction(3)

    def turn_right(direction):
        return Direction(direction + 1) if direction < 3 else Direction(0)

    def move_forward(direction, current_position):
        x, y = current_position
        if direction == Direction.UP:
            current_position = (x, y + 1)
        elif direction == Direction.RIGHT:
            current_position = (x + 1, y)
        elif direction == Direction.DOWN:
            current_position = (x, y - 1)
        elif direction == Direction.LEFT:
            current_position = (x - 1, y)
        return current_position


def get_hull(starting_color=0):
    return {(0, 0): starting_color}


def walk(robot, robot_input, hull):
    position, direction = (0, 0), Direction.UP
    robot.run()
    while not robot.is_terminated:
        if position not in hull:
            hull[position] = 0

        hull_panel = hull[position]
        robot_input.append(hull_panel)
        robot.run()

        paint_cmd, turn_cmd = robot.output_array[-2:]
        hull[position] = paint_cmd
        direction = direction.turn_left() if turn_cmd == 0 else direction.turn_right()
        position = direction.move_forward(position)


def get_hull_area(hull):
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    for x, y in hull:
        if x < min_x:
            min_x = x
        elif x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        elif y > max_y:
            max_y = y
    return range(min_x, max_x + 1), range(max_y, min_y - 1, -1)


def print_hull(hull):
    x_range, y_range = get_hull_area(hull)
    print(f"Hull print:")
    for y in y_range:
        for x in x_range:
            value = hull[x, y] if (x, y) in hull else 0
            print("1" if value == 1 else " ", end="")
        print()


with open("input/star21") as input_file:
    robot_program = input_file.read().strip()


def run_star21():
    robot_input = []
    robot = IntcodeComputer(robot_program, robot_input, [])
    hull = get_hull()
    walk(robot, robot_input, hull)
    return f"Hull panels traveled: {len(hull)}"


def run_star22():
    robot_input = []
    robot = IntcodeComputer(robot_program, robot_input, [])
    hull = get_hull(starting_color=1)
    walk(robot, robot_input, hull)
    print_hull(hull)
    return f"Identifier: {'PCKRLPUK'}"
