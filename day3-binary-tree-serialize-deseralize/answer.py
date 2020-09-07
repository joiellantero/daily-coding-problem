# I've decided to use preorder tree traversal for my solution to this problem.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# concatenate each nodes of the binary tree into a string
def serialize(node):
    # if the node is empty, put the none string placeholder
    if node is None:
        return 'none'
        
    # put everything in a string
    return f'{node.val} {serialize(node.left)} {serialize(node.right)}'

# format the string back into a binary tree by using recursion
def deserialize(string):
    def helper():
        # at first iter, get first val. at succeeding iter, get next val.
        val = next(vals)

        # detect if the node has the string none. If so, return Nonetype.
        if val == 'none':
            return None

        # place the value in the node
        node = Node(val)

        # do recursion to place left node val
        node.left = helper()

        # do recursion to place right node val
        node.right = helper()
        return node

    # the deserialize function will begin by splitting the string by the spaces and get each element
    vals = iter(string.split())

    # return the binary tree
    return helper()

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
