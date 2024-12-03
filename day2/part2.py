# Number of bad levels allowed
MAX_BAD_LEVELS = 1

def is_safe(arr, p1, p2, bad_levels, order):
    """
    Recursively determines whether a sequence of integers is "safe" based on specific rules.

    Rules:
    1. The absolute difference between consecutive elements must be between 1 and 3 (inclusive).
    2. The sequence is either consistently increasing or decreasing but a limited number of "bad levels" are allowed (determined by MAX_BAD_LEVELS).

    Args:
        arr (list[int]): The list of integers to evaluate.
        p1 (int): The current position in the array.
        p2 (int): The next position to evaluate in the array.
        bad_levels (int): The current count of deviations from the sequence order.
        order (str or None): The order of the sequence, either "inc" (increasing), "dec" (decreasing), or None if undetermined.

    Returns:
        bool: True if the sequence is safe, False otherwise.

    Examples:
        >>> is_safe([1, 2, 3, 7], 0, 1, 0, None)
        True
        >>> is_safe([1, 2, 1, 3], 0, 1, 0, None)
        False
        >>> is_safe([1, 3, 2, 4], 0, 1, 1, None)
        False
    """
    if bad_levels > MAX_BAD_LEVELS:
        return False
    
    if p2 >= len(arr):
        return p1 == len(arr) - 1 or bad_levels <= MAX_BAD_LEVELS   
    
    difference = int(arr[p2]) - int(arr[p1])

    if abs(difference) > 3 or abs(difference) < 1:
        return False

    if not order:
        if difference > 0:
            order = "inc"
        else:
            order = "dec"
    else:
        if order == "inc" and difference < 0:
            return False
        if order == "dec" and difference > 0:
            return False
        
    return is_safe(arr, p2, p2 + 1, bad_levels, order) or is_safe(arr, p2, p2 + 2, bad_levels + 1, order)
        

input_file = "input.txt"

safe = 0

with open(input_file, "r") as f:
    for line in f:
        # For each line we evaluate if the input arr is safe and add it to the counter
        line_arr = line.strip().split(" ")
        # We have 3 starting scenarios:
        # p1 = 0 p2 = 1 and no position skipped
        # p1 = 1 p2 = 2 where we skip the first position
        # p1 = 0 p2 = 2 where we skip the second position
        if is_safe(line_arr, 0, 1, 0, None) or is_safe(line_arr, 1, 2, 1, None) or is_safe(line_arr, 0, 2, 1, None):
            safe += 1

print(safe)