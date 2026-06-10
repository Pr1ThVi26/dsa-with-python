class Node:
    def __init__(self,value):
        self.data= value
        self.left=None
        self.right=None


class BST:
    def create(self,root,data):
        if root==None:
            return Node(data)
        elif data<root.data:
            print(f"Data inserted at left of {root.data}")
            root.left=self.create(root.left, data)
        elif data>root.data:
            print(f"Data inserted at right of {root.data}")
            root.right=self.create(root.right, data)
        else:
            print("Duplicate data not allowed")
        return root

    def inorder(self,root):
        if root!=None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def delete(self,root,data):
        if root==None:
            print("Data not found!")
            return root
        if data<root.data:
            root.left=self.delete(root.left, data)
        elif data>root.data:
            root.right=self.delete(root.right, data)
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
                root.left=self.delete(root.left, temp.data)
        return root

print("Create Binary Search Tree")
tree=BST()
root=None
while True:
    data=int(input("Enter node value (-1 to stop): "))
    if data==-1:
        break
    root=tree.create(root, data)
print("Display Tree:")
tree.inorder(root)
ch=input("\nDo you want to delete any Data? (y/n) : ")
while ch=='y' or ch=='Y':
    ele=int(input("Data to be deleted : "))
    root=tree.delete(root, ele)
    print("Current Tree:")
    tree.inorder(root)
    ch=input("\nContinue deleting Data? (y/n) : ")
print("Final Tree:")
tree.inorder(root)