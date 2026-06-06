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

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

# Main Program
tree = BinaryTree()

print("Create Binary Tree")
root = tree.create()

print("\nInorder Traversal:")
tree.inorder(root)

print("\nPreorder Traversal:")
tree.preorder(root)

print("\nPostorder Traversal:")
tree.postorder(root)