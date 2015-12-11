class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def lowestCommon(node, nodea, nodeb):
    if node == None:
        return None
    if node.value == nodea.value or node.value == nodeb.value:
        return node
    else:
        left_ret =lowestCommon(node.left, nodea, nodeb)
        right_ret = lowestCommon(node.right, nodea, nodeb)

        #Check if we found them in different subtrees
        #So this guarantees that we find the divergence point and propogate it up
        if left_ret != None and right_ret != None:
            return node
        elif left_ret != None:
            return node.left
        elif right_ret != None:
            return node.right

def main():
    """
         1
        / \
       2   3
      / \ / \
     4  5 6  7
    """
    one = Node(1)
    one.left = Node(2)
    one.left.left = Node(4)
    one.left.right = Node(5)
    one.right = Node(3)
    one.right.left = Node(6)
    one.right.right = Node(7)
    print lowestCommon(one, one.left.right, one.right.left).value
    print lowestCommon(one, one.left.left, one.left.right).value

if __name__ == "__main__":
    main()
