EXPECTED_TEST_ANSWER_PART1 = [3]
EXPECTED_TEST_ANSWER_PART2 = [14]


def parse_data(data: list[str]) -> tuple[list[tuple[int]], list[int]]:
    """
        Sorts the data into two lists:
        1) At the start, there are ranges 123-456
        2) Then there's an empty line for a gap
        3) Then there are a list of numbers (ingredients): one per line
    """
    ingredient_switch = False
    ranges = []
    ingredients = []
    for line in data:
        if line.strip() == "":
            ingredient_switch = True
            continue
        if not ingredient_switch:
            nums = line.strip().split("-")
            ranges.append((int(nums[0]), int(nums[1])))
            continue
        ingredients.append(int(line.strip()))
    return ranges, ingredients


def check_ranges(ranges: list[tuple[int]], ingredient: int) -> bool:
    """
        Checks to see if an ingredient is in any of the given ranges.
    """
    found_range = False
    for r in ranges:
        if r[0] <= ingredient <= r[1]:
            found_range = True

    return found_range


def run(data: list[str]) -> int:
    """

    """
    total = 0
    ranges, ingredients = parse_data(data)
    for ingredient in ingredients:
        res = check_ranges(ranges, ingredient)
        if res:
            total += 1
    return total


def sort_ranges(ranges):
    """
        Takes all the ranges, and sorts then by the start number
    """
    ranges.sort(key=lambda x: x[0])
    return ranges


def merge_ranges(ranges):
    """
        In order to avoid issues from overlapping ranges,
        we need to merge any ranges that share values.
    """
    merged = []

    current_start, current_end = ranges[0]
    for next_start, next_end in ranges[1:]:
        if next_start <= current_end:
            current_end = max(current_end, next_end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = next_start, next_end
    merged.append((current_start, current_end))
    return merged


def run_p2(data: list[str]) -> int:
    """

    """
    total = 0
    ranges, ingredients = parse_data(data)
    ranges = sort_ranges(ranges)
    ranges = merge_ranges(ranges)
    for r in ranges:
        total += r[1] - r[0] + 1

    return total
