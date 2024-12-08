# Possible operations
POSSIBLE_OPERATIONS = ["+", "*"]
POSSIBLE_OPERATIONS_2 = ["+", "*", "||"]


# Part 1 and 2
def is_valid(arr, total, curr_val, pos, operator, possible_operations):
    """
    Determines if applying the possible operations to the array makes it equal to
    the total value.

    Args:
        arr (list[str]): A list of numbers as strings to evaluate.
        total (int): Target value.
        current_val (int): Current val to use for the next operation.
        pos (int): Current array position to evaluate.
        operator (str): Operator to use.
        possible_operations (list[str]): List of possible operations.

    Returns:
        bool: True if the array is valid, False otherwise.

    Examples:
        >>> is_valid(["10", "19"], 190, 0, 0, None, POSSIBLE_OPERATIONS)
        True
    """

    # If we pass the last array position and the current val is
    # equal to total then the array is valid
    if curr_val == total and pos == len(arr):
        return True

    # If the current val is greater than total or we pass the last
    # position and still didn't reach the total the the array is not valid
    if curr_val > total:
        return False

    if pos >= len(arr):
        return False

    # How each operator changes the current value
    if operator:
        if operator == "+":
            curr_val += int(arr[pos])
        if operator == "*":
            curr_val = curr_val * int(arr[pos])
        if operator == "||":
            curr_val = int(str(curr_val) + arr[pos])
    # Used for the first element
    else:
        curr_val = int(arr[pos])

    # For each possible operations run recursively
    for op in possible_operations:
        # If we reach a valid combination then return True
        if is_valid(arr, total, curr_val, pos + 1, op, possible_operations):
            return True

    # No valid combination of operations
    return False


input_file = "input.txt"

# Variables to hold the sum for both cases
calibration_result = 0
calibration_result_2 = 0

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line_arr = line.strip().split(":")
        total_val = int(line_arr[0])
        numbers = line_arr[1].strip().split(" ")
        # For part 1
        if is_valid(numbers, total_val, 0, 0, None, POSSIBLE_OPERATIONS):
            calibration_result += total_val
        # For part 2
        if is_valid(numbers, total_val, 0, 0, None, POSSIBLE_OPERATIONS_2):
            calibration_result_2 += total_val

print(f"Part 1 Solution: {calibration_result}")
print(f"Part 2 Solution: {calibration_result_2}")
