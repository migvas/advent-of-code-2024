# Empty slot symbol
EMPTY_SLOT = "."

input_file = "input.txt"


def count_antinodes(antenna_map):
    """
    Counts how many unique locations within the bounds of the map contain an antinode.

    Args:
        antenna_map (list[list[str]]): The map with the positions to evaluate.

    Returns:
        int: Number of unique locations with antinodes.

    """
    # Set to store antinode positions
    antinodes = set()

    # Dict to store antenna positons
    antennas = {}

    # Loop through all the positions of the map
    for i, map_line in enumerate(antenna_map):
        for j, pos in enumerate(map_line):
            # If the position contains an antenna
            if pos != EMPTY_SLOT:
                # If it is a new antenna create an array for that antenna in the dict
                if pos not in antennas:
                    antennas[pos] = []

                # For each other antenna from the same frequency
                for other_antenna in antennas[pos]:
                    # Compute the distance between the two antennas
                    distance = [i - other_antenna[0], j - other_antenna[1]]

                    # Compute the 2 possible antinode locations
                    possible_antinodes = [
                        (i + distance[0], j + distance[1]),
                        (
                            other_antenna[0] - distance[0],
                            other_antenna[1] - distance[1],
                        ),
                    ]

                    for ant in possible_antinodes:
                        # If the antinode is inside the map add its location to the set
                        if (
                            ant[0] >= 0
                            and ant[0] < len(antenna_map)
                            and ant[1] >= 0
                            and ant[1] < len(antenna_map[0])
                        ):
                            antinodes.add(ant)

                antennas[pos].append([i, j])

    # Return the length of the set
    return len(antinodes)


def count_antinodes_harmonics(antenna_map):
    """
    Counts how many unique locations within the bounds of the map contain an antinode.
    In this function we consider that all locations in the same line as two antennas
    can contain an antinode.

    Args:
        antenna_map (list[list[str]]): The map with the positions to evaluate.

    Returns:
        int: Number of unique locations with antinodes.

    """
    # Set to store antinode positions
    antinodes = set()
    # Dict to store antenna positons
    antennas = {}

    # Set to store the locations of two antennas to form a line
    antenna_lines = set()

    # Loop through all the positions of the map
    for i, map_line in enumerate(antenna_map):
        for j, pos in enumerate(map_line):
            # If it is a new antenna create an array for that antenna in the dict
            if pos != EMPTY_SLOT:
                if pos not in antennas:
                    antennas[pos] = []

                # For each other antenna from the same frequency add both locations to the set
                for other_antenna in antennas[pos]:
                    antenna_lines.add((i, j, other_antenna[0], other_antenna[1]))
                # We could also compute the line equation y = ax + b and then store a and b
                # But since a = (y2-y1)/(x2-x1) this would lead to floating-point precision
                # errors so we went with a different approach

                antennas[pos].append([i, j])

    # Loop through all the positions of the map again
    for i, map_line in enumerate(antenna_map):
        for j, pos in enumerate(map_line):
            # For each pair of points
            for lp in antenna_lines:
                # To avoid division we consider that the three points (A and B from lp
                # and C from the current position) form two vectors AB and AC
                # Creating a matrix with both vectors, we compute the determinant
                # of that matrix and if it equals 0 then they are colinear
                det = ((lp[2] - lp[0]) * (j - lp[1])) - ((lp[3] - lp[1]) * (i - lp[0]))
                if det == 0:
                    antinodes.add((i, j))
                    # If the position belongs to a line we don't need to test other lines
                    break

    # Return the length of the set
    return len(antinodes)


# Grid that holds the map
grid = []

# Create the grid
with open(input_file, "r", encoding="utf-8") as f:
    while 1:
        line = f.readline().strip()

        if not line:
            break

        grid.append(list(line))


print(f"Part 1 Solution: {count_antinodes(grid)}")
print(f"Part 2 Solution: {count_antinodes_harmonics(grid)}")
