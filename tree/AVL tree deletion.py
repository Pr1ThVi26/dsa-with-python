class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1   # AVL requires height

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Right Rotation (LL Case)
    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # Left Rotation (RR Case)
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # Insert with AVL balancing
    def insert(self, root, key):
        # Standard BST insertion
        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Balance factor
        balance = self.get_balance(root)

        # 4 Cases
        # LL
        if balance > 1 and key < root.left.data:
            return self.right_rotate(root)

        # RR
        if balance < -1 and key > root.right.data:
            return self.left_rotate(root)

        # LR
        if balance > 1 and key > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL
        if balance < -1 and key < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def AVLdelete(self,root,data):
        if root==None:
            print("Data not found!")
            return root
        if data<root.data:
            root.left=self.AVLdelete(root.left, data)
        elif data>root.data:
            root.right=self.AVLdelete(root.right, data)
        else:
            if root.left==None and root.right==None:
                print(f"{root.data} is deleted")
                print("Deleted node is a leaf node")
                return None
            elif root.left==None:
                print(f"{root.data} is deleted")
                print("Deleted node has one child")
                return root.right
            elif root.right==None:
                print(f"{root.data} is deleted")
                print("Deleted node has one child")
                return root.left
            else:
                print(f"{root.data} is deleted")
                temp=root.left
                while temp.right!=None:
                    temp=temp.right
                root.data=temp.data
                root.left=self.AVLdelete(root.left, temp.data)
        return root

# Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# ------------ MAIN PROGRAM ----------------
avl = AVLTree()
root = None
print("Enter numbers for AVL Tree (type 'done' to finish):")
while True:
    value = input("Enter data: ")
    if value.lower() == "done":
        break
    root = avl.insert(root, int(value))
print("\nInorder Traversal of AVL Tree:")
inorder(root)
print()
ch=input("\nDo you want to delete any Data? (y/n) : ")
while ch=='y' or ch=='Y':
    ele=int(input("Data to be deleted : "))
    root=avl.AVLdelete(root, ele)
    print("Current Tree:")
    inorder(root)
    ch=input("\nContinue deleting Data? (y/n) : ")
print("Final Tree:")
inorder(root)