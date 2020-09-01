# I've decided to use preorder tree traversal for my solution to this problem.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    if node is None:
        return 'none'
    return f'{node.val} {serialize(node.left)} {serialize(node.right)}'

def deserialize(string):
    def helper():
        val = next(vals)
        if val == 'none':
            return None
        node = Node(val)
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(string.split())
    return helper()

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
