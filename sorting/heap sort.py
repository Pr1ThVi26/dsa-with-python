class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinaryTree:
    def create(self):
        data = int(input("Enter node value (-1 for no node): "))

        if data == -1:
            return None

        root = Node(data)

        print("Left child of", data)
        root.left = self.create()

        print("Right child of", data)
        root.right = self.create()

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

tree = BinaryTree()

print("Create Binary Tree")
root = tree.create()

print("\nInorder Traversal:")
tree.inorder(root)
