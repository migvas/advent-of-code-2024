class FileBlock:
    """
    Blocks of a single file.

    Attributes:
        idx (int): Id of the file.
        files (int): Number of blocks this file takes.
        starting_pos (int): Position of the first file block in disk.
    """

    def __init__(self, idx, files, starting_pos):
        """
        Initializes the file block.

        Args:
            idx (int): Id of the file.
            files (int): Number of blocks this file takes.
            starting_pos (int): Position of the first file block in disk.
        """
        self.idx = idx
        self.files = files
        self.starting_pos = starting_pos


class EmptySpace:
    """
    Blocks of empty space.

    Attributes:
        amount (int): Number of blocks of empty space.
        starting_pos (int): Position of the first empty block in disk.
    """

    def __init__(self, amount, starting_pos):
        """
        Initializes the empty space blocks.

        Args:
            amount (int): Number of blocks of empty space.
            starting_pos (int): Position of the first empty block in disk.
        """
        self.amount = amount
        self.starting_pos = starting_pos


input_file = "input.txt"


# Part 1
def compact_hard_drive(disk_map):
    """
    Computes the filesystem checksum after the file-compacting process.
    This function moves the file blocks one at a time from the end of
    the disk to the leftmost free space block.

    Args:
        disk_map (list[str]): The map of the disk that we want to compact.

    Returns:
        int: Filesystem checksum.

    """

    # Start left pointer
    i = 0
    curr_i = int(disk_map[i])
    check_sum = 0

    # Start right pointer
    j = len(disk_map) - 1

    # Set right pointer to the first file block
    while j > 0:
        if j % 2 == 0 and int(disk_map[0]):
            break

        j -= 1

    curr_j = int(disk_map[j])

    # Start position counter
    pos = 0

    # While we have files to move
    while i < j:
        # If it is a file block index
        if i % 2 == 0:
            # If we still have file blocks
            if curr_i > 0:
                # Increment checksum, move position and remove block
                check_sum += pos * i // 2
                pos += 1
                curr_i -= 1

            # If we have processed every block
            else:
                # Increment pointer
                i += 1
                curr_i = int(disk_map[i])
        # If it is an empty space block
        else:
            # If we don't have file blocks to process on the right pointer
            if curr_j == 0:
                # Move pointer to next file block
                j -= 2
                curr_j = int(disk_map[j])
            # If we still have empty space
            elif curr_i > 0:
                # Increment checksum, move position and remove block from empty
                # and from current file block
                check_sum += pos * j // 2
                pos += 1
                curr_i -= 1
                curr_j -= 1
            # If we have processed every block
            else:
                # Increment pointer
                i += 1
                curr_i = int(disk_map[i])

    # If both pointers are on the same block
    if i == j:
        # It is a file block so we have to add it to the checksum
        for _ in range(curr_j):
            check_sum += pos * i // 2
            pos += 1
            curr_i -= 1

    # Return checksum
    return check_sum


# Part 2
def compact_hard_drive_2(disk_map):
    """
    Computes the filesystem checksum after the file-compacting process.
    This function attempts to move whole files to the leftmost span of free
    space blocks that could fit the file. Attempt to move each file exactly
    once in order of decreasing file ID number starting with the file with the
    highest file ID number. If there is no span of free space to the left of a file
    that is large enough to fit the file, the file does not move.

    Args:
        disk_map (list[str]): The map of the disk that we want to compact.

    Returns:
        int: Filesystem checksum.

    """
    check_sum = 0

    # Arrays to hold FileBlock and EmptySpace instances
    file_blocks = []
    empty_space = []

    # Start position counter
    pos = 0

    # Fill the arrays
    for i, n in enumerate(disk_map):
        if i % 2 == 0:
            file_blocks.append(FileBlock(i // 2, int(n), pos))
        else:
            empty_space.append(EmptySpace(int(n), pos))
        pos += int(n)

    # Loop through the file block array backwards
    for j in range(len(file_blocks) - 1, -1, -1):
        current_block = file_blocks[j]
        # Search empty space until current file block
        for k in range(current_block.idx):
            # If empty space is enough
            if empty_space[k].amount >= current_block.files:
                # Move file block to empty space and reduce empty space
                current_block.starting_pos = empty_space[k].starting_pos
                empty_space[k].amount -= current_block.files
                empty_space[k].starting_pos += current_block.files
                break

    # Loop through the file blocks and add to checksum
    for fb in file_blocks:
        for m in range(fb.files):
            check_sum += fb.idx * (fb.starting_pos + m)

    # Return checksum
    return check_sum


with open(input_file, "r", encoding="utf-8") as f:
    # Create a variable with all the data from the file
    file_data = f.read().strip()

print(f"Part 1 Solution: {compact_hard_drive(file_data)}")
print(f"Part 2 Solution: {compact_hard_drive_2(file_data)}")
