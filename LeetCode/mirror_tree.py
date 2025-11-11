class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirror_tree(root):
    if root is None:
        return None

    # Swap left and right subtrees
    root.left, root.right = mirror_tree(root.right), mirror_tree(root.left)
    return root

# Helper function to print in-order traversal
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)

# Sample tree
#       1
#     /   \
#    2     3
#   / \   / \
#  4   5 6   7

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Original Inorder Traversal:")
inorder_traversal(root)

mirror_tree(root)

print("\nMirrored Inorder Traversal:")
inorder_traversal(root)