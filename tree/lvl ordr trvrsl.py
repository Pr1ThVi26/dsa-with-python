class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Create 5 nodes
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

# Level Order Traversal (Without Recursion)
queue = []

queue.append(root)

print("Binary Tree Nodes:")

while queue:
    temp = queue.pop(0)
    print(temp.data, end=" ")

    if temp.left:
        queue.append(temp.left)

    if temp.right:
        queue.append(temp.right)