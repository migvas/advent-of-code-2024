import math


# Part 1
def is_valid_update(arr, rule_ancestors):
    """
    Determines if the array is in the right order considering that
    every element in rule_ancestors must come before the corresponding
    element in the array.

    Args:
        arr (list[str]): List of numbers as string to check the order.
        rule_ancestors (dic): Dictionary with the ancestors for multiple elements.

    Returns:
        bool: True if ordered, False if not.

    """
    # Dict to hold invalid successors
    invalid_successors = {}

    # Check every element
    for el in arr:
        # If the element is inside invalid_successors return False
        if el in invalid_successors:
            return False

        # If not then check if element has ancestors
        if el in rule_ancestors:
            # Add all the ancestors as invalid successors
            for a in rule_ancestors[el]:
                invalid_successors[a] = True

    return True

# Part 2
def correct_array(arr, rule_ancestors, mid):
    """
    Order the invalid arrays and return the middle element.

    Args:
        arr (list[str]): List of numbers as string to order.
        rule_ancestors (dic): Dictionary with the ancestors for multiple elements.
        mid (int): Middle index.

    Returns:
        int: Value of the middle element as int.

    """
    i = 0
    # For each element, check every other element and if it is an ancestor
    # then switch postion and repeat
    while i < len(arr) - 1:
        curr_ancestors = rule_ancestors.get(arr[i], {})
        for j in range(i + 1, len(arr)):
            if arr[j] in curr_ancestors:
                arr[i], arr[j] = arr[j], arr[i]
                i -= 1
                break
        i += 1

    return int(arr[mid])


input_file = "input.txt"

# Dict to hold the ancestors for each element
ancestors = {}
# Hold the sum of the middle numbers for each sequence
mid_sum = 0
# Hold the sum of the middle numbers for each corrected sequence
corrected_mid_sum = 0

with open(input_file, "r", encoding="utf-8") as f:
    while 1:
        rule_line = f.readline().strip()

        if not rule_line:
            break

        n1, n2 = rule_line.split("|")

        # n2 will always have to succeed to n1
        # So n1 is n2 ancestor
        if n2 not in ancestors:
            ancestors[n2] = {}

        ancestors[n2][n1] = True

    while 1:
        updates = f.readline().strip()

        if not updates:
            break

        update_arr = updates.split(",")
        # Compute the middle index
        mid_idx = math.floor(len(update_arr) / 2)

        # If the sequence is valid the add the middle number
        if is_valid_update(update_arr, ancestors):
            mid_sum += int(update_arr[mid_idx])
        else:
            # If it is not valid the correct the array and sum the new middle number
            corrected_mid_sum += correct_array(update_arr, ancestors, mid_idx)

print(f"Part 1 Solution: {mid_sum}")
print(f"Part 2 Solution: {corrected_mid_sum}")
