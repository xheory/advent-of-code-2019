def count_passwords_matching_criteria(range_start, range_end, criteria_check):
    count = 0
    for x in range(int(range_start), int(range_end) + 1):
        if criteria_check(str(x)):
            count += 1
    return count


def star7_criteria(number):
    matching_digits = False
    decreasing_digits = False
    for c0, c1 in [(int(number[i]), int(number[i + 1])) for i in range(5)]:
        if c0 == c1:
            matching_digits = True
        if c1 < c0:
            decreasing_digits = True
    return matching_digits and not decreasing_digits


def run_star7():
    with open("input/star7.input", "r") as input_file:
        range_start, range_end = input_file.read().split("-")
        amount = count_passwords_matching_criteria(
            range_start, range_end, star7_criteria
        )
    return f"Amount of matching passwords: {amount}"


def star8_criteria(number):
    pair_found = False
    pair_digit = None
    increasing_digits = True

    for c0, c1 in [(int(number[i]), int(number[i + 1])) for i in range(5)]:
        if c1 < c0:
            increasing_digits = False
            break

        if pair_found and c1 != pair_digit:
            pair_found

        if c0 == c1:
            if c1 == pair_digit:
                pair_found = False
            elif not pair_found:
                pair_found = True
                pair_digit = c1
        else:
            pair_digit = None

    return pair_found and increasing_digits


def run_star8():
    with open("input/star7.input", "r") as input_file:
        range_start, range_end = input_file.read().split("-")
        amount = count_passwords_matching_criteria(
            range_start, range_end, star8_criteria
        )
    return f"Amount of matching passwords: {amount}"
