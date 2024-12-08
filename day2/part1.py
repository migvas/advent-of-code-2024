def is_safe(arr):
    """
    Determines whether a sequence of integers is "safe" based on specific rules.

    A sequence is considered "safe" if:
    1. The absolute difference between consecutive elements is between 1 and 3 (inclusive).
    2. The sequence is either consistently increasing or decreasing.

    Args:
        arr (list[str]): A list of numbers in the form of strings to evaluate.

    Returns:
        bool: True if the sequence is safe, False otherwise.

    Examples:
        >>> is_safe(["1", "3", "4"])
        True
        >>> is_safe(["4", "1", "1"])
        False
        >>> is_safe(["5"])
        True
    """
    if len(arr) == 1:
        return True
    
    is_increasing = True
    for i in range(1, len(arr)):
        difference = int(arr[i]) - int(arr[i-1])

        if abs(difference) > 3 or abs(difference) < 1:
            return False

        if i == 1:
            is_increasing = (difference >= 0)
        else:
            if (difference > 0) != is_increasing:
                return False
            
    
    return True
        

input_file = "input.txt"

safe = 0

with open(input_file, "r") as f:
    for line in f:
        # For each line we evaluate if the input arr is safe and add it to the counter
        line_arr = line.strip().split(" ")
        if is_safe(line_arr):
            safe += 1

print(safe)