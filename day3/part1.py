import re

input_file = "day3/input.txt"

with open(input_file, "r") as f:
    # Create a variable with all the data from the file
    file_data = f.read()

# Use regex to find all occurrences of mul(3 digits, 3 digits)
valid_mul = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)", file_data)

# Start counter
instruction_sum = 0

# For each valid occurrence
for inst in valid_mul:
   # Since we always have the following structure "mul(x, y)" we know that
   # the digits are always between the position of the first ( + 1 and
   # the last ) - 1
   d1, d2 = inst[4:-1].split(",")

   # Just sum the product of the two digits to the counter
   instruction_sum += (int(d1) * int(d2))

print(instruction_sum)