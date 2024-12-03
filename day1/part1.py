class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
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

left_tree = BinaryTree()
right_tree = BinaryTree()

with open(input_file, "r") as f:
    for line in f:
        line_arr = line.strip().split(" ")
        left_tree.add_node(int(line_arr[0]))
        right_tree.add_node(int(line_arr[-1]))

left_arr = left_tree.inorder_traversal()
right_arr = right_tree.inorder_traversal()

distance = 0

for i in range(len(left_arr)):
    distance += abs(left_arr[i] - right_arr[i])

print(distance)