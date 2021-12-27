from typing import List, Union
import sys


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1 2 4 -1 -1 5 7 -1 -1 -1 3 -1 6 -1 -1
def buildTree(val: List[int]) -> Union[TreeNode, None]:
    if val[0] == -1:
        val.pop(0)
        return None
    root = TreeNode(val[0])
    val.pop(0)
    if len(val) <= 0:
        return root
    root.left = buildTree(val)
    if len(val) <= 0:
        return root
    root.right = buildTree(val)
    return root


# 1 2 3 4 5 -1 6 -1 -1 7 -1 -1 -1 -1 -1
def levelOrderBuildTree(val: List[int]) -> Union[TreeNode, None]:
    root = TreeNode(val[0])
    val.pop(0)
    q = [root]
    while len(q) > 0:
        popped = q.pop(0)
        if len(val) > 0:
            x = val.pop(0)
            popped.left = TreeNode(x) if x != -1 else None
            if popped.left is not None:
                q.append(popped.left)
        if len(val) > 0:
            x = val.pop(0)
            popped.right = TreeNode(x) if x != -1 else None
            if popped.right is not None:
                q.append(popped.right)

    return root


def levelOrderTraversal(root: TreeNode):
    q = [root]
    res = []
    while len(q) > 0:
        popped = q.pop(0)
        if popped.left:
            q.append(popped.left)
        if popped.right:
            q.append(popped.right)
        res.append(popped.val)
    return res
