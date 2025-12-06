EXPECTED_TEST_ANSWER_PART1 = [357]
EXPECTED_TEST_ANSWER_PART2 = [3121910778619]


def parse_input(data: list[str]) -> list[list[int]]:
    banks = []
    for bank_str in data:
        bank = []
        for battery in bank_str.strip():
            bank.append(int(battery))
        banks.append(bank)
    return banks


def find_largest_simple(bank: str) -> int:
    """
    Find the largest 2-digit number in a string
    without reordering digits, but removing some if
    needed
    """
    largest_battery = max(bank[:-1])
    battery_location = bank.index(largest_battery)
    bank.pop(battery_location)
    second_battery = max(bank[battery_location:])

    return int(str(largest_battery) + str(second_battery))


def run(data: list[str]) -> int:
    """
    Takes a list of values in "data" and returns
    the number of times the position is 0 after
    a turn
    """
    total = 0
    banks = parse_input(data)
    for bank in banks:
        print(bank)
        num = find_largest_simple(bank)
        print(num)
        total += num
    return total


def find_largest_number(bank: str, num_digits: int) -> int:
    """
    Finds the largest number by removing digits from the string
    version of the bank definition.
    """
    n = len(bank)
    removals_allowed = n - num_digits
    result = []

    for digit in bank:
        while removals_allowed > 0 and result and result[-1] < digit:
            result.pop()
            removals_allowed -= 1

        result.append(digit)

    while removals_allowed > 0:
        result.pop()
        removals_allowed -= 1

    final_string = "".join(str(digit) for digit in result)
    return int(final_string)


def run_p2(data: list[str]) -> int:
    """
    Takes a list of values in "data" and returns the total
    of first and last digits concatenated in the string.
    First and last digits now include number words
    """
    total = 0
    banks = parse_input(data)
    for bank in banks:
        print(bank)
        num = find_largest_number(bank, 12)
        print(num)
        total += num
    return total
