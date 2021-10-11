# A binary tree is a tree data structure in which each parent node can have 
# at most two children. Each node of a binary tree consists of three 
# items: 1. data item, 2.address of left child, 3.address of right child

# Below is the implementation of a Binary Tree (BT) in Python3 along with
# methods to traverse the nodes of the tree

# Class to represent a node of tree
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# In-Order Traversal (visit left child, root and then right child)
def inOrder_traversal(root):
    
    if root:
        inOrder_traversal(root.left)
        print(root.data, end=" ")
        inOrder_traversal(root.right)

# Pre-Order Traversal (visit root, left child and then right child)
def preOrder_traversal(root):
    
    if root:
        print(root.data, end=" ")
        preOrder_traversal(root.left)
        preOrder_traversal(root.right)

# Post-Order Traversal (visit left child, right child and root)
def postOrder_traversal(root):
    
    if root:
        postOrder_traversal(root.left)
        postOrder_traversal(root.right)
        print(root.data, end=" ")


# driver code
def main():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Inorder traversal ")
    inOrder_traversal(root)

    print("\nPreorder traversal ")
    preOrder_traversal(root)

    print("\nPostorder traversal ")
    postOrder_traversal(root)


if __name__ == "__main__":

    main()