class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

n = int(input("Enter number of nodes: "))

nodes = []

# Input node values
for i in range(n):
    x = int(input(f"Enter data for node {i+1}: "))
    nodes.append(Node(x))

# Connect nodes as a binary tree
for i in range(n):
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        nodes[i].left = nodes[left]

    if right < n:
        nodes[i].right = nodes[right]

root = nodes[0]

# Display all nodes without recursion
print("\nNodes are:")
for i in range(n):
    print(nodes[i].data, end=" ")