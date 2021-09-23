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

#function for BFS using queue
def breadth_first_search(root, q):

    if q.empty():
        return

    root = q.get()              #pop the first element from queue and print
    print(root.data,end=" ")

    if root.left != None:       #if root has left and right chilrens, put to queue
        q.put(root.left)
    if root.right != None:
        q.put(root.right)
    
    breadth_first_search(root, q)   #recursive call to get child and find its children


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
breadth_first_search(root, q)