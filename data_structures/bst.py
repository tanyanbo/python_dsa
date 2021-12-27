class BSTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left: BSTNode = left
        self.right: BSTNode = right


def insert(root: BSTNode, val):
    if not root:
        return BSTNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def deleteNode(root: BSTNode, val):
    if not root:
        return None
    if root.val == val:
        if not root.right and not root.left:
            root = None
        elif (root.right and not root.left) or (root.left and not root.right):
            if root.right:
                root = root.right
            else:
                root = root.left
        else:
            temp = root.right
            while temp.left and temp.left.left:
                temp = temp.left
            if temp.left:
                root.val = temp.left.val
            else:
                root.val = temp.val
                root.right = None
                return root
            temp.left = None
        return root
    root.left = deleteNode(root.left, val)
    root.right = deleteNode(root.right, val)
    return root
