# Adjacency list representation and basic operations like adding edge,
# removing edge and printing the list

# A simple dictionary of vertices and its edges is a sufficient 
# representation of a graph


class Graph:
    
    def __init__(self, nodes, isDirected = False):
        self.nodes = nodes
        self.isDirected = isDirected

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
        if not self.isDirected:
            self.adjList[v2].append(v1)

    # degree of a vertex
    def degreeVertex(self, node):
        return len(self.adjList[node])

    # print the adjacency list
    def printAdjList(self):
        for node in self.nodes:
            print(node, ":", self.adjList[node])
        print()

    # breadth first search in graph
    def bfsInGraph(self, node):

        queue = [node]
        visited = [node]

        while queue:
            curr = queue.pop(0)
            print(curr, end=" ")

            for neighbour in self.adjList[curr]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)
        print()

    # depth first search in graph
    def dfsInGraph(self, node, visited=set()):

        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            for neighbour in self.adjList[node]:
                self.dfsInGraph(neighbour, visited)
        

# driver code
def main():
    nodes = [1,2,3,4,5]
    edges = [(1,2),(1,3),(2,3),(2,4),(2,5),(3,4),(4,5)]

    g = Graph(nodes, isDirected = False)
    # g.printAdjList()

    for v1, v2 in edges:
        g.addEdge(v1, v2)

    g.printAdjList()
    
    print("degree of node %d is %d"%(nodes[1], g.degreeVertex(nodes[1])), "\n")

    print("Breadth first search for the above graph is:\n")
    g.bfsInGraph(1)
    
    print("Depth first search for the above graph is:\n")
    g.dfsInGraph(1)

if __name__ == "__main__":
    main()