n = int(input("Enter number of nodes: "))
tree = []
for i in range(n):
    x = int(input(f"Enter data for node {i+1}: "))
    tree.append(x)
print("\nBinary Tree:")
for i in range(n):
    print(f"\nNode = {tree[i]}")
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n:
        print("Left Child =", tree[left])
    else:
        print("Left Child = None")
    if right < n:
        print("Right Child =", tree[right])
    else:
        print("Right Child = None")