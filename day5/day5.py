import math


# Part 1
def is_valid_update(arr, rule_ancestors):
    invalid_successors = {}

    for el in arr:
        if el in invalid_successors:
            return False

        if el in ancestors:
            for a in rule_ancestors[el]:
                invalid_successors[a] = True

    return True

# Part 2
def correct_array(arr, rule_ancestors, mid):
    i = 0
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

ancestors = {}
mid_sum = 0
corrected_mid_sum = 0

with open(input_file, "r", encoding="utf-8") as f:
    while 1:
        rule_line = f.readline().strip()

        if not rule_line:
            break

        n1, n2 = rule_line.split("|")

        if n2 not in ancestors:
            ancestors[n2] = {}

        ancestors[n2][n1] = True

    while 1:
        updates = f.readline().strip()

        if not updates:
            break

        update_arr = updates.split(",")
        mid_idx = math.floor(len(update_arr) / 2)

        if is_valid_update(update_arr, ancestors):
            mid_sum += int(update_arr[mid_idx])
        else:
            corrected_mid_sum += correct_array(update_arr, ancestors, mid_idx)

print(f"Part 1 Solution: {mid_sum}")
print(f"Part 2 Solution: {corrected_mid_sum}")
