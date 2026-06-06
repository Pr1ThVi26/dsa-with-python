class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST:
    def create(self,root,data):
        if root == None:
            return Node(data)
        elif data<root.data:
            print(f"Data inserted at left of {root.data}")
            root.left=self.create(root.left,data)
        elif data>root.data:
            print(f"Data inserted at right of {root.data}")
            root.right=self.create(root.right,data)
        else:
            print("Duplicate data not allowed")
        return root

    def sum1(self,root):
        if root==None:
            print("Tree is empty")
            return
        l=[]
        s=0
        l.append(root)
        while l:
            temp=l.pop()
            s=s+temp.data
            if temp.right!=None:
                l.append(temp.right)
            if temp.left!=None:
                l.append(temp.left)
        return s

    def sum2(self, root):
        if root==None:
            return 0
        s=0
        s=s+self.sum2(root.left)
        s=s+root.data
        s=s+self.sum2(root.right)
        return s

tree = BST()
root=None
while True:
    data = int(input("Enter node value (-1 to stop): "))
    if data == -1:
        break
    root = tree.create(root,data)
ch=int(input("1. Sum of tree elements w/o using recursion\n2. Sum of tree elements using recursion\nEnter your choice : "))
match ch:
    case 1:
        print("Sum of tree elements : ", tree.sum1(root))
    case 2:
        print("Sum of tree elements : ", tree.sum2(root))
    case _:
        print("Invalid choice")
