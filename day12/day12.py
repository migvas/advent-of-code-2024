POSSIBLE_DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

input_file = "input.txt"

# Grid that holds the map
grid = []

# Create the grid
with open(input_file, "r", encoding="utf-8") as f:
    while 1:
        line = f.readline().strip()

        if not line:
            break

        grid.append(list(line))

visited = {}


def get_region_specs(l, c, r_type):

    if grid[l][c] != r_type:
        return (0, 1)

    if (l, c) in visited:
        return (0, 0)
    else:
        visited[(l, c)] = True

    area = 1
    perimeter = 0

    for d in POSSIBLE_DIRECTIONS:
        new_l = l + d[0]
        new_c = c + d[1]

        if new_l < 0 or new_l >= len(grid) or new_c < 0 or new_c >= len(grid[0]):
            perimeter += 1
            continue

        new_area, new_per = get_region_specs(new_l, new_c, r_type)
        area += new_area
        perimeter += new_per

    return (area, perimeter)


fence_price = 0

# For each position inside the grid
for i, line in enumerate(grid):
    for j, pos in enumerate(line):
        a, per = get_region_specs(i, j, grid[i][j])
        fence_price += a * per

print(f"Part 1 Solution: {fence_price}")
# print(f"Part 2 Solution: {}")
