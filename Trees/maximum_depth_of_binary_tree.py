from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(self, root: Optional[TreeNode]) -> int:
    def get_depth(node: TreeNode) -> int:
        if node is None:
            return 0
        depth = 1
        return depth + max(get_depth(node.left), get_depth(node.right))
    return get_depth(root)


