from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return root
    queue = deque()
    queue.append(root)
    while queue:
        cur = queue.popleft()
        temp = cur.left
        cur.left = cur.right
        cur.right = temp
        if cur.left is not None:
            queue.append(cur.left)
        if cur.right is not None:
            queue.append(cur.right)
    return root
