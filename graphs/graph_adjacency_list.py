# Adjacency list representation and basic operations like adding edge,
# removing edge and printing the list

# A simple dictionary of vertices and its edges is a sufficient 
# representation of a graph


class Graph:
    
    def __init__(self, nodes):
        self.nodes = nodes

        # creating an empty dictionary for representing a graph
        self.adjList = {}

        # adding the nodes as key with empty values in the dictionary
        for node in self.nodes:
            self.adjList[node] = []

    def addEdge(self, v1, v2):
        # if both vertices are identical, exit the operation
        if v1 == v2:
            print("identical vertices v1=%d and v2=%d passed\n"%(v1, v2))
            return

        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)

    # print the adjacency list
    def printAdjList(self):
        for node in self.nodes:
            print(node, ": ", self.adjList[node])
        print()


# driver code
def main():
    nodes = [1,2,3,4,5]
    edges = [(1,2),(1,3),(2,3),(2,4),(2,5),(3,4),(4,5)]
    g = Graph(nodes)
    g.printAdjList()

    for v1, v2 in edges:
        g.addEdge(v1, v2)

    g.printAdjList()

if __name__ == "__main__":
    main()