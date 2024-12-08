# Starting position symbol
STARTING_POS = "^"
# Starting direction
STARTING_DIR = [-1, 0]
# Obstacle and empty slot symbols
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
    """
    Determines the number of possible positions that can be visited when
    travelling inside the grid. We stop counting when the evaluated position
    is outside of the grid.

    Args:
        s_line (int): Starting line.
        s_col (int): Starting column.

    Returns:
        int: Number of distinct positions visited.

    """
    positions = 0
    current_line = s_line
    current_col = s_col
    direction = STARTING_DIR

    # Set to hold visited positions
    visited = set()

    while 1:
        # If current position not visited add to the set and
        # increment positions
        if (current_line, current_col) not in visited:
            positions += 1
            visited.add((current_line, current_col))

        # Get next position line and col
        next_l, next_c = current_line + direction[0], current_col + direction[1]

        # If the next position is outside of the grid stop
        if next_l >= len(grid) or next_l < 0 or next_c >= len(grid[0]) or next_c < 0:
            return positions

        next_pos = grid[next_l][next_c]

        # If the next position is an obstacle then change direction
        # and go to the next iteration of the loop in the same position
        if next_pos == OBSTACLE:
            direction = [direction[1], -direction[0]]
            continue

        # If not, change to new postion
        current_line, current_col = next_l, next_c


# Part 2
def has_loop(s_line, s_col, obs_line, obs_col):
    """
    Determines if adding an obstacle to a determine position will
    generate a loop.

    Args:
        s_line (int): Starting line.
        s_col (int): Starting column.
        obs_line (int): New obstacle line.
        obs_col (int): New obstacle column.

    Returns:
        int: 1 if there is a loop, 0 if not.

    """
    current_line = s_line
    current_col = s_col
    direction = STARTING_DIR

    # Set to hold visited positions
    visited = set()

    while 1:
        # Now we save the line, col and direction inside the set
        if (current_line, current_col, direction[0], direction[1]) not in visited:
            visited.add((current_line, current_col, direction[0], direction[1]))
        # If we have a match then it has to be a loop
        else:
            return 1

        # Get next position line and col
        next_l, next_c = current_line + direction[0], current_col + direction[1]

        # If the next position is outside of the grid stop
        if next_l >= len(grid) or next_l < 0 or next_c >= len(grid[0]) or next_c < 0:
            return 0

        next_pos = grid[next_l][next_c]

        # If the next position is an obstacle then change direction
        # and go to the next iteration of the loop in the same position
        # We also have a new obstacle that is not inside the grid
        if next_pos == OBSTACLE or (next_l == obs_line and next_c == obs_col):
            direction = [direction[1], -direction[0]]
            continue

        # If not, change to new postion
        current_line, current_col = next_l, next_c


# Counter to hold the number of loops
loop_counter = 0

# For each position inside the grid, if it an empty slot
# run has_loop adding an obstacle to the current position
for i, line in enumerate(grid):
    for j, pos in enumerate(line):
        if pos == EMPTY_SLOT:
            loop_counter += has_loop(start_line, start_col, i, j)


print(f"Part 1 Solution: {possible_positions(start_line, start_col)}")
print(f"Part 2 Solution: {loop_counter}")
