def is_safe(arr):
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
        line_arr = line.strip().split(" ")
        if is_safe(line_arr):
            safe += 1

print(safe)