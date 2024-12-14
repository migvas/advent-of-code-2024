# Offset for part 2
POSITION_OFFSET = 10000000000000

def cramers_rule(v11, v12, v21, v22, v31, v32):
    """
    Solve a linear equation using Cramer's rule.

    Args:
        v11 (int): First value of the first vector.
        v12 (int): Second value of the first vector.
        v21 (int): First value of the second vector.
        v22 (int): Second value of the second vector.
        v31 (int): First value of the third vector.
        v32 (int): Second value of the third vector.

    Returns:
        tuple: A tuple containing:
            x (float): The x value of the linear equation.
            y (float): The y value of the linear equation.

    """
    x = (v31*v22 - v21*v32)/(v11*v22 - v21*v12)
    y = (v11*v32 - v31*v12)/(v11*v22 - v21*v12)

    return x, y

input_file = "input.txt"

# Token counters for both parts
total_tokens = 0
total_tokens2 = 0

with open(input_file, "r", encoding="utf-8") as f:
    while 1:
        # When reading the file we need to always read 3 lines
        a_line = f.readline().strip()
        # If the first doesn't exist we have reached the end
        if not a_line:
            break
        
        # For every line split by : and take the second half
        a_line = a_line.split(":")[1]

        # For the buttons split by , and then for each coordinate take what comes after +
        h1, h2 = a_line.split(",")
        a1 = int(h1.split("+")[-1])
        a2 = int(h2.split("+")[-1])

        b_line = f.readline().strip().split(":")[1]

        h1, h2 = b_line.split(",")
        b1 = int(h1.split("+")[-1])
        b2 = int(h2.split("+")[-1])

        prize_line = f.readline().strip().split(":")[1]

        # For the prize line split by , and then for each coordinate take what comes after =
        h1, h2 = prize_line.split(",")
        c1 = int(h1.split("=")[-1])
        c2 = int(h2.split("=")[-1])

        # For part 2 add the position offset to the prize coordinates
        c21 = c1 + POSITION_OFFSET
        c22 = c2 + POSITION_OFFSET

        f.readline()

        # Solve the linear equation
        n_a, n_b = cramers_rule(a1, a2, b1, b2, c1, c2)
        n_a2, n_b2 = cramers_rule(a1, a2, b1, b2, c21, c22)

        # Since n_a and n_b are floats we have to check if the decimal part is 0
        # If not it is impossible to win the prize
        # If we check the remainder of the division by 1 we can know if it is a decimal
        # number or an integer
        if n_a % 1 == 0 and n_b % 1 == 0:
            total_tokens += int(n_a) * 3 + int(n_b)

        if n_a2 % 1 == 0 and n_b2 % 1 == 0:
            total_tokens2 += int(n_a2) * 3 + int(n_b2)

print(f"Part 1 Solution: {total_tokens}")
print(f"Part 2 Solution: {total_tokens2}")