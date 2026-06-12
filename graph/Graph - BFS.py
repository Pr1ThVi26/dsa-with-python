class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.numVertices = vertices
        self.adjLists = [None] * vertices
        self.visited = [0] * vertices


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.isEmpty():
            return -1
        return self.items.pop(0)


def addEdge(graph, u, v):
    newNode = Node(v)
    newNode.next = graph.adjLists[u]
    graph.adjLists[u] = newNode

    newNode = Node(u)
    newNode.next = graph.adjLists[v]
    graph.adjLists[v] = newNode


def bfs(graph, startVertex):
    queue = Queue()

    graph.visited[startVertex] = 1
    queue.enqueue(startVertex)

    while not queue.isEmpty():
        currentVertex = queue.dequeue()
        print(currentVertex, end=" ")

        temp = graph.adjLists[currentVertex]

        while temp:
            adjVertex = temp.vertex

            if graph.visited[adjVertex] == 0:
                graph.visited[adjVertex] = 1
                queue.enqueue(adjVertex)

            temp = temp.next


vertices = int(input("Enter the number of vertices: "))
graph = Graph(vertices)

edges = int(input("Enter the number of edges: "))

for i in range(edges):
    u, v = map(int, input("Enter the edge (u v): ").split())
    addEdge(graph, u, v)

startVertex = int(input("Enter the starting vertex for BFS: "))

print("BFS Traversal:", end=" ")
bfs(graph, startVertex)