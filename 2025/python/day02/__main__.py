EXPECTED_TEST_ANSWER_PART1 = [1227775554]
EXPECTED_TEST_ANSWER_PART2 = [4174379265]


def parse_input(data: str) -> list[list[int]]:
    """
    Turns a line of input into values that can be used.
    :param data: a list of ranges separated by comas. Individual numbers are separated by hyphens
    :return: data in the format like [[1,3],[5,9]] where the original was "1-3,5-9"
    """
    result = []
    ranges = data.split(",")
    for item in ranges:
        numbers = item.split("-")
        result.append([numbers[0], numbers[1]])
    return result


def pattern_finder(num: int, break_limiter: int | None = None) -> bool:
    """
    Looks for patterns in a given number
    :num: The number
    :break_limiter: Can set to a specific number to limit the breaking that can be done
        on a number string. For instance, 2 would limit this to only breaking the number
        in half to look for patterns. Leaving as None would break it up all possible ways
    :return: bool if a pattern is found
    """
    num_str = str(num)
    num_str_len = len(num_str)

    max_pattern_len = num_str_len // 2
    for value in range(1, max_pattern_len + 1):
        if num_str_len % value == 0:
            num_repetitions = num_str_len // value
            if break_limiter is not None and num_repetitions > break_limiter:
                continue

            candidate_pattern = num_str[:value]
            reconstructed_num = candidate_pattern * num_repetitions
            if reconstructed_num == num_str:
                return True
    return False


def sort_through_ranges(ranges: list[list[int]], break_limiter: int | None = None):
    """
    Loops over the ranges given, and finds all numbers within that range. Passes
    to pattern_finder to actually test numbers for patterns
    ranges: List of ranges to check (e,g, [[1,3], [4,9]]
    break_limiter: how many breaks you can do on a number (see pattern_finder)
    """
    total = 0
    for start_str, end_str in ranges:
        start_num = int(start_str)
        end_num = int(end_str)
        for i in range(start_num, end_num + 1):
            if pattern_finder(i, break_limiter):
                total += i
    return total


def run(data: list[str]) -> int:
    """
    Takes a list of values in "data" and returns
    the number of times the position is 0 after
    a turn
    """
    ranges = parse_input(data[0])
    total = sort_through_ranges(ranges, 2)

    return total


def run_p2(data: list[str]) -> int:
    """
    Takes a list of values in "data" and returns the total
    of first and last digits concatenated in the string.
    First and last digits now include number words
    """
    ranges = parse_input(data[0])
    total = sort_through_ranges(ranges)
    return total
