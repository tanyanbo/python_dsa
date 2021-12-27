from data_structures.bst import BSTNode, insert, deleteNode
from data_structures.graph import Graph
from data_structures.tree import (
    buildTree,
    levelOrderTraversal,
    TreeNode,
    levelOrderBuildTree,
)
from data_structures.linked_list import ListNode
from typing import List, Optional
import sys
from copy import deepcopy


# 1 2 4 -1 -1 5 7 -1 -1 -1 3 -1 6 -1 -1
# print(levelOrderTraversal(descendentSum(root)))
def helper(root: TreeNode):
    # base case
    if not root:
        return 0
    if not root.right and not root.left:
        return root.val
    # rec case
    root.val += helper(root.left) + helper(root.right)
    return root.val


def subtractOriginal(root: TreeNode, newRoot: TreeNode):
    if root is None:
        return
    if root.left is None and root.right is None:
        return
    newRoot.val -= root.val
    subtractOriginal(root.left, newRoot.left)
    subtractOriginal(root.right, newRoot.right)


def descendentSum(root: TreeNode):
    newRoot = deepcopy(root)
    helper(newRoot)
    subtractOriginal(root, newRoot)
    return newRoot


root = levelOrderBuildTree([0, 1, -1, 3, 2])


def maxSubsetSum(root: Optional[TreeNode]) -> (int, int):
    if not root:
        return 0, 0
    if not root.left and not root.right:
        return root.val, 0
    left_inc, left_exc = maxSubsetSum(root.left)
    right_inc, right_exc = maxSubsetSum(root.right)
    return (
        root.val + left_exc + right_exc,
        max(left_inc, left_exc) + max(right_inc, right_exc),
    )


# class Solution:
# def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
def printKthLevel(root: Optional[TreeNode], k: int):
    if k == 0:
        return [root]
    s1: List[TreeNode] = [root.left, root.right]
    s2: List[TreeNode] = []
    k -= 1
    cur = "s1"
    while k > 0:
        if cur == "s1":
            while len(s1) > 0:
                popped = s1.pop()
                if popped and popped.left:
                    s2.append(popped.left)
                if popped and popped.right:
                    s2.append(popped.right)
            cur = "s2"
        else:
            while len(s2) > 0:
                popped = s2.pop()
                if popped and popped.left:
                    s1.append(popped.left)
                if popped and popped.right:
                    s1.append(popped.right)
            cur = "s1"
        k -= 1
    if cur == "s1":
        return s1
    else:
        return s2


def findAncestors(root: TreeNode, target: int, state: bool, res: List[TreeNode]):
    if not root:
        return res, False
    if not root.left and not root.right:
        return res, True if root.val == target else False
    if root.val != target:
        res, state = findAncestors(root.left, target, state, res)
        if state:
            res.append(root)
            return res, True
        res, state = findAncestors(root.right, target, state, res)
        if state:
            res.append(root)
            return res, True
    else:
        return res, True


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = printKthLevel(target, k)
        result = [x.val for x in res if x]
        ancestors, _ = findAncestors(root, target.val, False, [])
        for idx, ancestor in enumerate(ancestors):
            temp = printKthLevel(ancestor, k - idx - 1)
            for i in temp:
                result.append(i.val)
        return [res for res in result if res != target.val]


def verticalTraversal(root: TreeNode, ver: int):
    if not root:
        return
    if not root.left and not root.right:
        root.ver = ver
        return
    root.ver = ver
    verticalTraversal(root.left, ver - 1)
    verticalTraversal(root.right, ver + 1)


res = {}


def traverse(root: TreeNode):
    if not root:
        return
    if not root.left and not root.right:
        if root.ver in res:
            res[root.ver].append(root.val)
        else:
            res[root.ver] = [root.val]
        return
    if root.ver in res:
        res[root.ver].append(root.val)
    else:
        res[root.ver] = [root.val]
    traverse(root.left)
    traverse(root.right)


root1 = levelOrderBuildTree([1, 2, 3, 4, 5, 6, 7, -1, -1, -1, -1, -1, 8, -1, 9])
verticalTraversal(root1, 0)
traverse(root1)


# print(res)


def redundantParenthesis(exp: str):
    stack = []
    for i in exp:
        if i != ")":
            stack.append(i)
        else:
            popped = stack.pop()
            operator = False
            while popped != "(":
                if popped in ["+", "-", "*", "/"]:
                    operator = True
                popped = stack.pop()
            if not operator:
                return True
    return False


# print(redundantParenthesis("(a+b)"))
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        root = head
        while root.next is not None:
            nodes.append(root)
            root = root.next
        nodes.append(root)
        i = 0
        j = len(nodes)
        while i < j:
            temp = head.next
            if i + 1 < j - 1:
                head.next = nodes[j - 1]
                head = head.next
                head.next = temp
                head = head.next
            i += 2
            j -= 1


# s = Solution()


# a = ListNode(
#     1,
#     ListNode(
#         2,
#         ListNode(
#             3,
#             ListNode(
#                 4,
#                 ListNode(
#                     5,
#                     ListNode(
#                         6,
#                         ListNode(
#                             7,
#                             ListNode(
#                                 8,
#                                 ListNode(
#                                     9,
#                                     ListNode(
#                                         10,
#                                         ListNode(
#                                             11,
#                                             ListNode(
#                                                 12,
#                                                 ListNode(
#                                                     13,
#                                                     ListNode(
#                                                         14, ListNode(15, ListNode(16))
#                                                     ),
#                                                 ),
#                                             ),
#                                         ),
#                                     ),
#                                 ),
#                             ),
#                         ),
#                     ),
#                 ),
#             ),
#         ),
#     ),
# )
# a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# s.reorderList(a)
# # print(a.next.next.next.next.next.next.next.next.next.val)
# # while a.next:
# #     print(a.val)
# #     a = a.next
# print(
#     a.val, a.next.val, a.next.next.val, a.next.next.next.val, a.next.next.next.next.val
# )
# print(a.next.next.next.next.next.val)


class Solution:
    def firstNonRepeatingChar(self, s: str) -> str:
        d = {}
        q = []
        res = ""
        for i in s:
            if i not in d:
                d[i] = False
        for i in s:
            if not d[i]:
                q.append(i)
                d[i] = True
            else:
                if i in q:
                    q.remove(i)
            if len(q) == 0:
                res += "0"
            else:
                res += q[0]
        return res


s = Solution()


# print(s.firstNonRepeatingChar("aabcbcd"))
# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         li = list(filter(lambda x: x != "", path.split("/")[1:]))
#         stack = []
#         for item in li:
#             if item == "..":
#                 if len(stack) > 0:
#                     stack.pop()
#             elif item != ".":
#                 stack.append(item)
#         res = "/"
#         for item in stack:
#             res += f"{item}/"
#         return res[:-1] if len(res) > 1 else res
#
#
# s = Solution()
# print(s.simplifyPath("/home//foo"))


class Solution:
    def reverseK(self, head: ListNode, k: int):
        temp = None
        root = head
        for j in range(1000000):
            for i in range(k):
                nex = head.next
                head.next = temp
                if not nex:
                    if j == 0:
                        return head
                    for _ in range(k - 1):
                        if root.next:
                            root = root.next
                    temp = None
                    if i != k - 1:
                        for x in range(i + 1):
                            nex = head.next
                            head.next = temp
                            temp = head
                            if x != i:
                                head = nex
                    root.next = deepcopy(head)
                    return res
                temp = head
                if i != k - 1:
                    head = nex
            if j == 0:
                root = head
                res = root
            else:
                for _ in range(k - 1):
                    root = root.next
                root.next = deepcopy(head)
                root = root.next
            nextCycleHead = nex
            for _ in range(k - 1):
                head = head.next
            head.next = nextCycleHead
            head = head.next
            temp = None


# s = Solution()
# h1 = s.reverseK(
#     ListNode(
#         1,
#         ListNode(
#             2,
#             ListNode(
#                 3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))),
#             ),
#         ),
#     ),
#     3,
# )
# for i in range(8):
#     print(h1.val)
#     h1 = h1.next
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g1 = Graph(numCourses)
        g2 = Graph(numCourses)
        for item in prerequisites:
            g1.addEdge(item[1], item[0], directed=True)
            g2.addEdge(item[0], item[1], directed=True)
        cur = []
        for idx, li in enumerate(g1.graph):
            if len(li) == 0:
                cur.append(idx)
        res = []
        while len(cur) > 0:
            popped = cur.pop(0)
            res.append(popped)
            for idx, li in enumerate(g2.graph[popped]):
                if popped in g1.graph[li]:
                    g1.graph[li].remove(popped)
                    if len(g1.graph[li]) == 0:
                        cur.append(li)
        return res[::-1] if len(res) == numCourses else []


# s = Solution()
# print(s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         fast = head
#         root = head
#         while fast and fast.next:
#             if fast.next and fast.next.next and fast.next.next.next:
#                 fast = fast.next.next
#                 head = head.next
#             else:
#                 if head.next.next is not None:
#                     head.next = head.next.next
#                 else:
#                     head.next = None
#         return root, head
#
#
# a = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# s = Solution()
# r, h = s.deleteMiddle(a)
# for _ in range(3):
#     print(h.val)
#     h = h.next
class Solution:
    class Node:
        def __init__(self, node: ListNode, count: int, next=None, back=None):
            self.node = node
            self.count = count
            self.next = next
            self.back = back

    def reorderList(self, head: Optional[ListNode]):
        """
        Do not return anything, modify head in-place instead.
        """
        root = head
        front = self.Node(head, 1)
        f = front
        while root.next:
            front.next = self.Node(root.next, front.count + 1, back=front)
            root = root.next
            front = front.next
        b = front
        res = f.node
        final = res
        f = f.next
        if not f:
            return final
        while f.count <= b.count:
            if b.back:
                res.next = b.node
                b = b.back
                res = res.next
            if f.next:
                res.next = f.node
                f = f.next
                res = res.next
        res.next = None
        return final


# s = Solution()
# a = s.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
#
# for _ in range(5):
#     print(a.val)
#     a = a.next
a = BSTNode(30, BSTNode(15), BSTNode(50))
a = insert(a, 8)
a = insert(a, 12)
a = insert(a, 40)
a = insert(a, 25)
a = deleteNode(a, 15)
print(a.val, a.left.val, a.left.left.val, a.left.left.right.val, a.right.val)
