from pprint import pprint
from collections import Counter
import re

REACTION_REGEX = r"(\d+) (\w+)"


class Reaction:
    def __init__(self, reaction_line):
        matches = re.findall(REACTION_REGEX, reaction_line)
        self.compounds = [(int(m[0]), m[1]) for m in matches[:-1]]
        self.result = int(matches[-1][0]), matches[-1][1]

    def __repr__(self):
        compound_str = ", ".join([f"{i[0]} {i[1]}" for i in self.compounds])
        result_str = f"{self.result[0]} {self.result[1]}"
        return f"<Reaction({compound_str} => {result_str})>"


def break_down_compounds(reactions, compounds, indent=0):
    print(f"breaking down compounds: {compounds}")
    new_compounds = Counter()
    for compound in compounds:
        print(f"breaking down '{compound}':")
        if compound != "ORE":
            subcompounds = reactions[compound].compounds
            subcomp_counter = Counter({sc[1]: sc[0] for sc in subcompounds})
            break_down_compounds(reactions, subcomp_counter, indent + 1)
            new_compounds += break_down_compounds(
                reactions, subcomp_counter, indent + 1
            )
        else:
            new_compounds[compound] += 1
    return new_compounds


if __name__ == "__main__":
    print(f"[Day 14: Part I]")
    reactions = {}
    with open("../input/star27") as input_file:
        for reaction_line in input_file:
            reaction = Reaction(reaction_line.strip())
            reactions[reaction.result[1]] = reaction
    print("----Reactions:")
    pprint(reactions)
    print()
    compounds = Counter({c[1]: c[0] for c in reactions["FUEL"].compounds})
    compounds_needed = break_down_compounds(reactions, compounds)
    print("\n----compounds needed: ")
    pprint(compounds_needed)
