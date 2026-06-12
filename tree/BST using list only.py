tree = []
def insert(data):
    global tree
    if len(tree) == 0:
        tree.append(data)
        return
    i = 0
    while True:
        if data < tree[i]:
            child = 2 * i + 1
        elif data > tree[i]:
            child = 2 * i + 2
        else:
            print("Duplicate not allowed")
            return
        while child >= len(tree):
            tree.append(None)
        if tree[child] is None:
            tree[child] = data
            return
        i = child

n = int(input("Enter number of nodes: "))
for i in range(n):
    x = int(input("Enter value: "))
    insert(x)
print("BST stored in list:")
print(tree)