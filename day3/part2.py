import re

input_file = "input.txt"

with open(input_file, "r") as f:
    # Create a variable with all the data from the file
    file_data = f.read()

# Use regex to find all occurrences of mul(3 digits, 3 digits), don't() and do()
valid_mul = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)|don't\\(\\)|do\\(\\)", file_data)

# Start counter
instruction_sum = 0

# Variable that controls if we should perform mul or not
stop_validation = False

for inst in valid_mul:
    match inst:
        # We have to stop the next validations
        case "don't()":
            stop_validation = True
        
        # Turn the validation back on
        case "do()":
            stop_validation = False

        # Perform validation
        case _:
            # If stop_validation is True then ignore this step
            if not stop_validation:
                d1, d2 = inst[4:-1].split(",")
                instruction_sum += (int(d1) * int(d2))


print(instruction_sum)