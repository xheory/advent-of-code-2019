import re


class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"<x={self.x:>4}, y={self.y:>4}, z={self.z:>4}>"

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


class Moon:
    def __init__(self, id, position):
        self.id = id
        self.position = position
        self.velocity = Vector()

    def __repr__(self):
        return f"<Moon id={self.id}, pos={self.position}, vel={self.velocity}>"

    def get_potential_energy(self):
        return abs(self.position.x) + abs(self.position.y) + abs(self.position.z)

    def get_kinetic_energy(self):
        return abs(self.velocity.x) + abs(self.velocity.y) + abs(self.velocity.z)

    def get_total_energy(self):
        return self.get_potential_energy() * self.get_kinetic_energy()


def load_moons():
    moons = []
    with open("input/star23") as input_file:
        for line in input_file:
            coordinates = re.findall(r"-?\d+", line.strip())
            moons.append(Moon(len(moons), Vector(*map(int, coordinates))))
    return moons


def apply_gravity(moon1, moon2):
    for coordinate in range(3):
        if moon1.position[coordinate] > moon2.position[coordinate]:
            moon1.velocity[coordinate] -= 1
            moon2.velocity[coordinate] += 1
        elif moon1.position[coordinate] < moon2.position[coordinate]:
            moon1.velocity[coordinate] += 1
            moon2.velocity[coordinate] -= 1


def do_time_step(moons):
    for moon1_index, moon1 in enumerate(moons):
        for moon2 in moons[moon1_index:]:
            if moon1.id != moon2.id:
                apply_gravity(moon1, moon2)
        moon1.position += moon1.velocity


def run_star23():
    moons = load_moons()

    # --- Debug print:
    print("After 0 steps:")
    for moon in moons:
        print(moon)
    print()

    steps = 1000
    for step_index in range(steps):
        do_time_step(moons)

        if (step_index + 1) % 10 == 0:
            print(f"After {step_index+1} step{'' if step_index == 0 else 's'}:")
            for moon in moons:
                print(moon)
            print()

    total_energy = sum(moon.get_total_energy() for moon in moons)
    return f"Total energy: {total_energy}"


def run_star24():
    moons = load_moons()
    return f"???: {moons}"
