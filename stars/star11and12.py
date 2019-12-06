orbits = {}


def path(child_tag, acc):
    parent_tag = orbits[child_tag]
    acc.insert(0, parent_tag)
    return path(parent_tag, acc) if parent_tag != "COM" else acc


def count_orbits():
    orbit_count = 0
    for child_tag in orbits:
        orbit_count += len(path(child_tag, []))
    return orbit_count


def get_transfers_to_san():
    san_path = set(path("SAN", []))
    you_path = set(path("YOU", []))
    return len(san_path.symmetric_difference(you_path))


def run_star11():
    with open("input/star11", "r") as input_file:
        for line in input_file:
            parent_tag, child_tag = line.strip().split(")")
            orbits[child_tag] = parent_tag
    orbit_count = count_orbits()
    return f"Orbit count: {orbit_count}"


def run_star12():
    transfers = get_transfers_to_san()
    return f"Transfers to that guy: {transfers}"
