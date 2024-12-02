def is_safe(arr, p1, p2, bad_levels, order):
    if bad_levels == 2:
        return False
    
    if p2 >= len(arr):
        return p1 == len(arr) - 1 or bad_levels < 2   
    
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
        line_arr = line.strip().split(" ")
        if is_safe(line_arr, 0, 1, 0, None) or is_safe(line_arr, 1, 2, 1, None) or is_safe(line_arr, 0, 2, 1, None):
            safe += 1

print(safe)