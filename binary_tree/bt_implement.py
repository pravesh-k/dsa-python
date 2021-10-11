class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrder_traversal(root):
    
    if root:
        inOrder_traversal(root.left)
        print(root.data, end=" ")
        inOrder_traversal(root.right)


def preOrder_traversal(root):
    
    if root:
        print(root.data, end=" ")
        preOrder_traversal(root.left)
        preOrder_traversal(root.right)


def postOrder_traversal(root):
    
    if root:
        postOrder_traversal(root.left)
        postOrder_traversal(root.right)
        print(root.data, end=" ")


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