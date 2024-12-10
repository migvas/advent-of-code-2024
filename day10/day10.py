from collections import deque

# List of possible directions
POSSIBLE_DIRECTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]

# Part 1 and 2
def count_trails(trail_map, start_line, start_col, count_distinct):
    """
    Counts how many trails we can find in the trail map from a determined starting
    position. A trail is given by a sequence of positions that start as 0 and end with 9,
    only incrementing by 1 and moving acording to POSSIBLE_DIRECTIONS.
    Count distinct changes how the function counts the trails, if it is False then we only
    want to know how many paths start in this position and end at a 9.
    If it is True then we want to know how many distinct paths reach every 9.

    Args:
        trail_map (list[list[string]]): Grid with the heights from 0 to 9 as strings.
        start_line (int): Starting line.
        start_col (col): Starting column.
        count_distinct (bool): Determines how the trails are counted.

    Returns:
        int: Number of possible trails.

    """
    # Variable that counts trails
    trails = 0

    # Queue of postions to process
    q = deque()

    # Put the starting postion in the queue
    q.append((start_line, start_col))

    # Create a set of visited postions and mark the starting position as visited
    # This will make sure that we only count a trail that ends in a specific 9
    # as one instead of all the possible ways of reaching that 9
    # Part 1 we use the set, in part 2 we ignore it
    visited = set((start_line, start_col))

    # While we have positions to process
    while len(q):
        # Get postion from the queue
        coordinates = q.popleft()
        # Get the height from that position
        height = int(trail_map[coordinates[0]][coordinates[1]])

        # For each possible direction
        for d in POSSIBLE_DIRECTIONS:
            # Compute new coordinates
            new_l = coordinates[0] + d[0]
            new_c = coordinates[1] + d[1]

            # If the new position is outside the grid ignore it
            if (
                new_l < 0
                or new_l >= len(trail_map)
                or new_c < 0
                or new_c >= len(trail_map[0])
            ):
                continue
            
            # If we are not counting distinct trails and the coordinates
            # are marked as visited jump to next iteration
            if not count_distinct and (new_l, new_c) in visited:
                continue

            new_height = int(trail_map[new_l][new_c])

            # If the height difference is different than 1 it is not a valid trail
            if new_height - height != 1:
                continue

            # If not counting distinct trails mark the current postion as visited
            if not count_distinct:
                visited.add((new_l, new_c))
            
            # If we reach 9 and the trail is valid increment the trail counter
            # else add the new position to the queue
            if new_height == 9:
                trails += 1
            else:
                q.append((new_l, new_c))

    # Return the number of trails
    return trails


input_file = "input.txt"

# Grid that holds the map
grid = []

# Counter for part 1
trail_score = 0

# Counter for part 2
trail_rating = 0

# Create the grid
with open(input_file, "r", encoding="utf-8") as f:
    while 1:
        line = f.readline().strip()

        if not line:
            break

        grid.append(list(line))

# Loop through the grid and when we find a starting position (0)
# count the trails and add them to the counter
for i, l in enumerate(grid):
    for j, p in enumerate(l):
        if int(p) == 0:
            trail_score += count_trails(grid, i, j, False)
            trail_rating += count_trails(grid, i, j, True)

print(f"Part 1 Solution: {trail_score}")
print(f"Part 2 Solution: {trail_rating}")
