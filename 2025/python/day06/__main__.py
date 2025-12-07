from math import prod

EXPECTED_TEST_ANSWER_PART1 = [4277556]
EXPECTED_TEST_ANSWER_PART2 = [3263827]


def parse_input(data):
    """
    Simple parsing of input used in part 1
    """
    numbers = []
    for row in data[:-1]:
        numbers.append([int(num) for num in row.split()])
    operations = [op.strip() for op in data[-1].split()]
    number_columns = [list(col) for col in zip(*numbers)]
    return number_columns, operations


def parse_input2(data):
    """
    Treat the columns like really odd problems where you're numbers are rotated
    """
    operations = [op.strip() for op in data[-1].split()]
    numbers = []

    space_locations = _find_spaces(data[:-1])

    space_locations = [0] + space_locations
    for row in data[:-1]:
        parts = _split_problems(space_locations, row)
        numbers.append(parts)

    number_columns = [list(col) for col in zip(*numbers)]

    rotated_numbers = []
    for column in number_columns:
        res = combine_digits_right_to_left(column)
        rotated_numbers.append(res)
    return rotated_numbers, operations


def _find_spaces(data):
    """
    Find where there are spaces in ALL the rows of data (discarding ones
    that only exist in some)
    """
    space_locations = False
    for row in data:
        if not space_locations:
            space_locations = [i for i, char in enumerate(row) if char == " "]
        else:
            locs = [i for i, char in enumerate(row) if char == " "]
            space_locations = sorted(list(set(space_locations) & set(locs)))
    return space_locations


def _split_problems(space_locations, row):
    """
    Split strings along found boundaries
    """
    parts = []
    end = 0
    for i in range(len(space_locations) - 1):
        start = space_locations[i]
        end = space_locations[i + 1]

        substring = row[start:end]
        parts.append(substring)
    parts.append(row[end + 1 :])
    return parts


def operate(numgroup, op):
    """
    Calculate result based on the operation (op) indicated
    """
    total = 0
    if op == "+":
        total += sum(numgroup)
    elif op == "*":
        total += prod(numgroup)
    return total


def combine_digits_right_to_left(str_list: list) -> list:
    """ """

    max_len = 0
    if str_list:
        max_len = max(len(s) for s in str_list)
    result_numbers = []
    for i in range(max_len - 1, -1, -1):
        column_digits = []
        for s in str_list:
            try:
                char = s[i]
            except IndexError:
                continue
            if char.isdigit():
                column_digits.append(char)

        if column_digits:
            number_str = "".join(column_digits)
            result_numbers.append(int(number_str))

    return result_numbers


def run(data: list[str]) -> int:
    """
    Treat the columns like everyday numbers
    """
    total = 0
    numbers, operations = parse_input(data)
    for idx, numgroup in enumerate(numbers):
        if len(numgroup) == 0:
            continue
        total += operate(numgroup, operations[idx])
    return total


def run_p2(data: list[str]) -> int:
    """ """
    total = 0
    numbers, operations = parse_input2(data)
    for idx, numgroup in enumerate(numbers):
        if len(numgroup) == 0:
            continue
        total += operate(numgroup, operations[idx])

    return total
