from enum import Enum

EXPECTED_TEST_ANSWER_PART1 = [13]
EXPECTED_TEST_ANSWER_PART2 = [43]

PACKED_LIMIT = 4
ROLL_SYMBOL = "@"
CLEAR_SYMBOL = "."


class Direction(Enum):
    UP_LEFT = (-1, -1)
    UP = (-1, 0)
    UP_RIGHT = (-1, 1)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    DOWN_LEFT = (1, -1)
    DOWN = (1, 0)
    DOWN_RIGHT = (1, 1)


def check_surroundings(
    grid: list[str], x: int, y: int, symbol: str = ROLL_SYMBOL
) -> bool:
    """
    Look around the indicated coordinates and count up how many other
    positions are filled with the given symbol
    """
    rows = len(grid)
    if rows == 0:
        return False
    cols = len(grid[0])

    count = 0

    neighbor_offsets = [direction.value for direction in Direction]

    for dr, dc in neighbor_offsets:
        new_x = x + dr
        new_y = y + dc

        is_valid_x = 0 <= new_x < rows and new_x < len(grid[0])
        is_valid_y = 0 <= new_y < cols and new_y < len(grid)

        if is_valid_x and is_valid_y and grid[new_y][new_x] == symbol:
            count += 1

    if count < PACKED_LIMIT:
        return True
    return False


def find_available_rolls(data):
    points = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if data[y][x] != ROLL_SYMBOL:
                continue
            res = check_surroundings(data, x, y)
            if res:
                points.append([x, y])

    return points


def run(data: list[str]) -> int:
    """
    Takes a list of values in "data" and returns
    the number of times the position is 0 after
    a turn
    """
    free_rolls = find_available_rolls(data)

    return len(free_rolls)


def remove_rolls(data, free_rolls):
    for roll in free_rolls:
        original_string = data[roll[1]]
        index_to_replace = roll[0]
        prefix = original_string[:index_to_replace]
        suffix = original_string[index_to_replace + 1 :]
        data[roll[1]] = prefix + CLEAR_SYMBOL + suffix
    return data


def print_grid(data):
    for row in data:
        print(row)


def run_p2(data: list[str]) -> int:
    """
    Takes a list of values in "data" and returns the total
    of first and last digits concatenated in the string.
    First and last digits now include number words
    """
    first_run = True
    free_rolls = []
    total = 0
    while len(free_rolls) > 0 or first_run:
        first_run = False
        free_rolls = find_available_rolls(data)
        data = remove_rolls(data, free_rolls)
        total += len(free_rolls)

    return total
