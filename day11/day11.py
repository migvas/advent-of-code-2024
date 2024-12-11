from collections import deque

STONE_MULTIPLIER = 2024

input_file = "input.txt"

stone_mem = {}
def change_stones(stone, num_blinks):
    if (stone, num_blinks) in stone_mem:
        return stone_mem[(stone, num_blinks)]
    
    if num_blinks == 0:
        num_stones = 1

    elif stone == "0":
        num_stones = change_stones("1", num_blinks - 1)

    elif len(stone) % 2 == 0:
        mid = len(stone) // 2
        h1, h2 = int(stone[:mid]), int(stone[mid:])
        num_stones = change_stones(str(h1), num_blinks - 1) + change_stones(str(h2), num_blinks - 1)

    else:
        new_stone = int(stone) * STONE_MULTIPLIER
        num_stones = change_stones(str(new_stone), num_blinks - 1)

    stone_mem[(stone, num_blinks)] = num_stones
    return num_stones

def run_blinks(stones_arr, num_blinks):
    stone_counter = 0
    for stone in stones_arr:
        stone_counter += change_stones(stone, num_blinks)

    return stone_counter


with open(input_file, "r", encoding="utf-8") as f:
    # Create a variable with all the data from the file
    file_data = f.read()
    stones = file_data.strip().split(" ")

print(f"Part 1 Solution: {run_blinks(stones, 25)}")
print(f"Part 2 Solution: {run_blinks(stones, 75)}")
