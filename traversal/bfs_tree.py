### BREADTH FIRST SEARCH (BFS) in BINARY TREE (BT)
##  BFS is also known as Level Order Traversal. Each level of BT is traversed 
##  completely from left most to right most and then next level is traversed and so on..
#   Time Complexity: O(n) where n is the number of nodes
#   Space complexity: O(n) where n is the number of nodes

from queue import Queue

#creating node structure
class Node:
    
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

#function for BFS using queue and recursive  approach
def breadth_first_search_recursive(root, q):

    if q.empty():
        return

    root = q.get()              #pop the first element from queue and print
    print(root.data,end=" ")

    if root.left != None:       #if root has left and right childrens, put to queue
        q.put(root.left)
    if root.right != None:
        q.put(root.right)
    
    breadth_first_search_recursive(root, q)   #recursive call to get child and find its children


#function for BFS using queue and iterative approach
def breadth_first_search_iterative(root):

    if root is None:
        return

    q = []                          #using list for q implementation
    q.append(root)                  #enqueuing/putting root of the tree to the queue

    while(len(q) > 0):              #until queue is not empty, pop the first enqueued
                                    #item and find the children and put into queue
        print(q[0].data, end=" ")
        node = q.pop(0)

        if node.left is not None:
            q.append(node.left)

        if node.right is not None:
            q.append(node.right)


#Driver Program                     #       Tree Structure
root = Node(1)                      #           1
root.left = Node(2)                 #         /   \
root.right = Node(3)                #        2     3       
root.left.left = Node(4)            #       / \   / \
root.left.right = Node(5)           #      4   5 6   7
root.right.left = Node(6)
root.right.right = Node(7)          

#initializing q using Queue class from queue libary
q = Queue(maxsize=0)    # initializing with infinite size limit

q.put(root)
breadth_first_search_recursive(root, q)
print()
breadth_first_search_iterative(root)