# Adjacency matrix representation and basic operations like adding edge,
# removing edge and printing the matrix

class Graph:
    
    def __init__(self, size):
        self.adjMatrix = []

        # creating a square matrix with 0's
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])

        self.size = size

    # adding an edge to an adjaceny matrix
    def addEdge(self, v1, v2):
        # if both vertices are identical, exit the operation
        if v1 == v2:
            print("identical vertices v1=%d and v2=%d passed\n"%(v1, v2))
            return

        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1 

    # removing an edge from an adjaceny matrix
    def removeEdge(self, v1, v2):
        # if both vertices are identical, exit the operation
        if v1 == v2:
            print("identical vertices v1=%d and v2=%d passed\n"%(v1, v2))
            return
            
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
    
    # return the lenght of adjacency matrix
    def __len__(self):
        return self.size

    # print the adjacency matrix
    def printMatrix(self):
        for row in self.adjMatrix:
            for val in row:
                # formatting value with two spaces
                print('{:2}'.format(val), end=" ")
            print()
        print()


# driver code to test the graph implemetation
def main():

    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,4)
    g.addEdge(2,3)
    # g.addEdge(1,1)
    
    g.printMatrix()
    
    g.removeEdge(1,2)

    g.printMatrix()

if __name__ == '__main__':

    main()