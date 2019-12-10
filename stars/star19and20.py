import math
from pprint import pprint


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = x, y
        self.distances = {}
        self.angles = {}

    def __repr__(self):
        return f"<Asteroid({self.x}, {self.y})>"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def calc_angle_to(self, other):
        self.distances[other.pos] = math.sqrt(
            (other.x - self.x) ** 2 + (other.y - self.y) ** 2
        )
        self.angles[other.pos] = (
            math.atan2(other.y - self.y, other.x - self.x) * 180 / math.pi
        )
        return self.angles[other.pos]

    def __getitem__(self, other_pos):
        return self.angles[other_pos], self.distances[other_pos]

    def __setitem__(self, other_pos, value):
        raise NotImplementedError("Stop trying to alter the universe.")

    def __delitem__(self, other_pos):
        raise NotImplementedError("Stop trying to alter the universe.")


def load_map(map_string):
    asteroids = []
    for y, line in enumerate(map_string.strip().split()):
        for x, char in enumerate(line):
            if char == "#":
                asteroids.append(Asteroid(x, y))
    return asteroids


def identify_best_station_position(asteroids):
    unique_angle_counts = {}
    for aid, asteroid in enumerate(asteroids):
        for other_astroid in asteroids:
            if asteroid != other_astroid:
                asteroid.calc_angle_to(other_astroid)
        unique_angle_count = len(set(asteroid.angles.values()))
        unique_angle_counts[asteroid.pos] = unique_angle_count
    return max(unique_angle_counts.items(), key=lambda item: item[1])


def order_asteroids_around_station(asteroids, station):
    relative_asteroids = []
    for asteroid in asteroids:
        angle = (station.angles[asteroid.pos] + 90) % 360
        distance = station.distances[asteroid.pos]
        relative_asteroids.append(
            {
                "asteroid": asteroid,
                "position": asteroid.pos,
                "angle": angle,
                "angle_original": station.angles[asteroid.pos],
                "distance": distance,
            }
        )
    return sorted(
        relative_asteroids,
        key=lambda asteroid: (asteroid["angle"], asteroid["distance"]),
    )


def shoot_asteroids(asteroids):
    vaporized_asteroids = []
    while len(asteroids) > 0:
        next_asteroid_angle = asteroids[0]["angle"]
        for index, asteroid in enumerate(asteroids):
            if next_asteroid_angle != asteroid["angle"]:
                next_asteroids = asteroids[0:index]
                break
        del asteroids[: len(next_asteroids)]

        # If more than one asteroid, add the rest to the back
        if len(next_asteroids) > 1:
            asteroids.extend(next_asteroids[1:])

        vaporized_asteroids.append(next_asteroids[0]["asteroid"])
    return vaporized_asteroids


def run_star19():
    with open("input/star19") as input_file:
        asteroids = load_map(input_file.read())
    location, station_angle_count = identify_best_station_position(asteroids)
    return f"Most angles reached | loc={location}: {station_angle_count}"


def run_star20():
    with open("input/star19") as input_file:
        asteroids = load_map(input_file.read())
    station_position, _ = identify_best_station_position(asteroids)
    for asteroid in asteroids:
        if asteroid.pos == station_position:
            station_asteroid = asteroid
            break
    asteroids.remove(station_asteroid)

    sorted_asteroids = order_asteroids_around_station(asteroids, station_asteroid)
    vaporized_asteroids = shoot_asteroids(sorted_asteroids)
    x, y = vaporized_asteroids[199].pos
    result = x * 100 + y
    return f"result: {result}"
