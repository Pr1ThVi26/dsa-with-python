from collections import deque

# BFS for single connected component
def bfs(adj):
    V = len(adj)
    visited = [False] * V
    res = []

    src = 0  # Starting vertex
    q = deque()

    visited[src] = True
    q.append(src)

    while q:
        curr = q.popleft()
        res.append(curr)

        # Visit all unvisited neighbours
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

    return res


# Function to add an edge
def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


# Driver code
if __name__ == "__main__":
    V = 5

    # Create adjacency list
    adj = [[] for _ in range(V)]

    # Add edges
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 0)
    addEdge(adj, 2, 0)
    addEdge(adj, 2, 3)
    addEdge(adj, 2, 4)

    # Print adjacency list
    print("Adjacency List:")
    for i in range(V):
        print(i, "->", adj[i])

    # Perform BFS
    res = bfs(adj)

    print("\nBFS Traversal:")
    for node in res:
        print(node, end=" ")