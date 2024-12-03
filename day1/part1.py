class Node:
    """
    Node in a binary tree.

    Attributes:
        value (int): The value of the node.
        left (Node): The left child of the node.
        right (Node): The right child of the node.
    """
    def __init__(self, value):
        """
        Initializes a Node with a given value.

        Args:
            value (int): The value to store in the node.
        """
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
    Represents a binary search tree.

    Attributes:
        root (Node): The root node of the binary tree.
    """
    def __init__(self):
        """
        Initializes an empty tree.
        """
        self.root = None

    def add_node(self, value):
        """
        Adds a node with the specified value to the binary search tree.

        If the tree is empty, the new node becomes the root. Otherwise, it is
        added to the appropriate position in the tree based on its value.

        Args:
            value (int): The value of the node to add.
        """
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return
        
        curr_node = self.root

        while 1:
            if value > curr_node.value:
                if not curr_node.right:
                    curr_node.right = new_node
                    return
                curr_node = curr_node.right
            else:
                if not curr_node.left:
                    curr_node.left = new_node
                    return
                curr_node = curr_node.left

    def inorder_traversal(self):
        """
        Performs an in-order traversal of the binary search tree.

        Returns:
            list[int]: A list of node values in in-order sequence.
        """
        tree_arr = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            tree_arr.append(node.value)
            dfs(node.right)

        dfs(self.root)
        return tree_arr

input_file = "input.txt"

# Create tree for left side and right side of the input list
left_tree = BinaryTree()
right_tree = BinaryTree()

with open(input_file, "r") as f:
    for line in f:
        # For each line in file add node to both trees
        line_arr = line.strip().split(" ")
        left_tree.add_node(int(line_arr[0]))
        right_tree.add_node(int(line_arr[-1]))

# Get the values from both trees in ascending order
left_arr = left_tree.inorder_traversal()
right_arr = right_tree.inorder_traversal()

distance = 0

for i in range(len(left_arr)):
    # For each position add the distance between the two values
    distance += abs(left_arr[i] - right_arr[i])

print(distance)