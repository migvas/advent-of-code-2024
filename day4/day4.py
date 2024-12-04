# Word we are searching for
TARGET_WORD = "XMAS"

# Possible valid directions that the word can be written in
POSSIBLE_DIRECTIONS = [
    [0, 1],
    [1, 0],
    [1, 1],
    [-1, 0],
    [0, -1],
    [1, -1],
    [-1, 1],
    [-1, -1],
]

# Directions to analyze the X letters, we pair them because no two pairs can be equal
X_DIRECTIONS_PAIRS = [[[-1, -1], [1, 1]], [[1, -1], [-1, 1]]]

# Center letter for the X
X_CENTER = "A"

# Letters that make each side of the X
X_WORD_LETTERS = {"M": 1, "S": 1}

input_file = "input.txt"

# Create the grid with the letters from the input data
grid = []
with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line_arr = list(line.strip())
        grid.append(line_arr)

# Part 1


def word_search(x, y, direction, letter_pos):
    """
    Search recursively if the target word is found inside the grid.

    If the direction is not defined we loop through all directions in
    POSSIBLE_DIRECTIONS and if the TARGET_WORD is found in that
    direction we add one to the counter.

    Args:
        x (int): x coordinate.
        y (int): y coordinate.
        direction(list[int]): Direction followed to find the word.
        letter_pos (int): Position of the current letter in the
        target word.

    Returns:
        int: Number of times the target word is found.
    """

    # If x or y are out of the grid then return 0
    if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
        return 0

    # If the current grid pos has a different letter than the one
    # that we are analyzing then return 0
    if grid[x][y] != TARGET_WORD[letter_pos]:
        return 0

    if not direction:
        # If a direction is not defined then we should be at the first letter
        # We need to loop through all possible directions and find how many
        # times we found the target word from the current first letter
        counter = 0
        for d in POSSIBLE_DIRECTIONS:
            counter += word_search(x + d[0], y + d[1], d, letter_pos + 1)
        return counter

    # If we reach the final letter then return 1
    if letter_pos == len(TARGET_WORD) - 1:
        return 1

    return word_search(x + direction[0], y + direction[1], direction, letter_pos + 1)


# Part 2


def x_search(x, y):
    """
    Search if an X exists in the grid.

    It takes the coordinates of the first letter and if it is valid
    searches if the letters on X_DIRECTIONS_PAIRS match the ones that
    form a valid X.

    Args:
        x (int): x coordinate.
        y (int): y coordinate.

    Returns:
        int: Number of valid Xs (0 or 1).
    """

    # If current letter is not the center letter
    if grid[x][y] != X_CENTER:
        return 0

    letter_counter = []
    # Check each direction pair
    # We divide the directions in pairs because the X is only valid
    # if it contains the word MAS
    # This way we can remove cases where we have 2 Ms, 2 Ss and 1 A but
    # the X contains the words MAM and SAS
    for pair in X_DIRECTIONS_PAIRS:
        # Dict used to count letters
        letters = {}
        # For each direction get the letter
        for d in pair:
            new_x = x + d[0]
            new_y = y + d[1]
            
            # If new x and y are out of the grid then X is not valid
            if new_x >= len(grid) or new_x < 0 or new_y >= len(grid[0]) or new_y < 0:
                return 0

            # Fill the dict
            letter = grid[new_x][new_y]
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1

            letter_counter.append(letters)

    # For each dict generated that correspondts to each side of the X
    for l_dict in letter_counter:
        # If it is different from the reference dict, the X is not valid
        if l_dict != X_WORD_LETTERS:
            return 0

    return 1


# Go through every position in the grid and run both functions
word_count = 0
count_x = 0
for i, _ in enumerate(grid):
    for j, _ in enumerate(grid[i]):
        word_count += word_search(i, j, None, 0)
        count_x += x_search(i, j)

print(f"Part 1 Solution: {word_count}")
print(f"Part 2 Solution: {count_x}")
