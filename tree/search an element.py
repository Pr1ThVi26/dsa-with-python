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

    def search(self,root):
        if root==None:
            print("Tree is empty")
            return
        e,o=0,0
        l=[]
        l.append(root)
        ele=int(input("Enter element to search : "))
        while l:
            temp=l.pop()
            if ele==temp.data:
                print("Element found!")
            else:
                print("Element not found")
            if temp.right!=None:
                l.append(temp.right)
            if temp.left!=None:
                l.append(temp.left)

tree = BST()
root=None
while True:
    data = int(input("Enter node value (-1 to stop): "))
    if data == -1:
        break
    root = tree.create(root,data)
tree.search(root)