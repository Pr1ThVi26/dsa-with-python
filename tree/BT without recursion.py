from queue import Queue

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def create(self):
        data = int(input("Enter root value: "))

        if data == -1:
            return None

        self.root = Node(data)

        q = Queue()
        q.put(self.root)

        while not q.empty():
            current = q.get()

            # Left Child
            left_data = int(input(f"Enter left child of {current.data} (-1 for no node): "))

            if left_data != -1:
                current.left = Node(left_data)
                q.put(current.left)

            # Right Child
            right_data = int(input(f"Enter right child of {current.data} (-1 for no node): "))

            if right_data != -1:
                current.right = Node(right_data)
                q.put(current.right)

        return self.root

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

# Main Program
tree = BinaryTree()

tree.root = tree.create()

print("\nInorder Traversal:", end=" ")
tree.inorder(tree.root)

print("\nPreorder Traversal:", end=" ")
tree.preorder(tree.root)

print("\nPostorder Traversal:", end=" ")
tree.postorder(tree.root)