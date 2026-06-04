class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(int(input("Enter root node: ")))

n = int(input("How many nodes to add? "))

for i in range(n):
    parent = int(input("\nEnter parent node value: "))
    child = int(input("Enter child node value: "))
    pos = input("Add Left(L) or Right(R)? ").upper()

    # Find parent node manually
    stack = [root]

    while stack:
        temp = stack.pop()

        if temp.data == parent:
            if pos == 'L':
                temp.left = Node(child)
            elif pos == 'R':
                temp.right = Node(child)
            break

        if temp.right:
            stack.append(temp.right)

        if temp.left:
            stack.append(temp.left)

# Display nodes
print("\nTree Nodes:")
stack = [root]

while stack:
    temp = stack.pop()
    print(temp.data, end=" ")

    if temp.right:
        stack.append(temp.right)

    if temp.left:
        stack.append(temp.left)