"""
Write a functionn that takes the input node of the binary tree as input and
returns whether the tree is symettric or not.
"""

def symettryChecker(leftnode, rightnode):

    if leftnode == None or rightnode == None:
         if leftnode == None and rightnode == None:
             return True
         return False
    else:
        if leftnode.value == rightnode.value:
            return (symettryChecker(leftnode.left, rightnode.right) \
            and symettryChecker(leftnode.right, rightnode.left))
        else:
            return False

def symMain(root):
    return symettryChecker(root.left, root.right)

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def main():
    """
        1
       / \
      2   2
     / \  / \
    1   3 3  1
    """
    rootNode = Node(1)
    rootNode.left = Node(2)
    rootNode.left.left = Node(1)
    rootNode.left.right = Node(3)
    rootNode.right = Node(2)
    rootNode.right.left = Node(3)
    rootNode.right.right = Node(1)
    print symMain(rootNode)
    rootNode.right.right = None
    print symMain(rootNode)
main()
