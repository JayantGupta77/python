class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(18)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

inorder(root)  # Output: 3 5 7 10 15 18