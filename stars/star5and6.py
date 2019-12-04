from collections import Counter


class Grid:
    def __init__(self, wire_paths):
        self.wire_paths = wire_paths
        self.reset_data()

    def reset_data(self):
        self.data = Counter()
        self.step_counter = {}

    def add_step_count(self, wire_index, coordinate, step):
        if coordinate not in self.step_counter:
            self.step_counter[coordinate] = [None] * len(self.wire_paths)
        if self.step_counter[coordinate][wire_index] is None:
            self.step_counter[coordinate][wire_index] = step

    def plot(self):
        self.reset_data()
        for wire_index, wire_path in enumerate(self.wire_paths):
            # start at the central port:
            x, y = (0, 0)
            step_count = 0

            for instruction in wire_path:
                direction, value = instruction[0], int(instruction[1:])

                # generate a list of coordinates traveled by the instruction:
                if direction == "U":
                    coordinates = [(x, y + n) for n in range(1, value + 1)]
                elif direction == "D":
                    coordinates = [(x, y - n) for n in range(1, value + 1)]
                elif direction == "L":
                    coordinates = [(x - n, y) for n in range(1, value + 1)]
                elif direction == "R":
                    coordinates = [(x + n, y) for n in range(1, value + 1)]

                # add the coordinates to the counter:
                self.data.update(coordinates)
                for coordinate in coordinates:
                    step_count += 1
                    self.add_step_count(wire_index, coordinate, step_count)

                # update the starting x and y values for the instruction:
                x, y = coordinates[-1]

    def get_distance(self, coordinate):
        return abs(coordinate[0]) + abs(coordinate[1])

    def get_combined_steps_to_coordinate(self, coordinate):
        return sum(self.step_counter[coordinate])

    def get_intersection_coordinates(self):
        return {
            coordinate: self.data[coordinate]
            for coordinate in self.data
            if self.data[coordinate] > 1
        }

    def get_closest_intersection(self):
        intersections = self.get_intersection_coordinates()
        distances = [self.get_distance(coordinate) for coordinate in intersections]
        return min(distances)


def run_star5():
    with open("input/star5.input", "r") as input_file:
        wire_paths = [line.strip().split(",") for line in input_file.readlines()]
    grid = Grid(wire_paths)
    grid.plot()
    return f"Closest Intersection Distance: {grid.get_closest_intersection()}"


def run_star6():
    with open("input/star5.input", "r") as input_file:
        wire_paths = [line.strip().split(",") for line in input_file.readlines()]
    grid = Grid(wire_paths)
    grid.plot()
    intersections = grid.get_intersection_coordinates()
    intersection_steps = [
        sum(grid.step_counter[i])
        for i in intersections
        if all(count is not None for count in grid.step_counter[i])
    ]
    return f"Fewest combined steps until intersection: {min(intersection_steps)}"
