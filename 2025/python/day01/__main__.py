EXPECTED_TEST_ANSWER_PART1 = [3]
EXPECTED_TEST_ANSWER_PART2 = [6]


START_POS = 50
MAX_POS = 100


def parse_rotation(row: str) -> int:
    """
    Simple parsing of the row. The first position
    is the direction, the rest if a number.
    """
    dir = 1 if row[0] == "R" else -1
    value = int(row[1:])
    return dir * value


def run(data: list[str]) -> int:
    """
    Takes a list of values in "data" and returns
    the number of times the position is 0 after
    a turn
    """
    total = 0
    position = START_POS
    for row in data:
        position += parse_rotation(row)
        position = position % MAX_POS

        if position == 0:
            total += 1

    return total


def parse_row(row: str, position: int, total: int):
    prev_position = position
    position += parse_rotation(row)
    if prev_position * position < 0 or position == 0:
        total += 1
    if abs(position) >= MAX_POS:
        total += abs(position) // MAX_POS
    position = position % MAX_POS
    return total, position


def run_p2(data):
    """
    Takes a list of values in "data" and returns the total
    of first and last digits concatenated in the string.
    First and last digits now include number words
    """
    total = 0
    position = START_POS
    for row in data:
        total, position = parse_row(row, position, total)
    return total
