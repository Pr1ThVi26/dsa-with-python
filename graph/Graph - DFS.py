class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.numVertices = vertices
        self.adjLists = [None] * vertices
        self.visited = [0] * vertices


def addEdge(graph, u, v):
    # Add v to u's list
    newNode = Node(v)
    newNode.next = graph.adjLists[u]
    graph.adjLists[u] = newNode

    # Add u to v's list (undirected graph)
    newNode = Node(u)
    newNode.next = graph.adjLists[v]
    graph.adjLists[v] = newNode


def dfs(graph, vertex):
    graph.visited[vertex] = 1
    print(vertex, end=" ")

    temp = graph.adjLists[vertex]

    while temp:
        adjVertex = temp.vertex

        if graph.visited[adjVertex] == 0:
            dfs(graph, adjVertex)

        temp = temp.next


# Main Program
vertices = int(input("Enter the number of vertices: "))
graph = Graph(vertices)

edges = int(input("Enter the number of edges: "))

for i in range(edges):
    u, v = map(int, input("Enter the edge (u v): ").split())
    addEdge(graph, u, v)

startVertex = int(input("Enter the starting vertex for DFS: "))

print("DFS Traversal:", end=" ")
dfs(graph, startVertex)