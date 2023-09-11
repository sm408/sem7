# Adjacency Matrix representation of a graph
class Graph:
    # self represents the instance of the class.
    # By using the “self” keyword we can access the
    # attributes and methods of the class in python.
    # It binds the attributes with the given arguments.

    # This constructor is used to initialize the adjacecny matrix
    # with 0.
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # This function prints the adjacency matrix of the graph
    # Due to two nested loops, it is O(V^2)
    def printGraph(self):
        print("\nAdjacency Matrix:")
        for i in range(self.V):
            for j in range(self.V):
                print(self.graph[i][j], end=" ")
            print()

    # This function is used to add an edge
    # between vertices v and w.
    # This implementation is for undirected graph
    def addEdge(self, v, w):
        print("Adding an edge between", v, "and", w, "and between", w, "and", v)
        self.graph[v][w] = 1
        self.graph[w][v] = 1

    # This function is used to add a
    # vertex to the graph.
    def addVertex(self, v):
        self.V += 1
        for i in range(self.V):
            self.graph[i].append(0)
        self.graph.append([0 for column in range(self.V)])


if __name__ == "__main__":
    # Initialize the graph with 7 vertices
    g = Graph(7)

    # An edge between 0 and 1 and between 1 and 0 will be created
    # g.addEdge(0, 1)

    g.addEdge(1,2)
    g.addEdge(1,5)
    g.addEdge(1,4)
    g.addEdge(4,2)
    g.addEdge(4,6)
    g.addEdge(5,2)
    g.addEdge(5,3)

    g.printGraph()

