# ***************************************************
# *  Program Title: Binary Search Tree Builder
# *  Author: Hunter Duffek
# *  Class: CSCI3320,  Fall 2022
# *  Assignment #2
# ****************************************************


# A class to store a BST node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Function to perform inorder traversal on the BST
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)


# Function to find the maximum value node in the subtree rooted at `ptr`
def findMaximumKey(ptr):
    while ptr.right:
        ptr = ptr.right
    return ptr


# Recursive function to insert a key into a BST
def insert(root, key):
    # if the root is None, create a new node and return it
    if root is None:
        return Node(key)

    # if the given key is less than the root node, recur for the left subtree
    if key < root.data:
        root.left = insert(root.left, key)

    # if the given key is more than the root node, recur for the right subtree
    else:
        root.right = insert(root.right, key)

    return root


# Function to delete a node from a BST
def deleteNode(root, key):
    # base case: the key is not found in the tree
    if root is None:
        return root

    # if the given key is less than the root node, recur for the left subtree
    if key < root.data:
        root.left = deleteNode(root.left, key)

    # if the given key is more than the root node, recur for the right subtree
    elif key > root.data:
        root.right = deleteNode(root.right, key)

    # key found
    else:

        # Case 1: node to be deleted has no children (it is a leaf node)
        if root.left is None and root.right is None:
            # update root to None
            return None

        # Case 2: node to be deleted has two children
        elif root.left and root.right:
            # find its inorder predecessor node
            predecessor = findMaximumKey(root.left)

            # copy value of the predecessor to the current node
            root.data = predecessor.data

            # recursively delete the predecessor. Note that the
            # predecessor will have at most one child (left child)
            root.left = deleteNode(root.left, predecessor.data)

        # Case 3: node to be deleted has only one child
        else:
            # choose a child node
            child = root.left if root.left else root.right
            root = child

    return root


# ***************************************************
# *  FUNCTION  numTwoChildrenNodes :
# *    Recursive function to print BST in descending order
# *  INPUT PARAMETERS :
# *    root - current node
# *  OUTPUT :
# *    prints BST nodes in descending order
# ****************************************************

def printNode(root):
    if root is None:
        return
    printNode(root.right)  # Finds highest value node first
    print(root.data, end=' ')
    printNode(root.left)  # Finds next highest value node


# ***************************************************
# *  FUNCTION  numTwoChildrenNodes :
# *    Recursive function to count number of leaf nodes in BST
# *  INPUT PARAMETERS :
# *    root - current node
# *  OUTPUT :
# *    returns number of leaf nodes
# ****************************************************

def numLeaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:  # Both children must be empty to be a leaf node
        return 1
    return numLeaves(root.left) + numLeaves(root.right)


# ***************************************************
# *  FUNCTION  numTwoChildrenNodes :
# *    Recursive function to count number of one child nodes in BST
# *  INPUT PARAMETERS :
# *    root - current node
# *  OUTPUT :
# *    returns number of one-child nodes
# ****************************************************

def numOneChildNodes(root):
    numChild = 0
    if root is None:
        return 0
    if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
        # One of the two children nodes must be empty to be a one-child node
        numChild += 1
    return numOneChildNodes(root.left) + numOneChildNodes(root.right) + numChild


# ***************************************************
# *  FUNCTION  numTwoChildrenNodes :
# *    Recursive function to count nodes with two children in BST
# *  INPUT PARAMETERS :
# *    root - current node
# *  OUTPUT :
# *    returns number of two-child nodes
# ****************************************************

def numTwoChildrenNodes(root):
    numTwoChild = 0
    if root is None:
        return 0
    if root.left is not None and root.right is not None:
        #  Both children nodes must be occupied to be a two-child node
        numTwoChild += 1
    return numTwoChildrenNodes(root.left) + numTwoChildrenNodes(root.right) + numTwoChild


# ***************************************************
# *  FUNCTION  levelOrder :
# *    Function to print BST in level order
# *  INPUT PARAMETERS :
# *    root - current node
# *  OUTPUT :
# *    returns printed BST in level order
# ****************************************************

def levelOrder(root):
    level = 1
    if root is None:
        return 0
    while currLevel(root, level):  # While loop goes through each level of BST till each node is in level order
        level += 1


# ***************************************************
# *  FUNCTION  currLevel :
# *    Recursive function to print key based on current level in BST
# *  INPUT PARAMETERS :
# *    root - current node, level - current level in BST
# *  OUTPUT :
# *    returns left or right node based on current level
# ****************************************************

def currLevel(root, level):
    if root is None:
        return False  # Breaks out of while loop in previous function, node is empty
    if level == 1:
        print(root.data, end=' ')
        return True  # Continues recursive function while printing current node

    #  Recursive calls to decrease levels till in order, then nodes are printed
    left = currLevel(root.left, level - 1)
    right = currLevel(root.right, level - 1)
    return left or right


# ***************************************************
# *  FUNCTION  printBetween :
# *    Recursive function to print between given k1 and k2 element in BST
# *  INPUT PARAMETERS :
# *    root - current node, k1 - first input parameter, k2 - second input parameter
# *  OUTPUT :
# *    printed values between k1 and k2
# ****************************************************

def printBetween(root, k1, k2):
    if root is None:
        return 0

    #  Recursion to find numbers between k1 and k2
    if k1 < root.data:
        printBetween(root.left, k1, k2)
    if k1 <= root.data <= k2:
        print(root.data, end=' ')
    if k2 > root.data:
        printBetween(root.right, k1, k2)


if __name__ == '__main__':
    while True:
        print(">> Enter choice [1-8] from menu below:\n")
        print(
            "1.Construct a Tree \n2.Print tree in a descending order \n3.Print number of leaves in tree \n4.Print the "
            "number of nodes in T that contain only one child \n5.Print the number of nodes in T that contain only "
            "two children \n6.Print the level order traversal of the tree \n7.Print all elements in the tree between "
            "k1 and k2 \n8.Exit program")
        choice = int(input())
        if choice == 1:
            keys = list(map(int, input("Enter initial elements: ").split()))
            root = None
            for key in keys:
                root = insert(root, key)
        elif choice == 2:
            print("\n Print in Descending order: ", end="")
            printNode(root)
            print()
        elif choice == 3:
            leaves = numLeaves(root)
            print("Number of leaves: " + str(leaves))
        elif choice == 4:
            print("Number of nodes with one child: " + str(numOneChildNodes(root)))
        elif choice == 5:
            print("Number of nodes with two children: " + str(numTwoChildrenNodes(root)))
        elif choice == 6:
            print("\nPrint in level order: ", end="")
            levelOrder(root)
            print()
        elif choice == 7:
            k1 = int(input("Enter k1: "))
            k2 = int(input("Enter k2: "))
            print(f"\nPrint between {k1} and {k2}: ", end="")
            printBetween(root, k1, k2)
            print()
        elif choice == 8:
            print("Goodbye!\n")
            break
