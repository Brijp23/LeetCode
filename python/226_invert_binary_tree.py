# 226. Invert Binary Tree — Easy
# https://leetcode.com/problems/invert-binary-tree/
#
# Mirror a binary tree (swap every left and right child).
#
# Approach: recursive DFS — swap children at each node, recurse.
# Time: O(n)  Space: O(h) where h = tree height

from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def level_order(root):
    if not root:
        return []
    from collections import deque
    q, result = deque([root]), []
    while q:
        node = q.popleft()
        result.append(node.val)
        if node.left:  q.append(node.left)
        if node.right: q.append(node.right)
    return result


if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    assert level_order(invert_tree(root)) == [4, 7, 2, 9, 6, 3, 1]
    print("All tests passed.")
