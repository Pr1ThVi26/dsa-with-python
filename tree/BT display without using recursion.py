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

    def preorder(self,root):
        #root->leff->right
        if root==None:
            print("Tree is empty")
            return
        l=[]
        l.append(root)
        while l:
            temp=l.pop()
            print(temp.data,end=" ")
            if temp.right!=None:
                l.append(temp.right)
            if temp.left!=None:
                l.append(temp.left)

tree = BinaryTree()
tree.root = tree.create()
print("\nPreorder Traversal:", end=" ")
tree.preorder(tree.root)