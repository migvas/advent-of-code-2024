STARTING_POS = "^"
STARTING_DIR = [-1, 0]
OBSTACLE = "#"
EMPTY_SLOT = "."

input_file = "input.txt"

# Create the grid with the letters from the input data
grid = []
start_line = 0
start_col = 0
with open(input_file, "r", encoding="utf-8") as f:
    i = 0
    while 1:
        rule_line = f.readline().strip()

        if not rule_line:
            break

        line_arr = list(rule_line)

        for j, pos in enumerate(line_arr):
            if pos == STARTING_POS:
                start_line = i
                start_col = j

        grid.append(line_arr)

        i += 1


# Part 1
def possible_positions(s_line, s_col):
    positions = 0
    current_line = s_line
    current_col = s_col
    direction = STARTING_DIR

    visited = set()

    while 1:
        if (current_line, current_col) not in visited:
            positions += 1
            visited.add((current_line, current_col))

        next_l, next_c = current_line + direction[0], current_col + direction[1]

        if next_l >= len(grid) or next_l < 0 or next_c >= len(grid[0]) or next_c < 0:
            return positions

        next_pos = grid[next_l][next_c]

        if next_pos == OBSTACLE:
            direction = [direction[1], -direction[0]]
            continue

        current_line, current_col = next_l, next_c


# Part 2
def has_loop(s_line, s_col, obs_line, obs_col):
    current_line = s_line
    current_col = s_col
    direction = STARTING_DIR

    visited = set()

    while 1:
        if (current_line, current_col, direction[0], direction[1]) not in visited:
            visited.add((current_line, current_col, direction[0], direction[1]))
        else:
            return 1

        next_l, next_c = current_line + direction[0], current_col + direction[1]

        if next_l >= len(grid) or next_l < 0 or next_c >= len(grid[0]) or next_c < 0:
            return 0

        next_pos = grid[next_l][next_c]

        if next_pos == OBSTACLE or (next_l == obs_line and next_c == obs_col):
            direction = [direction[1], -direction[0]]
            continue

        current_line, current_col = next_l, next_c


loop_counter = 0

for i, line in enumerate(grid):
    for j, pos in enumerate(line):
        if pos == EMPTY_SLOT:
            loop_counter += has_loop(start_line, start_col, i, j)


print(f"Part 1 Solution: {possible_positions(start_line, start_col)}")
print(f"Part 2 Solution: {loop_counter}")
